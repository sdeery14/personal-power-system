"""Geometry checks for the PRELIMINARY Diesel Heater Module (002) model, all three variants.

These tests check counts, nominal dimensions, orientation, member end-face
contact under the documented joint assumption, and the reported mounting-hole
relationships. They do not check clearances, interference, loads, joint
strength, or any engineering adequacy, and passing them opens no release gate.
The bounding-box separations they assert are modelled placeholder distances,
not safe clearances.
"""

import re

import cadquery as cq
import pytest

import params as P
from model import MEMBER_ROLES, PLACEHOLDER_ROLES, build_assembly, build_parts, by_id, members

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


def rng(b, ax):
    return getattr(b, f"{ax}min"), getattr(b, f"{ax}max")


def contains(outer, inner):
    return outer[0] <= inner[0] + TOL and inner[1] <= outer[1] + TOL


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
    if variant.plate_holes:
        expected |= {f"plate_hole_{j}" for j in (1, 2, 3, 4)}
    assert set(ids) == expected


def test_part_count_per_variant(parts, variant):
    assert len(parts) == {"original": 27, "compact": 28, "adjusted": 32}[variant.key]


B1_VARIANTS = [P.COMPACT, P.ADJUSTED]
B1_IDS = [v.key for v in B1_VARIANTS]


def test_roles_partition_members_and_placeholders(parts):
    """Every part is either a member (an axis and a length) or a placeholder; nothing falls between."""
    assert not set(MEMBER_ROLES) & set(PLACEHOLDER_ROLES)
    for p in parts:
        assert p.role in MEMBER_ROLES or p.role in PLACEHOLDER_ROLES, p.id
        if p.role in MEMBER_ROLES:
            assert p.axis in ("X", "Y", "Z") and p.length > 0, p.id
        assert p.basis and p.note, p.id
    assert set(members(parts)) == {p for p in parts if p.role in MEMBER_ROLES}


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
    assert (P.ADJUSTED.envelope_w, P.ADJUSTED.envelope_d, P.ADJUSTED.envelope_h) == pytest.approx((20 * P.IN, 22 * P.IN, 35 * P.IN))
    assert P.DEFAULT_VARIANT is P.ADJUSTED


def test_everything_inside_envelope(parts, variant):
    whole = cq.Compound.makeCompound([p.shape for p in parts]).BoundingBox()
    assert whole.xmin >= -TOL and whole.ymin >= -TOL and whole.zmin >= -TOL
    assert whole.xmax <= variant.envelope_w + TOL
    assert whole.ymax <= variant.envelope_d + TOL
    assert whole.zmax <= variant.envelope_h + TOL


def test_profile_is_2020_square():
    """Owner decision 2026-10-29: 2020 (20 x 20 mm) T-slot, 6 mm slot, for every member."""
    assert P.PROFILE_MINOR == P.PROFILE_MAJOR == 20.0
    assert P.SLOT_WIDTH == 6.0


def test_every_member_has_2020_section(parts):
    for p in members(parts):
        b = bb(p)
        dims = sorted([b.xlen, b.ylen, b.zlen])
        assert dims[0] == pytest.approx(P.PROFILE_MINOR, abs=TOL), p.id
        assert dims[1] == pytest.approx(P.PROFILE_MAJOR, abs=TOL), p.id
        assert dims[2] == pytest.approx(p.length, abs=TOL), p.id
        assert getattr(b, f"{p.axis.lower()}len") == pytest.approx(p.length, abs=TOL), p.id


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


@pytest.mark.parametrize("b1", B1_VARIANTS, ids=B1_IDS)
def test_b1_heater_length_parallel_to_tank_broad_face(b1):
    """B1 layouts: the 13.4 in body runs along Y, parallel to the tank's YZ broad face."""
    parts = build_parts(b1)
    h, t = bb(by_id(parts, "heater_body")), bb(by_id(parts, "fuel_tank"))
    assert h.ylen == pytest.approx(P.HEATER_L, abs=TOL)
    assert t.ylen > t.xlen and t.zlen > t.xlen


# -------------------------------------------------------- member end-face contact

