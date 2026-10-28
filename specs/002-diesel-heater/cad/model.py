"""PRELIMINARY parametric placeholder model of the Diesel Heater Module (002).

PRELIMINARY — NOT FOR FABRICATION.

Builds a list of named parts (bounding-box placeholders) and a CadQuery
Assembly from the values in ``params.py``. Coordinate frame: X = width (20 in),
Y = depth (24 in), Z = height (38 in), origin at the outside bottom corner.
"""

from dataclasses import dataclass

import cadquery as cq

import params as P

BANNER = "PRELIMINARY — NOT FOR FABRICATION"


@dataclass(frozen=True)
class Part:
    id: str  # stable identifier, also the STEP component name
    role: str  # upright | perimeter_width | perimeter_depth | heater_crossmember | tank_rail | heater | plate | tank | hole_marker | filler
    axis: str  # X | Y | Z for extrusion members, "-" otherwise
    length: float  # member length along its axis, or 0 for non-members
    illustrative: bool  # True if any placement or size value is an illustrative choice
    note: str
    shape: cq.Shape
    color: tuple


def _box(x0: float, y0: float, z0: float, dx: float, dy: float, dz: float) -> cq.Shape:
    return cq.Workplane("XY").box(dx, dy, dz, centered=False).translate((x0, y0, z0)).val()


def _cyl_x(x0: float, y: float, z: float, d: float, length: float) -> cq.Shape:
    """Cylinder with its axis along +X, starting at x0."""
    return cq.Workplane("YZ").center(y, z).circle(d / 2).extrude(length).translate((x0, 0, 0)).val()


def _cyl_z(x: float, y: float, z0: float, d: float, h: float) -> cq.Shape:
    return cq.Workplane("XY").center(x, y).circle(d / 2).extrude(h).translate((0, 0, z0)).val()


GREY = (0.72, 0.72, 0.74)
BLUE = (0.30, 0.50, 0.85)
GREEN = (0.35, 0.70, 0.40)
ORANGE = (0.95, 0.55, 0.15)
DARK = (0.30, 0.30, 0.32)
WHITE = (0.93, 0.93, 0.88)
RED = (0.90, 0.15, 0.15)


