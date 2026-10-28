"""Geometry checks for the PRELIMINARY Diesel Heater Module (002) model, both variants.

These tests check counts, nominal dimensions, orientation, and the reported
mounting-hole relationships. They do not check clearances, interference,
loads, or any engineering adequacy, and passing them opens no release gate.
The bounding-box separations they assert are modelled placeholder distances,
not safe clearances.
"""

import re

import cadquery as cq
import pytest

import params as P
from model import MEMBER_ROLES, build_assembly, build_parts, by_id, members

TOL = 0.05  # mm


@pytest.fixture(scope="module", params=list(P.VARIANTS), ids=list(P.VARIANTS))
def variant(request):
    return P.VARIANTS[request.param]


@pytest.fixture(scope="module")
def parts(variant):
    return build_parts(variant)


def bb(part):
    return part.shape.BoundingBox()


def by_role(parts, role):
    return [p for p in parts if p.role == role]


def footprints_disjoint(a, b):
    """True if the XY footprints of two bounding boxes do not overlap."""
    return a.xmax <= b.xmin + TOL or b.xmax <= a.xmin + TOL or a.ymax <= b.ymin + TOL or b.ymax <= a.ymin + TOL


# ----------------------------------------------------------------- counts

def test_member_counts(parts):
    assert len(by_role(parts, "upright")) == 4
    assert len(by_role(parts, "perimeter_width")) == 6
    assert len(by_role(parts, "perimeter_depth")) == 6
    assert len(by_role(parts, "heater_crossmember")) == 2
    assert len(by_role(parts, "tank_rail")) == 2
    assert len(members(parts)) == 20


def test_identifiers_unique_and_stable(parts, variant):
    ids = [p.id for p in parts]
    assert len(ids) == len(set(ids))
    expected = {"U1", "U2", "U3", "U4", "HX1", "HX2", "TR-lower", "TR-upper",
                "heater_body", "heater_plate", "fuel_tank", "tank_filler_neck",
                "tank_hole_lower_a", "tank_hole_lower_b", "tank_hole_upper"}
    expected |= {f"L{l}-W{j}" for l in (1, 2, 3) for j in (1, 2)}
    expected |= {f"L{l}-D{j}" for l in (1, 2, 3) for j in (1, 2)}
    if variant.outlet_end:
        expected.add("heater_outlet_cue")
    assert set(ids) == expected


def test_part_count_per_variant(parts, variant):
    assert len(parts) == {"original": 27, "compact": 28}[variant.key]


# ------------------------------------------------------------- dimensions

def test_envelope(parts, variant):
    frame = cq.Compound.makeCompound([p.shape for p in members(parts)]).BoundingBox()
    assert frame.xlen == pytest.approx(variant.envelope_w, abs=TOL)
    assert frame.ylen == pytest.approx(variant.envelope_d, abs=TOL)
    assert frame.zlen == pytest.approx(variant.envelope_h, abs=TOL)
    assert (frame.xmin, frame.ymin, frame.zmin) == pytest.approx((0, 0, 0), abs=TOL)


def test_variant_envelopes_are_the_briefed_values():
    assert (P.ORIGINAL.envelope_w, P.ORIGINAL.envelope_d, P.ORIGINAL.envelope_h) == pytest.approx((20 * P.IN, 24 * P.IN, 38 * P.IN))
    assert (P.COMPACT.envelope_w, P.COMPACT.envelope_d, P.COMPACT.envelope_h) == pytest.approx((20 * P.IN, 22 * P.IN, 28 * P.IN))


def test_everything_inside_envelope(parts, variant):
    whole = cq.Compound.makeCompound([p.shape for p in parts]).BoundingBox()
    assert whole.xmin >= -TOL and whole.ymin >= -TOL and whole.zmin >= -TOL
    assert whole.xmax <= variant.envelope_w + TOL
    assert whole.ymax <= variant.envelope_d + TOL
    assert whole.zmax <= variant.envelope_h + TOL