def test_every_horizontal_member_butts_face_to_face(parts):
    """Under the documented joint assumption every horizontal member butts against another
    member at both ends: its end face is coplanar with, and fully inside, a face of that member.

    Edge-only contact or a gap fails. This checks the modelled geometry only; it says nothing
    about connectors, load paths, or joint strength (D-01, D-02, MR-04 open).
    """
    ms = members(parts)
    for m in ms:
        if m.axis == "Z":
            continue
        ax = m.axis.lower()
        others = [o for o in ("x", "y", "z") if o != ax]
        b = bb(m)
        for end in ("min", "max"):
            coord = getattr(b, f"{ax}{end}")
            opposite = "max" if end == "min" else "min"
            supported = False
            for q in ms:
                if q is m:
                    continue
                qb = bb(q)
                if abs(getattr(qb, f"{ax}{opposite}") - coord) > TOL:
                    continue
                if all(contains(rng(qb, o), rng(b, o)) for o in others):
                    supported = True
                    break
            assert supported, f"{m.id} end at {ax}={coord:.1f} has no full face contact"


def test_tank_rails_butt_between_the_x_min_uprights(parts, variant):
    """Rail end faces lie fully on the inside faces of U1 and U3 (the X-min uprights)."""
    u1, u3 = bb(by_id(parts, "U1")), bb(by_id(parts, "U3"))
    for rid in ("TR-lower", "TR-upper"):
        r = bb(by_id(parts, rid))
        assert r.ymin == pytest.approx(u1.ymax, abs=TOL) and r.ymax == pytest.approx(u3.ymin, abs=TOL), rid
        for u in (u1, u3):
            assert contains(rng(u, "x"), rng(r, "x")), rid  # the whole end face is on the upright, not just an edge
            assert contains(rng(u, "z"), rng(r, "z")), rid
        assert r.xmin == pytest.approx(0.0, abs=TOL) and r.xmax == pytest.approx(P.PROFILE_MINOR, abs=TOL), rid


# ----------------------------------------------------- mounting relationships

def test_plate_rests_on_both_crossmembers_full_contact(parts, variant):
    """The plate's bottom face touches the top face of each crossmember, and the plate lies
    within the crossmember's X extent. Illustrative-spacing variants: the crossmember lies
    within the plate's Y extent. Plate-hole variants: the crossmember's centre line (its slot
    line) sits under the reported hole line, 6.35 mm in from the plate edge, so the 20 mm
    member overhangs the plate edge by 3.65 mm and the contact patch is 16.35 mm wide."""
    pl = bb(by_id(parts, "heater_plate"))
    for cid, edge in (("HX1", "ymin"), ("HX2", "ymax")):
        c = bb(by_id(parts, cid))
        assert pl.zmin == pytest.approx(c.zmax, abs=TOL), cid
        assert contains(rng(c, "x"), rng(pl, "x")), cid
        if variant.plate_holes:
            hole_line = getattr(pl, edge) + (P.PLATE_HOLE_INSET if edge == "ymin" else -P.PLATE_HOLE_INSET)
            assert c.center.y == pytest.approx(hole_line, abs=TOL), cid
            overlap = min(c.ymax, pl.ymax) - max(c.ymin, pl.ymin)
            assert overlap == pytest.approx(P.PROFILE_MINOR / 2 + P.PLATE_HOLE_INSET, abs=TOL), cid
            assert overlap >= 0.75 * P.PROFILE_MINOR, cid
        else:
            assert contains(rng(pl, "y"), rng(c, "y")), cid


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
        if p.id in ("heater_plate", "heater_body", "HX1", "HX2", "heater_outlet_cue") or p.role == "hole_marker":
            continue  # plate hole markers pass through the plate and crossmember top by design
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


def test_tank_hangs_on_rail_inside_face_with_filler_at_top_corner(parts):
    t, f = bb(by_id(parts, "fuel_tank")), bb(by_id(parts, "tank_filler_neck"))
    rails = [bb(by_id(parts, r)) for r in ("TR-lower", "TR-upper")]
    assert t.zlen > t.xlen and t.ylen > t.xlen  # broad face vertical, thin in X
    for r in rails:
        assert t.xmin == pytest.approx(r.xmax, abs=TOL)  # broad face on the rails' inside face
        assert contains(rng(t, "y"), rng(r, "y")) or contains(rng(r, "y"), rng(t, "y"))
        assert contains(rng(t, "z"), rng(r, "z"))  # each rail lies within the tank's height
    assert f.zmin == pytest.approx(t.zmax, abs=TOL)
    assert f.center.y == pytest.approx(t.ymin + P.FILLER_CORNER_INSET, abs=TOL)  # near the Y-min corner, not centred
    assert f.center.y < t.center.y - 0.25 * t.ylen
    assert t.xmin < f.center.x < t.xmax and t.ymin < f.ymin and f.ymax < t.ymax


