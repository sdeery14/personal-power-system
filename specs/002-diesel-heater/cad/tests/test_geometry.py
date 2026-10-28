"""Geometry checks for the PRELIMINARY Diesel Heater Module (002) model.

These tests check counts, nominal dimensions, and the reported mounting-hole
relationships. They do not check clearances, interference, loads, or any
engineering adequacy, and passing them opens no release gate.
"""

import re

import cadquery as cq
import pytest

import params as P
from model import MEMBER_ROLES, build_assembly, build_parts, members

TOL = 0.05  # mm


@pytest.fixture(scope="module")
def parts():
    return build_parts()


def bb(part):
    return part.shape.BoundingBox()


def by_id(parts, pid):
    return next(p for p in parts if p.id == pid)


def by_role(parts, role):
    return [p for p in parts if p.role == role]


# ----------------------------------------------------------------- counts

def test_member_counts(parts):
    assert len(by_role(parts, "upright")) == 4
    assert len(by_role(parts, "perimeter_width")) == 6
    assert len(by_role(parts, "perimeter_depth")) == 6
    assert len(by_role(parts, "heater_crossmember")) == 2
    assert len(by_role(parts, "tank_rail")) == 2
    assert len(members(parts)) == 20


def test_identifiers_unique_and_stable(parts):
    ids = [p.id for p in parts]
    assert len(ids) == len(set(ids))
    expected = {"U1", "U2", "U3", "U4", "HX1", "HX2", "TR-lower", "TR-upper",
                "heater_body", "heater_plate", "fuel_tank", "tank_filler_neck",
                "tank_hole_lower_a", "tank_hole_lower_b", "tank_hole_upper"}
    expected |= {f"L{l}-W{j}" for l in (1, 2, 3) for j in (1, 2)}
    expected |= {f"L{l}-D{j}" for l in (1, 2, 3) for j in (1, 2)}
    assert set(ids) == expected


# ------------------------------------------------------------- dimensions

def test_envelope(parts):
    frame = cq.Compound.makeCompound([p.shape for p in members(parts)]).BoundingBox()
    assert frame.xlen == pytest.approx(P.ENVELOPE_W, abs=TOL)
    assert frame.ylen == pytest.approx(P.ENVELOPE_D, abs=TOL)
    assert frame.zlen == pytest.approx(P.ENVELOPE_H, abs=TOL)
    assert (frame.xmin, frame.ymin, frame.zmin) == pytest.approx((0, 0, 0), abs=TOL)


def test_every_member_has_20x40_section(parts):
    for p in members(parts):
        b = bb(p)
        dims = sorted([b.xlen, b.ylen, b.zlen])
        assert dims[0] == pytest.approx(P.PROFILE_MINOR, abs=TOL), p.id
        assert dims[1] == pytest.approx(P.PROFILE_MAJOR, abs=TOL), p.id
        assert dims[2] == pytest.approx(p.length, abs=TOL), p.id


def test_uprights_continuous_full_height(parts):
    for p in by_role(parts, "upright"):
        assert bb(p).zlen == pytest.approx(P.ENVELOPE_H, abs=TOL)


def test_placeholder_sizes(parts):
    h = bb(by_id(parts, "heater_body"))
    assert (h.xlen, h.ylen, h.zlen) == pytest.approx((P.HEATER_L, P.HEATER_W, P.HEATER_H), abs=TOL)
    pl = bb(by_id(parts, "heater_plate"))
    assert (pl.xlen, pl.ylen) == pytest.approx((P.PLATE_X, P.PLATE_Y), abs=TOL)
    t = bb(by_id(parts, "fuel_tank"))
    assert (t.xlen, t.ylen, t.zlen) == pytest.approx((P.TANK_X, P.TANK_Y, P.TANK_Z), abs=TOL)


# ----------------------------------------------------- mounting relationships

def test_plate_rests_on_both_crossmembers(parts):
    pl = bb(by_id(parts, "heater_plate"))
    for cid in ("HX1", "HX2"):
        c = bb(by_id(parts, cid))
        assert pl.zmin == pytest.approx(c.zmax, abs=TOL), cid
        assert pl.ymin < c.ymin and c.ymax < pl.ymax, cid  # crossmember within the plate footprint


def test_heater_sits_on_plate(parts):
    h, pl = bb(by_id(parts, "heater_body")), bb(by_id(parts, "heater_plate"))
    assert h.zmin == pytest.approx(pl.zmax, abs=TOL)


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


def test_tank_upright_with_filler_at_top(parts):
    t, f = bb(by_id(parts, "fuel_tank")), bb(by_id(parts, "tank_filler_neck"))
    assert t.zlen > t.xlen and t.ylen > t.xlen  # broad face vertical, thin in X
    assert f.zmin == pytest.approx(t.zmax, abs=TOL)


def test_nominal_boxes_do_not_overlap(parts):
    """Bounding boxes of the heater, plate, tank, and members are pairwise disjoint.

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

def test_step_export_roundtrip_keeps_components_and_names(parts, tmp_path):
    path = tmp_path / "roundtrip.step"
    build_assembly(parts).export(str(path))
    reimported = cq.importers.importStep(str(path))
    assert reimported.solids().size() == len(parts)
    names = set(re.findall(r"PRODUCT\('([^']*)'", path.read_text(encoding="utf-8", errors="replace")))
    missing = {p.id for p in parts} - names
    assert not missing, f"STEP lost component names: {sorted(missing)}"


def test_every_member_role_is_known(parts):
    for p in members(parts):
        assert p.role in MEMBER_ROLES