def test_every_member_has_20x40_section(parts):
    for p in members(parts):
        b = bb(p)
        dims = sorted([b.xlen, b.ylen, b.zlen])
        assert dims[0] == pytest.approx(P.PROFILE_MINOR, abs=TOL), p.id
        assert dims[1] == pytest.approx(P.PROFILE_MAJOR, abs=TOL), p.id
        assert dims[2] == pytest.approx(p.length, abs=TOL), p.id


def test_uprights_continuous_full_height(parts, variant):
    for p in by_role(parts, "upright"):
        assert bb(p).zlen == pytest.approx(variant.envelope_h, abs=TOL)


def test_placeholder_sizes_and_heater_orientation(parts, variant):
    h = bb(by_id(parts, "heater_body"))
    pl = bb(by_id(parts, "heater_plate"))
    if variant.heater_axis == "X":
        assert (h.xlen, h.ylen, h.zlen) == pytest.approx((P.HEATER_L, P.HEATER_W, P.HEATER_H), abs=TOL)
        assert (pl.xlen, pl.ylen) == pytest.approx((P.PLATE_ALONG, P.PLATE_ACROSS), abs=TOL)
    else:
        assert (h.xlen, h.ylen, h.zlen) == pytest.approx((P.HEATER_W, P.HEATER_L, P.HEATER_H), abs=TOL)
        assert (pl.xlen, pl.ylen) == pytest.approx((P.PLATE_ACROSS, P.PLATE_ALONG), abs=TOL)
    t = bb(by_id(parts, "fuel_tank"))
    assert (t.xlen, t.ylen, t.zlen) == pytest.approx((P.TANK_X, P.TANK_Y, P.TANK_Z), abs=TOL)


def test_compact_heater_length_parallel_to_tank_broad_face():
    """B1: the 13.4 in body runs along Y, parallel to the tank's YZ broad face."""
    parts = build_parts(P.COMPACT)
    h, t = bb(by_id(parts, "heater_body")), bb(by_id(parts, "fuel_tank"))
    assert h.ylen == pytest.approx(P.HEATER_L, abs=TOL)
    assert t.ylen > t.xlen and t.zlen > t.xlen


# ----------------------------------------------------- mounting relationships

def test_plate_rests_on_both_crossmembers(parts):
    pl = bb(by_id(parts, "heater_plate"))
    for cid in ("HX1", "HX2"):
        c = bb(by_id(parts, cid))
        assert pl.zmin == pytest.approx(c.zmax, abs=TOL), cid
        assert pl.ymin < c.ymin and c.ymax < pl.ymax, cid  # crossmember within the plate footprint


def test_crossmembers_at_middle_level_between_depth_members(parts, variant):
    for cid in ("HX1", "HX2"):
        c = bb(by_id(parts, cid))
        assert c.zmin == pytest.approx(variant.level_mid_z, abs=TOL)
        assert c.xmin == pytest.approx(P.PROFILE_MINOR, abs=TOL)
        assert c.xmax == pytest.approx(variant.envelope_w - P.PROFILE_MINOR, abs=TOL)


def test_heater_sits_on_plate(parts):
    h, pl = bb(by_id(parts, "heater_body")), bb(by_id(parts, "heater_plate"))
    assert h.zmin == pytest.approx(pl.zmax, abs=TOL)
    # The supplied plate is smaller than the heater footprint; it is centred under the body.
    assert (h.center.x, h.center.y) == pytest.approx((pl.center.x, pl.center.y), abs=TOL)


def test_heater_raised_with_open_space_beneath(parts, variant):
    """Nothing but the two crossmembers lies under the plate footprint between the bottom level and the plate."""
    pl = bb(by_id(parts, "heater_plate"))
    bottom_top = P.PROFILE_MAJOR  # top face of the bottom-level members
    assert pl.zmin - bottom_top > 50.0, "no open space under the plate"
    for p in parts:
        if p.id in ("heater_plate", "heater_body", "HX1", "HX2", "heater_outlet_cue"):
            continue
        b = bb(p)
        under = not footprints_disjoint(b, pl) and b.zmax > bottom_top + TOL and b.zmin < pl.zmin - TOL
        assert not under, f"{p.id} intrudes into the space under the heater plate"