# ------------------------------------------------------- layout relationships

def test_relative_elevations(parts, variant):
    h, t = bb(by_id(parts, "heater_body")), bb(by_id(parts, "fuel_tank"))
    if variant.layout == "stacked":
        assert t.zmin > h.zmax  # tank entirely above the heater (A Original)
    elif variant.layout == "beside":
        # B1 Compact: tank bottom above the heater's bottom, below the heater's top; tank top above the heater
        assert h.zmin < t.zmin < h.zmax < t.zmax
        assert t.zmin == pytest.approx(8 * P.IN, abs=TOL)
        assert bb(by_id(parts, "heater_plate")).zmin == pytest.approx(7 * P.IN, abs=TOL)
    else:
        # B1 Adjusted: plate underside at 7 in; tank bottom above the heater body top by the provisional gap
        assert variant.layout == "beside-above"
        assert bb(by_id(parts, "heater_plate")).zmin == pytest.approx(7 * P.IN, abs=TOL)
        assert t.zmin - h.zmax == pytest.approx(P.TANK_GAP_ABOVE_HEATER, abs=TOL)
        assert t.zmin > h.zmax


@pytest.mark.parametrize("b1", B1_VARIANTS, ids=B1_IDS)
def test_b1_footprints_separate(b1):
    """B1 layouts: tank, heater, and plate occupy separate horizontal zones; no vertical stacking."""
    parts = build_parts(b1)
    t = bb(by_id(parts, "fuel_tank"))
    for pid in ("heater_body", "heater_plate", "heater_outlet_cue"):
        assert footprints_disjoint(t, bb(by_id(parts, pid))), pid
    assert t.xmax < bb(by_id(parts, "heater_plate")).xmin  # tank at X-min, heater toward X-max


@pytest.mark.parametrize("b1", B1_VARIANTS, ids=B1_IDS)
def test_b1_modelled_gaps_are_positive_not_clearances(b1):
    """Reports modelled bounding-box gaps. These are placeholder distances, not safe clearances."""
    parts = build_parts(b1)
    t, h, pl = (bb(by_id(parts, n)) for n in ("fuel_tank", "heater_body", "heater_plate"))
    assert h.xmin - t.xmax > 0
    assert pl.xmin - t.xmax > 0
    for cid in ("HX1", "HX2"):
        assert t.zmin - bb(by_id(parts, cid)).zmax > 0  # crossmembers pass beneath the tank with a gap


# ------------------------------------------------------- B1 Adjusted specifics

def test_adjusted_crossmember_spacing_is_the_reported_hole_pitch():
    """The spacing is derived, not measured: 5 7/16 in minus twice (1/8 in clearance + 1/8 in radius)."""
    assert P.PLATE_HOLE_INSET == pytest.approx(0.25 * P.IN, abs=TOL)
    assert P.PLATE_HOLE_PITCH_ALONG == pytest.approx((5 + 7 / 16) * P.IN - 0.5 * P.IN, abs=TOL)
    assert P.ADJUSTED.crossmember_spacing == pytest.approx(P.PLATE_HOLE_PITCH_ALONG, abs=TOL)
    assert P.PLATE_T == pytest.approx(P.IN / 32, abs=TOL) and P.PLATE_T < P.IN / 16


