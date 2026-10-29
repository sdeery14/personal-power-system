"""PRELIMINARY parametric placeholder model of the Diesel Heater Module (002).

PRELIMINARY — NOT FOR FABRICATION.

Builds a list of named parts (bounding-box placeholders) and a CadQuery
Assembly from the values in ``params.py`` for one layout variant
(``params.ORIGINAL``, ``params.COMPACT``, or ``params.ADJUSTED``). Coordinate
frame: X = width, Y = depth, Z = height, origin at the outside bottom corner.
The tank wall is the X-min wall in every variant.
"""

from dataclasses import dataclass

import cadquery as cq

import params as P

BANNER = "PRELIMINARY — NOT FOR FABRICATION"


@dataclass(frozen=True)
class Part:
    id: str  # stable identifier, also the STEP component name
    role: str  # upright | perimeter_width | perimeter_depth | heater_crossmember | tank_rail | heater | plate | tank | hole_marker | filler | outlet_cue
    axis: str  # X | Y | Z for extrusion members, "-" otherwise
    length: float  # member length along its axis, or 0 for non-members
    basis: str  # what the size and placement depend on: evidence-tagged values, illustrative parameters, assumptions
    note: str
    shape: cq.Shape
    color: tuple


def _box(x0: float, y0: float, z0: float, dx: float, dy: float, dz: float) -> cq.Shape:
    return cq.Workplane("XY").box(dx, dy, dz, centered=False).translate((x0, y0, z0)).val()


def _cyl(start: tuple, direction: tuple, d: float, length: float) -> cq.Shape:
    """Cylinder of diameter ``d`` from ``start`` along the unit ``direction``."""
    return cq.Solid.makeCylinder(d / 2, length, cq.Vector(*start), cq.Vector(*direction))


GREY = (0.72, 0.72, 0.74)
BLUE = (0.30, 0.50, 0.85)
GREEN = (0.35, 0.70, 0.40)
ORANGE = (0.95, 0.55, 0.15)
DARK = (0.30, 0.30, 0.32)
WHITE = (0.93, 0.93, 0.88)
RED = (0.90, 0.15, 0.15)
YELLOW = (0.95, 0.85, 0.20)

_AXIS = {"X": (1, 0, 0), "Y": (0, 1, 0), "Z": (0, 0, 1)}