def test_tank_holes_match_reported_geometry(parts):
    a, b_, u = (bb(by_id(parts, n)) for n in ("tank_hole_lower_a", "tank_hole_lower_b", "tank_hole_upper"))
    assert a.center.z == pytest.approx(b_.center.z, abs=TOL)  # lower row level
    assert abs(a.center.y - b_.center.y) == pytest.approx(P.HOLE_LOWER_SPACING, abs=TOL)
    assert u.center.z - a.center.z == pytest.approx(P.HOLE_UPPER_RISE, abs=TOL)


def test_lower_holes_on_lower_rail_and_upper_hole_on_upper_rail(parts):
    lower, upper = bb(by_id(parts, "TR-lower")), bb(by_id(parts, "TR-upper"))
    for n in ("tank_hole_lower_a", "tank_hole_lower_b"):
        c = bb(by_id(parts, n)).center
        assert lower.zmin < c.z < lower.zmax and lower.ymin < c.y < lower.ymax, n
        assert not (upper.zmin < c.z < upper.zmax), n
    c = bb(by_id(parts, "tank_hole_upper")).center
    assert upper.zmin < c.z < upper.zmax and upper.ymin < c.y < upper.ymax
    assert not (lower.zmin < c.z < lower.zmax)


def test_hole_markers_pass_through_rail_and_tank(parts):
    t = bb(by_id(parts, "fuel_tank"))
    for n in ("tank_hole_lower_a", "tank_hole_lower_b", "tank_hole_upper"):
        m = bb(by_id(parts, n))
        rail = bb(by_id(parts, "TR-upper" if n == "tank_hole_upper" else "TR-lower"))
        assert m.xmin <= rail.xmin + TOL and m.xmax >= t.xmax - TOL, n
        assert t.ymin < m.center.y < t.ymax and t.zmin < m.center.z < t.zmax, n


def test_tank_upright_on_x_min_wall_with_filler_at_top_corner(parts):
    t, f = bb(by_id(parts, "fuel_tank")), bb(by_id(parts, "tank_filler_neck"))
    assert t.zlen > t.xlen and t.ylen > t.xlen  # broad face vertical, thin in X
    assert t.xmin == pytest.approx(2 * P.PROFILE_MINOR, abs=TOL)  # against the rails on the X-min wall
    assert f.zmin == pytest.approx(t.zmax, abs=TOL)
    assert f.center.y == pytest.approx(t.ymin + P.FILLER_CORNER_INSET, abs=TOL)  # near the Y-min corner, not centred
    assert f.center.y < t.center.y - 0.25 * t.ylen
    assert t.xmin < f.center.x < t.xmax and t.ymin < f.ymin and f.ymax < t.ymax


def test_rails_span_between_uprights(parts, variant):
    for rid in ("TR-lower", "TR-upper"):
        r = bb(by_id(parts, rid))
        assert r.ymin == pytest.approx(P.PROFILE_MAJOR, abs=TOL)
        assert r.ymax == pytest.approx(variant.envelope_d - P.PROFILE_MAJOR, abs=TOL)
        assert r.xmin == pytest.approx(P.PROFILE_MINOR, abs=TOL)


# ------------------------------------------------------- layout relationships

def test_relative_elevations(parts, variant):
    h, t = bb(by_id(parts, "heater_body")), bb(by_id(parts, "fuel_tank"))
    if variant.layout == "stacked":
        assert t.zmin > h.zmax  # tank entirely above the heater (A Original)
    else:
        # B1: tank bottom above the heater's bottom, below the heater's top; tank top above the heater
        assert h.zmin < t.zmin < h.zmax < t.zmax
        assert t.zmin == pytest.approx(8 * P.IN, abs=TOL)
        assert bb(by_id(parts, "heater_plate")).zmin == pytest.approx(7 * P.IN, abs=TOL)


def test_compact_footprints_separate():
    """B1: tank, heater, and plate occupy separate horizontal zones; no vertical stacking."""
    parts = build_parts(P.COMPACT)
    t = bb(by_id(parts, "fuel_tank"))
    for pid in ("heater_body", "heater_plate", "heater_outlet_cue"):
        assert footprints_disjoint(t, bb(by_id(parts, pid))), pid
    assert t.xmax < bb(by_id(parts, "heater_plate")).xmin  # tank at X-min, heater toward X-max