def test_adjusted_plate_holes_at_reported_inset_and_on_crossmember_lines():
    """Four markers 6.35 mm in from each adjacent plate edge, at the reported diameter, each
    passing through the plate and into a crossmember's top face (where a slot line would be)."""
    parts = build_parts(P.ADJUSTED)
    pl = bb(by_id(parts, "heater_plate"))
    holes = [bb(by_id(parts, f"plate_hole_{j}")) for j in (1, 2, 3, 4)]
    expect = {(round(x, 2), round(y, 2)) for x in (pl.xmin + P.PLATE_HOLE_INSET, pl.xmax - P.PLATE_HOLE_INSET)
              for y in (pl.ymin + P.PLATE_HOLE_INSET, pl.ymax - P.PLATE_HOLE_INSET)}
    assert {(round(h.center.x, 2), round(h.center.y, 2)) for h in holes} == expect
    hx = [bb(by_id(parts, c)) for c in ("HX1", "HX2")]
    for h in holes:
        assert h.xlen == pytest.approx(P.PLATE_HOLE_D, abs=TOL) and h.ylen == pytest.approx(P.PLATE_HOLE_D, abs=TOL)
        assert h.zmin < pl.zmin < pl.zmax < h.zmax  # through the plate
        on = [c for c in hx if c.xmin < h.center.x < c.xmax and c.ymin < h.center.y < c.ymax and c.zmax > h.zmin]
        assert len(on) == 1, "each hole line lies on exactly one crossmember top face"
        assert on[0].center.y == pytest.approx(h.center.y, abs=TOL)


def test_adjusted_filler_headroom_and_reach_are_reported_not_cleared():
    """Geometric fit only: the tank top plus the filler/cap allowance stays below the top members,
    and the filler cue sits inside the top rectangle in plan so it is reachable from above.
    Whether a can or spout can actually be used there is for review (SR-02, SR-09), not this test."""
    parts = build_parts(P.ADJUSTED)
    t, f = bb(by_id(parts, "fuel_tank")), bb(by_id(parts, "tank_filler_neck"))
    top_band_bottom = P.ADJUSTED.level_z[2]
    assert t.zmax + P.FILLER_CAP_ALLOWANCE <= top_band_bottom + TOL
    assert f.zmax < top_band_bottom
    assert f.xmin > P.PROFILE_MINOR  # clear of the X-min top member in plan
    assert P.ADJUSTED.envelope_h - t.zmax > P.PROFILE_MAJOR  # tank top below the top-member band


def test_adjusted_keeps_the_twenty_member_frame():
    """The 18-member simplification is a recorded, deprioritized alternative (design.md D-14), not modelled."""
    parts = build_parts(P.ADJUSTED)
    assert len(members(parts)) == 20
    assert {p.id for p in members(parts)} == {p.id for p in members(build_parts(P.COMPACT))}


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
    text = path.read_text(encoding="utf-8", errors="replace")
    products = re.findall(r"PRODUCT\('([^']*)'", text)
    root = f"diesel_heater_module_{variant.key}_PRELIMINARY"
    # Exactly one PRODUCT per component plus the root, each name exactly once, nothing extra.
    assert sorted(products) == sorted([p.id for p in parts] + [root])
    # One assembly occurrence per component under the root.
    assert len(re.findall(r"NEXT_ASSEMBLY_USAGE_OCCURRENCE\(", text)) == len(parts)
    # Every re-imported solid matches some component's nominal bounding box, so the geometry
    # round-trips. This does NOT prove which PRODUCT name is attached to which solid: the names,
    # the occurrence count, and the solids are checked independently. Name-to-solid binding is
    # left for a later phase.
    boxes = {p.id: bb(p) for p in parts}
    for solid in reimported.solids().vals():
        sb = solid.BoundingBox()
        assert any(all(abs(getattr(sb, k) - getattr(b, k)) < 0.1 for k in ("xmin", "xmax", "ymin", "ymax", "zmin", "zmax"))
                   for b in boxes.values())


# ------------------------------------------------------------- build outputs

def test_schedule_and_comparison_carry_banner(tmp_path):
    from build import BANNER, write_comparison_md, write_schedule

    parts_by_key = {k: build_parts(v) for k, v in P.VARIANTS.items()}
    for k, v in P.VARIANTS.items():
        write_schedule(parts_by_key[k], tmp_path / f"{k}.md", v)
        text = (tmp_path / f"{k}.md").read_text(encoding="utf-8")
        assert BANNER in text and "not a cut list" in text and v.title in text
        assert "| no |" not in text  # no member is presented as non-provisional
        assert "20 × 20" in text and "20 × 40" not in text
    write_comparison_md(parts_by_key, tmp_path / "comparison.md")
    text = (tmp_path / "comparison.md").read_text(encoding="utf-8")
    assert BANNER in text and "do not establish safe" in text