def build_parts() -> list[Part]:
    W, D, H = P.ENVELOPE_W, P.ENVELOPE_D, P.ENVELOPE_H
    a, b = P.PROFILE_MINOR, P.PROFILE_MAJOR  # 20, 40
    parts: list[Part] = []

    # -- four continuous uprights: section a (X) by b (Y), full height -------------
    for i, (x0, y0) in enumerate([(0, 0), (W - a, 0), (0, D - b), (W - a, D - b)], start=1):
        parts.append(Part(f"U{i}", "upright", "Z", H, False,
                          "section orientation illustrative (D-02)", _box(x0, y0, 0, a, b, H), GREY))

    # -- three perimeter levels: two widthwise + two depthwise members each ---------
    len_w = W - 2 * a  # between uprights along X
    len_d = D - 2 * b  # between uprights along Y
    for lvl, z0 in enumerate(P.LEVEL_Z, start=1):
        note = "level height illustrative" if lvl == 2 else "joint assumption; see params"
        for j, y0 in enumerate([0, D - a], start=1):
            parts.append(Part(f"L{lvl}-W{j}", "perimeter_width", "X", len_w, lvl == 2, note,
                              _box(a, y0, z0, len_w, a, b), GREY))
        for j, x0 in enumerate([0, W - a], start=1):
            parts.append(Part(f"L{lvl}-D{j}", "perimeter_depth", "Y", len_d, lvl == 2, note,
                              _box(x0, b, z0, a, len_d, b), GREY))

    # -- two heater crossmembers at the middle level ---------------------------------
    z2 = P.LEVEL_Z[1]
    for j, yc in enumerate([P.HEATER_CENTER_Y - P.CROSSMEMBER_SPACING / 2,
                            P.HEATER_CENTER_Y + P.CROSSMEMBER_SPACING / 2], start=1):
        parts.append(Part(f"HX{j}", "heater_crossmember", "X", len_w, True,
                          "spacing illustrative (plate fixing pattern, Q-03)",
                          _box(a, yc - a / 2, z2, len_w, a, b), BLUE))

    # -- heater plate and heater body (bounding boxes) -------------------------------
    plate_z0 = z2 + b
    px0 = P.HEATER_CENTER_X - P.PLATE_X / 2
    py0 = P.HEATER_CENTER_Y - P.PLATE_Y / 2
    parts.append(Part("heater_plate", "plate", "-", 0, True,
                      "owner tape dimensions; thickness and position illustrative",
                      _box(px0, py0, plate_z0, P.PLATE_X, P.PLATE_Y, P.PLATE_T), DARK))
    hx0 = P.HEATER_CENTER_X - P.HEATER_L / 2
    hy0 = P.HEATER_CENTER_Y - P.HEATER_W / 2
    parts.append(Part("heater_body", "heater", "-", 0, True,
                      "manufacturer size as a bounding box; orientation and position illustrative",
                      _box(hx0, hy0, plate_z0 + P.PLATE_T, P.HEATER_L, P.HEATER_W, P.HEATER_H), ORANGE))

    # -- tank rails on the X-min inside wall, and the tank hanging on them -----------
    tank_x0 = a + a  # inside the perimeter depth member (0..a) and the rail (a..2a)
    tank_y0 = (D - P.TANK_Y) / 2
    hole_z_lower = P.TANK_BOTTOM_Z + P.TANK_HOLE_ABOVE_BOTTOM
    hole_z_upper = hole_z_lower + P.HOLE_UPPER_RISE
    yc = D / 2
    for name, zc in [("TR-lower", hole_z_lower), ("TR-upper", hole_z_upper)]:
        parts.append(Part(name, "tank_rail", "Y", len_d, True,
                          "height follows the illustrative tank position (SR-01 open)",
                          _box(a, b, zc - b / 2, a, len_d, b), GREEN))
    parts.append(Part("fuel_tank", "tank", "-", 0, True,
                      "owner tape dimensions as a bounding box; wall and height illustrative",
                      _box(tank_x0, tank_y0, P.TANK_BOTTOM_Z, P.TANK_X, P.TANK_Y, P.TANK_Z), WHITE))
    parts.append(Part("tank_filler_neck", "filler", "-", 0, True,
                      "orientation cue only; size not recorded",
                      _cyl_z(tank_x0 + P.TANK_X / 2, yc, P.TANK_BOTTOM_Z + P.TANK_Z, P.FILLER_D, P.FILLER_H), WHITE))

    # -- three mounting-point markers through rail and tank (not fasteners) ----------
    marker_len = (tank_x0 + P.TANK_X) - a
    for name, y, z in [("tank_hole_lower_a", yc - P.HOLE_LOWER_SPACING / 2, hole_z_lower),
                       ("tank_hole_lower_b", yc + P.HOLE_LOWER_SPACING / 2, hole_z_lower),
                       ("tank_hole_upper", yc, hole_z_upper)]:
        parts.append(Part(name, "hole_marker", "X", marker_len, True,
                          "marker at the reported spacing; not a fastener or boss (MR-04 open)",
                          _cyl_x(a, y, z, P.HOLE_DIA, marker_len), RED))

    ids = [p.id for p in parts]
    assert len(ids) == len(set(ids)), "part identifiers must be unique"
    return parts


def build_assembly(parts: list[Part] | None = None) -> cq.Assembly:
    parts = parts or build_parts()
    assy = cq.Assembly(name="diesel_heater_module_PRELIMINARY")
    for p in parts:
        assy.add(p.shape, name=p.id, color=cq.Color(*p.color))
    return assy


MEMBER_ROLES = ("upright", "perimeter_width", "perimeter_depth", "heater_crossmember", "tank_rail")


def members(parts: list[Part]) -> list[Part]:
    return [p for p in parts if p.role in MEMBER_ROLES]