def test_compact_modelled_gaps_are_positive_not_clearances():
    """Reports modelled bounding-box gaps. These are placeholder distances, not safe clearances."""
    parts = build_parts(P.COMPACT)
    t, h, pl = (bb(by_id(parts, n)) for n in ("fuel_tank", "heater_body", "heater_plate"))
    assert h.xmin - t.xmax > 0
    assert pl.xmin - t.xmax > 0
    for cid in ("HX1", "HX2"):
        assert t.zmin - bb(by_id(parts, cid)).zmax > 0  # crossmembers pass beneath the tank with a gap


def test_outlet_cue_on_heater_end(parts, variant):
    if not variant.outlet_end:
        assert all(p.role != "outlet_cue" for p in parts)
        return
    h, c = bb(by_id(parts, "heater_body")), bb(by_id(parts, "heater_outlet_cue"))
    sign, ax = variant.outlet_end[0], variant.outlet_end[1].lower()
    if sign == "+":
        assert getattr(c, f"{ax}min") == pytest.approx(getattr(h, f"{ax}max"), abs=TOL)
    else:
        assert getattr(c, f"{ax}max") == pytest.approx(getattr(h, f"{ax}min"), abs=TOL)
    assert getattr(c, f"{ax}len") == pytest.approx(P.OUTLET_CUE_L, abs=TOL)
    other = "x" if ax == "y" else "y"
    assert getattr(c, f"{other}len") == pytest.approx(P.OUTLET_D, abs=TOL)
    assert c.center.z == pytest.approx(h.center.z, abs=TOL)


def test_nominal_boxes_do_not_overlap(parts):
    """Bounding boxes of everything except the hole markers are pairwise disjoint.

    This is a nominal placement check only. It says nothing about clearances,
    exhaust routing, spill paths, or interference in a real assembly.
    """
    solids = [p for p in parts if p.role != "hole_marker"]
    for i, p in enumerate(solids):
        for q in solids[i + 1:]:
            a, b_ = bb(p), bb(q)
            overlap = (min(a.xmax, b_.xmax) - max(a.xmin, b_.xmin) > TOL and
                       min(a.ymax, b_.ymax) - max(a.ymin, b_.ymin) > TOL and
                       min(a.zmax, b_.zmax) - max(a.zmin, b_.zmin) > TOL)
            assert not overlap, f"{p.id} overlaps {q.id}"


# --------------------------------------------------------------- STEP export

def test_step_export_roundtrip_keeps_components_and_names(parts, variant, tmp_path):
    path = tmp_path / f"roundtrip-{variant.key}.step"
    build_assembly(parts, variant).export(str(path))
    reimported = cq.importers.importStep(str(path))
    assert reimported.solids().size() == len(parts)
    names = set(re.findall(r"PRODUCT\('([^']*)'", path.read_text(encoding="utf-8", errors="replace")))
    missing = {p.id for p in parts} - names
    assert not missing, f"STEP lost component names: {sorted(missing)}"
    assert f"diesel_heater_module_{variant.key}_PRELIMINARY" in names


def test_every_member_role_is_known(parts):
    for p in members(parts):
        assert p.role in MEMBER_ROLES


def test_schedule_and_comparison_carry_banner(tmp_path):
    from build import BANNER, write_comparison_md, write_schedule

    parts_by_key = {k: build_parts(v) for k, v in P.VARIANTS.items()}
    for k, v in P.VARIANTS.items():
        write_schedule(parts_by_key[k], tmp_path / f"{k}.md", v)
        text = (tmp_path / f"{k}.md").read_text(encoding="utf-8")
        assert BANNER in text and "not a cut list" in text and v.title in text
    write_comparison_md(parts_by_key, tmp_path / "comparison.md")
    text = (tmp_path / "comparison.md").read_text(encoding="utf-8")
    assert BANNER in text and "do not establish safe" in text