# ------------------------------------------------------- cut schedule (proposed)

def test_adjusted_nominal_lengths_for_2020():
    """With a square 20 mm section the depth members and rails run between uprights 20 mm
    wide, so they are 40 mm longer than under the withdrawn 20 x 40 assumption."""
    parts = build_parts(P.ADJUSTED)
    lengths = {p.id: p.length for p in members(parts)}
    assert all(lengths[f"U{i}"] == pytest.approx(35 * P.IN) for i in (1, 2, 3, 4))
    for pid in [f"L{l}-W{j}" for l in (1, 2, 3) for j in (1, 2)] + ["HX1", "HX2"]:
        assert lengths[pid] == pytest.approx(20 * P.IN - 2 * P.PROFILE_MINOR), pid  # 468.0
    for pid in [f"L{l}-D{j}" for l in (1, 2, 3) for j in (1, 2)] + ["TR-lower", "TR-upper"]:
        assert lengths[pid] == pytest.approx(22 * P.IN - 2 * P.PROFILE_MAJOR), pid  # 518.8
    assert sum(lengths.values()) == pytest.approx(4 * 889.0 + 8 * 468.0 + 8 * 518.8, abs=0.1)


def test_cut_pieces_are_members_plus_two_foot_bars():
    from build import cut_pieces

    parts = build_parts(P.ADJUSTED)
    pieces = cut_pieces(parts)
    assert len(pieces) == 22
    assert [pid for pid, _, _ in pieces[-2:]] == ["FB1", "FB2"]
    assert all(length == pytest.approx(P.FOOT_BAR_L) for _, length, _ in pieces[-2:])
    assert P.FOOT_BAR_L == pytest.approx(708.0)
    assert sum(length for _, length, _ in pieces) == pytest.approx(12866.4, abs=0.1)
    assert len(cut_pieces(parts, include_foot_bars=False)) == 20


def test_pack_stock_respects_stock_length_and_kerf():
    from build import pack_stock

    bars = pack_stock([900.0, 900.0, 300.0], stock=2000.0, kerf=3.0)
    assert sorted(map(sorted, bars)) == [[300.0], [900.0, 900.0]]  # 900 + 900 + 2 kerfs = 1806; the 300 would need 2109
    assert pack_stock([1000.0, 997.0], stock=2000.0, kerf=3.0) == [[1000.0], [997.0]]  # 1000 + 997 + 2 kerfs = 2003 > 2000
    assert pack_stock([1000.0, 994.0], stock=2000.0, kerf=3.0) == [[1000.0, 994.0]]  # exactly 2000
    # first-fit-decreasing would use 8 bars for the concept's pieces; the exact search finds 7
    concept = [889.0] * 4 + [468.0] * 8 + [518.8] * 8 + [708.0] * 2
    assert len(pack_stock(concept, stock=2000.0, kerf=3.0)) == 7
    with pytest.raises(ValueError):
        pack_stock([2000.0], stock=2000.0, kerf=3.0)


def test_adjusted_cut_schedule_packs_into_seven_bars(tmp_path):
    """The proposed order for the concept: 7 x 2000 mm. Each bar's pieces plus one kerf per
    piece fit the stock; every piece is placed exactly once. A sizing estimate, not a cut list."""
    from build import BANNER, cut_pieces, write_cut_schedule

    parts = build_parts(P.ADJUSTED)
    bars = write_cut_schedule(parts, tmp_path / "cut-schedule.md", P.ADJUSTED)
    assert len(bars) == 7
    placed = sorted(x for bar in bars for x in bar)
    assert placed == sorted(length for _, length, _ in cut_pieces(parts))
    for bar in bars:
        assert sum(bar) + P.KERF_ALLOWANCE * len(bar) <= P.STOCK_LENGTH
    text = (tmp_path / "cut-schedule.md").read_text(encoding="utf-8")
    assert BANNER in text and "Proposed, not approved" in text and "7 × 2000 mm" in text
    assert "12.866 m" in text and "FB1, FB2" in text and "20 × 40" not in text