def build_parts(variant: P.Variant = P.DEFAULT_VARIANT) -> list[Part]:
    v = variant
    W, D, H = v.envelope_w, v.envelope_d, v.envelope_h
    a, b = P.PROFILE_MINOR, P.PROFILE_MAJOR  # 20, 20 (2020 square section, Owner decision 2026-10-29)
    parts: list[Part] = []

    # -- four continuous uprights: section a (X) by b (Y), full height -------------
    for i, (x0, y0) in enumerate([(0, 0), (W - a, 0), (0, D - b), (W - a, D - b)], start=1):
        parts.append(Part(f"U{i}", "upright", "Z", H, f"envelope height ({v.envelope_tag}); joint assumption",
                          "2020 square section; no orientation choice (D-02 closed 2026-10-29)", _box(x0, y0, 0, a, b, H), GREY))

    # -- three perimeter levels: two widthwise + two depthwise members each ---------
    len_w = W - 2 * a  # between uprights along X
    len_d = D - 2 * b  # between uprights along Y
    for lvl, z0 in enumerate(v.level_z, start=1):
        note = "level height illustrative" if lvl == 2 else "level at the envelope top or bottom"
        basis = f"envelope ({v.envelope_tag}); joint assumption" + ("; illustrative middle-level height" if lvl == 2 else "")
        for j, y0 in enumerate([0, D - a], start=1):
            parts.append(Part(f"L{lvl}-W{j}", "perimeter_width", "X", len_w, basis, note,
                              _box(a, y0, z0, len_w, a, b), GREY))
        for j, x0 in enumerate([0, W - a], start=1):
            parts.append(Part(f"L{lvl}-D{j}", "perimeter_depth", "Y", len_d, basis, note,
                              _box(x0, b, z0, a, len_d, b), GREY))

    # -- two widthwise heater crossmembers at the middle level, spaced along Y -----
    z2 = v.level_mid_z
    if v.plate_holes:
        cross_note = ("spacing derived from the owner-reported plate hole pitch (not measured, PLT-06 to PLT-09); "
                      f"slot line under each hole line, so the member overhangs the plate edge by {P.PROFILE_MINOR / 2 - P.PLATE_HOLE_INSET:.1f} mm")
    else:
        cross_note = "spacing illustrative (plate fixing pattern not used, Q-03)"
    if v.layout != "stacked":
        cross_note += "; spans the full width and passes beneath the tank zone"
    for j, yc in enumerate([v.heater_center_y - v.crossmember_spacing / 2,
                            v.heater_center_y + v.crossmember_spacing / 2], start=1):
        parts.append(Part(f"HX{j}", "heater_crossmember", "X", len_w,
                          "envelope width; joint assumption; illustrative middle-level height, heater position, and spacing", cross_note,
                          _box(a, yc - a / 2, z2, len_w, a, b), BLUE))

    # -- heater plate and heater body (bounding boxes), oriented by heater_axis ------
    if v.heater_axis == "X":
        plate_dx, plate_dy = P.PLATE_ALONG, P.PLATE_ACROSS
        heat_dx, heat_dy = P.HEATER_L, P.HEATER_W
    else:
        plate_dx, plate_dy = P.PLATE_ACROSS, P.PLATE_ALONG
        heat_dx, heat_dy = P.HEATER_W, P.HEATER_L
    plate_z0 = z2 + b
    plate_x0, plate_y0 = v.heater_center_x - plate_dx / 2, v.heater_center_y - plate_dy / 2
    parts.append(Part("heater_plate", "plate", "-", 0, "User-reported size and thickness estimate; illustrative orientation and position",
                      "owner tape dimensions; thickness an owner estimate (about 1/32 in, not measured); position and which side runs along the heater illustrative",
                      _box(plate_x0, plate_y0, plate_z0, plate_dx, plate_dy, P.PLATE_T), DARK))
    heater_z0 = plate_z0 + P.PLATE_T
    heater_note = f"manufacturer size as a bounding box; body length along {v.heater_axis}; orientation and position illustrative"
    if v.layout != "stacked":
        heater_note += "; heating-air inlet assumed at the end opposite the outlet cue, facing open space (SR-07)"

    # -- four plate fixing-hole markers at the reported inset from the plate edges ----
    # -- (adjusted variant): markers through the plate and the crossmember top, not fasteners
    if v.plate_holes:
        inset, mark_len = P.PLATE_HOLE_INSET, 10.0 + P.PLATE_T + 10.0
        corners = [(plate_x0 + inset, plate_y0 + inset), (plate_x0 + plate_dx - inset, plate_y0 + inset),
                   (plate_x0 + plate_dx - inset, plate_y0 + plate_dy - inset), (plate_x0 + inset, plate_y0 + plate_dy - inset)]
        for j, (hx, hy) in enumerate(corners, start=1):
            parts.append(Part(f"plate_hole_{j}", "hole_marker", "Z", mark_len,
                              "User-reported hole diameter and edge clearance (not measured); plate orientation illustrative",
                              "marker at the reported position; not a fastener; whether the heater's own fixings pass through it is open (D-16)",
                              _cyl((hx, hy, plate_z0 - 10.0), (0, 0, 1), P.PLATE_HOLE_D, mark_len), RED))
    parts.append(Part("heater_body", "heater", "-", 0, "Manufacturer-stated size; illustrative orientation and position", heater_note,
                      _box(v.heater_center_x - heat_dx / 2, v.heater_center_y - heat_dy / 2, heater_z0,
                           heat_dx, heat_dy, P.HEATER_H), ORANGE))

    # -- hot-air outlet direction cue at one end of the heater (not a duct) ----------
    if v.outlet_end:
        sign, ax = (1 if v.outlet_end[0] == "+" else -1), v.outlet_end[1]
        direction = tuple(sign * c for c in _AXIS[ax])
        half = (heat_dx if ax == "X" else heat_dy) / 2
        start = [v.heater_center_x, v.heater_center_y, heater_z0 + P.HEATER_H / 2]
        start["XY".index(ax)] += sign * half
        parts.append(Part("heater_outlet_cue", "outlet_cue", ax, P.OUTLET_CUE_L, "Manufacturer-stated diameter; illustrative end and length",
                          f"direction cue at the {v.outlet_end} end; outlet inner diameter C23; which end faces the duct is open (D-03, D-08)",
                          _cyl(tuple(start), direction, P.OUTLET_D, P.OUTLET_CUE_L), YELLOW))

    # -- tank rails in the plane of the X-min perimeter members, butting between the --
    # -- uprights like the depth members; the tank hangs on their inside face ----------
    tank_x0 = a  # inside face of the rails and of the X-min members (0..a)
    tank_y0 = (D - P.TANK_Y) / 2
    hole_z_lower = v.tank_bottom_z + P.TANK_HOLE_ABOVE_BOTTOM
    hole_z_upper = hole_z_lower + P.HOLE_UPPER_RISE
    yc = D / 2
    for name, zc in [("TR-lower", hole_z_lower), ("TR-upper", hole_z_upper)]:
        parts.append(Part(name, "tank_rail", "Y", len_d,
                          "envelope depth; joint assumption; illustrative tank height and hole position",
                          "height follows the illustrative tank position (SR-01 open); butts between the uprights",
                          _box(0, b, zc - b / 2, a, len_d, b), GREEN))
    parts.append(Part("fuel_tank", "tank", "-", 0, "User-reported size; illustrative wall and height",
                      "owner tape dimensions as a bounding box; wall and height illustrative; " + P.LAYOUT_NOTE[v.layout],
                      _box(tank_x0, tank_y0, v.tank_bottom_z, P.TANK_X, P.TANK_Y, P.TANK_Z), WHITE))
    parts.append(Part("tank_filler_neck", "filler", "-", 0, "illustrative size and corner",
                      "orientation cue near the Y-min top corner; corner, angle, and size not recorded",
                      _cyl((tank_x0 + P.TANK_X / 2, tank_y0 + P.FILLER_CORNER_INSET, v.tank_bottom_z + P.TANK_Z),
                           (0, 0, 1), P.FILLER_D, P.FILLER_H), WHITE))

    # -- three mounting-point markers through rail and tank (not fasteners) ----------
    marker_len = tank_x0 + P.TANK_X  # from the rail outside face (x = 0) to the tank far face
    for name, y, z in [("tank_hole_lower_a", yc - P.HOLE_LOWER_SPACING / 2, hole_z_lower),
                       ("tank_hole_lower_b", yc + P.HOLE_LOWER_SPACING / 2, hole_z_lower),
                       ("tank_hole_upper", yc, hole_z_upper)]:
        parts.append(Part(name, "hole_marker", "X", marker_len, "User-reported spacing; illustrative diameter and position on the tank face",
                          "marker at the reported spacing; not a fastener or boss (MR-04 open)",
                          _cyl((0, y, z), (1, 0, 0), P.HOLE_DIA, marker_len), RED))

    ids = [p.id for p in parts]
    assert len(ids) == len(set(ids)), "part identifiers must be unique"
    return parts


def build_assembly(parts: list[Part] | None = None, variant: P.Variant = P.DEFAULT_VARIANT) -> cq.Assembly:
    parts = parts or build_parts(variant)
    assy = cq.Assembly(name=f"diesel_heater_module_{variant.key}_PRELIMINARY")
    for p in parts:
        assy.add(p.shape, name=p.id, color=cq.Color(*p.color))
    return assy


MEMBER_ROLES = ("upright", "perimeter_width", "perimeter_depth", "heater_crossmember", "tank_rail")
PLACEHOLDER_ROLES = ("heater", "plate", "tank", "filler", "hole_marker", "outlet_cue")


def members(parts: list[Part]) -> list[Part]:
    return [p for p in parts if p.role in MEMBER_ROLES]


def by_id(parts: list[Part], pid: str) -> Part:
    return next(p for p in parts if p.id == pid)