def test_comparison_png_is_parallel_projection_at_one_scale(tmp_path):
    """The comparison scene uses parallel projection, and a 100 mm segment at each variant's
    origin projects to the same pixel length (perspective would shrink the farther one)."""
    import build

    parts_by_key = {k: build_parts(v) for k, v in P.VARIANTS.items()}
    path = tmp_path / "comparison.png"
    win, ren = build.write_comparison_png(parts_by_key, path)
    assert path.exists() and path.stat().st_size > 10_000
    assert ren.GetActiveCamera().GetParallelProjection() == 1
    offsets = build.comparison_offsets(list(parts_by_key))

    def pixels(x0, y0, z0, dx, dy, dz):
        pts = []
        for x, y, z in ((x0, y0, z0), (x0 + dx, y0 + dy, z0 + dz)):
            ren.SetWorldPoint(x, y, z, 1.0)
            ren.WorldToDisplay()
            pts.append(ren.GetDisplayPoint()[:2])
        return ((pts[1][0] - pts[0][0]) ** 2 + (pts[1][1] - pts[0][1]) ** 2) ** 0.5

    lengths = {}
    for key, x_off in offsets.items():
        v = P.VARIANTS[key]
        # a 100 mm vertical segment at the near-left and far-right corners of each frame
        lengths[key] = (pixels(x_off, 0, 0, 0, 0, 100), pixels(x_off + v.envelope_w, v.envelope_d, 0, 0, 0, 100))
    flat = [px for pair in lengths.values() for px in pair]
    assert max(flat) - min(flat) < 0.5, f"projected 100 mm segments differ: {lengths}"
    del win


def valid_png(path, size=(16, 12)):
    """Write a small but complete, decodable PNG (the mocks must not weaken output validation)."""
    from PIL import Image

    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, (250, 250, 250)).save(path)


def _mock_png_writer(behaviour: dict):
    """A write_png replacement; ``behaviour`` maps file name -> 'raise' | 'nothing' | 'garbage' | 'truncated' | 'ok'."""
    calls = []

    def fake_write_png(parts, path, variant, *args):
        calls.append(path.name)
        mode = behaviour.get(path.name, "ok")
        if mode == "raise":
            raise RuntimeError("simulated renderer failure")
        if mode == "nothing":
            return None  # returns normally, creates no file
        if mode == "garbage":
            path.write_bytes(b"\x89PNG\r\n\x1a\n garbage that is not a PNG stream")
        elif mode == "truncated":
            valid_png(path, (64, 64))
            data = path.read_bytes()
            path.write_bytes(data[: int(len(data) * 0.6)])  # header intact, IDAT cut short
        else:
            valid_png(path)
        return None

    return fake_write_png, calls


def _assert_other_outputs_kept(out_dir):
    for name in ("heater-module.step", "isometric.svg", "member-schedule.md"):
        assert (out_dir / name).stat().st_size > 0, name


def test_build_fails_when_renderer_raises(tmp_path, monkeypatch):
    """A render exception gives a non-zero exit status, removes the stale PNG, and keeps the other outputs."""
    import build

    monkeypatch.setattr(build, "OUT", tmp_path)
    stale = tmp_path / "compact" / "top.png"
    stale.parent.mkdir(parents=True)
    stale.write_bytes(b"old image")
    fake, calls = _mock_png_writer({"top.png": "raise"})
    monkeypatch.setattr(build, "write_png", fake)
    assert build.main(["--variant", "compact"]) == 1
    assert not stale.exists(), "a stale PNG survived a failed render"
    build.validate_png(tmp_path / "compact" / "isometric.png")
    build.validate_png(tmp_path / "compact" / "front-elevation.png")
    _assert_other_outputs_kept(tmp_path / "compact")
    assert calls == ["isometric.png", "top.png", "front-elevation.png"]


def test_build_fails_when_renderer_returns_without_creating_png(tmp_path, monkeypatch):
    """Codex finding: a writer that fails natively returns normally and leaves no file."""
    import build

    monkeypatch.setattr(build, "OUT", tmp_path)
    stale = tmp_path / "compact" / "isometric.png"
    stale.parent.mkdir(parents=True)
    stale.write_bytes(b"old image")
    fake, _ = _mock_png_writer({"isometric.png": "nothing"})
    monkeypatch.setattr(build, "write_png", fake)
    assert build.main(["--variant", "compact"]) == 1
    assert not stale.exists()
    build.validate_png(tmp_path / "compact" / "top.png")
    _assert_other_outputs_kept(tmp_path / "compact")


def test_build_fails_on_invalid_or_truncated_png(tmp_path, monkeypatch, capsys):
    import build

    monkeypatch.setattr(build, "OUT", tmp_path)
    fake, _ = _mock_png_writer({"top.png": "garbage", "front-elevation.png": "truncated"})
    monkeypatch.setattr(build, "write_png", fake)
    assert build.main(["--variant", "compact"]) == 1
    assert not (tmp_path / "compact" / "top.png").exists(), "garbage file left under the output name"
    assert not (tmp_path / "compact" / "front-elevation.png").exists(), "truncated file left under the output name"
    build.validate_png(tmp_path / "compact" / "isometric.png")
    err = capsys.readouterr().err
    assert "BUILD FAILED: 2" in err and "compact/top.png" in err and "compact/front-elevation.png" in err
    _assert_other_outputs_kept(tmp_path / "compact")


def test_build_fails_when_comparison_png_is_missing_or_invalid(tmp_path, monkeypatch):
    import build

    monkeypatch.setattr(build, "OUT", tmp_path)
    fake, _ = _mock_png_writer({})
    monkeypatch.setattr(build, "write_png", fake)
    monkeypatch.setattr(build, "write_comparison_png", lambda pk, path: None)  # creates nothing
    assert build.main([]) == 1
    assert not (tmp_path / "comparison.png").exists() and (tmp_path / "comparison.md").exists()
    monkeypatch.setattr(build, "write_comparison_png", lambda pk, path: path.write_bytes(b"\x89PNG partial"))
    assert build.main([]) == 1
    assert not (tmp_path / "comparison.png").exists()


def test_build_succeeds_with_valid_pngs(tmp_path, monkeypatch, capsys):
    import build

    monkeypatch.setattr(build, "OUT", tmp_path)
    fake, _ = _mock_png_writer({})
    monkeypatch.setattr(build, "write_png", fake)
    monkeypatch.setattr(build, "write_comparison_png", lambda pk, path: valid_png(path, (40, 20)))
    assert build.main([]) == 0
    assert "BUILD OK" in capsys.readouterr().out
    for rel in ("original/isometric.png", "original/tank-side.png", "compact/isometric.png",
                "compact/top.png", "compact/front-elevation.png", "adjusted/isometric.png",
                "adjusted/top.png", "adjusted/front-elevation.png", "comparison.png"):
        build.validate_png(tmp_path / rel)
    assert (tmp_path / "comparison.md").exists()


def test_native_vtk_writer_failure_is_detected(tmp_path, monkeypatch):
    """Reproduces the Codex report: vtkPNGWriter cannot open an unwritable destination, raises no
    Python exception, and produces no file. The real render path must still fail the build."""
    import build

    monkeypatch.setattr(build, "OUT", tmp_path)
    view = build.VIEWS["compact"][1]  # the top view, a cheap parallel render
    monkeypatch.setitem(build.VIEWS, "compact", [("missing-dir/top.png", *view[1:])])
    status = build.main(["--variant", "compact"])
    assert status == 1
    assert not (tmp_path / "compact" / "missing-dir" / "top.png").exists()
    _assert_other_outputs_kept(tmp_path / "compact")


def test_validate_png_rejects_bad_files_and_accepts_real_render(tmp_path):
    import build

    with pytest.raises(build.RenderError):
        build.validate_png(tmp_path / "absent.png")
    (tmp_path / "empty.png").write_bytes(b"")
    with pytest.raises(build.RenderError):
        build.validate_png(tmp_path / "empty.png")
    (tmp_path / "sig-only.png").write_bytes(b"\x89PNG\r\n\x1a\n")
    with pytest.raises(build.RenderError):
        build.validate_png(tmp_path / "sig-only.png")
    valid_png(tmp_path / "ok.png")
    build.validate_png(tmp_path / "ok.png")
    # a real VTK render of the compact top view validates too
    parts = build_parts(P.COMPACT)
    name, direction, up, parallel, caption = build.VIEWS["compact"][1]
    build.write_png(parts, tmp_path / "real.png", P.COMPACT, direction, up, parallel, caption)
    build.validate_png(tmp_path / "real.png")
