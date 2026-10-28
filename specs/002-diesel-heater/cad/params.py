"""Parameters for the PRELIMINARY Diesel Heater Module (002) placeholder model.

PRELIMINARY — NOT FOR FABRICATION.

Every value is in millimetres. Source measurements given in inches are converted
here, once, and nowhere else. Each parameter carries the evidence tag it has in
specs/002-diesel-heater/spec.md. Parameters tagged ``illustrative`` were chosen
only so that a picture can be drawn; the design documents leave them open and
nothing here resolves them.

Two layout variants exist for comparison in a viewer:

* ``ORIGINAL`` (A Original): the frame concept in design.md, tank above the heater.
* ``COMPACT`` (B1 Compact): an owner-proposed starting point from the 2026-10-28
  brief, tank beside the heater. Its envelope is **not** the MR-02 envelope in
  spec.md and nothing in spec.md or design.md has been changed to match it.

Values shared by both variants (component sizes, hole pattern, profile) are
module constants. Values that differ are fields of ``Variant``.
"""

from dataclasses import dataclass

IN = 25.4  # millimetres per inch; the only conversion factor in the model


@dataclass(frozen=True)
class Param:
    name: str
    value: float
    unit: str
    tag: str  # Owner decision | Manufacturer-stated | User-reported | illustrative | Proposed/illustrative
    source: str


# ---------------------------------------------------------------- extrusion
PROFILE_MINOR = 20.0  # T-slot section, short side
PROFILE_MAJOR = 40.0  # T-slot section, long side

# ---------------------------------------------------------------- heater
HEATER_L = 13.4 * IN  # body length, along the variant's heater axis
HEATER_W = 4.5 * IN  # body width, across the heater axis
HEATER_H = 5.5 * IN  # body height
PLATE_ALONG = (5 + 7 / 16) * IN  # plate dimension placed along the heater axis
PLATE_ACROSS = (6 + 11 / 16) * IN  # plate dimension placed across the heater axis
OUTLET_D = 76.5  # hot-air outlet pipe inner diameter

# ---------------------------------------------------------------- fuel tank
TANK_Y = 16 * IN  # broad face, along Y (upright tank against the X-min wall)
TANK_Z = 16 * IN  # broad face, along Z
TANK_X = 3 * IN  # thickness, along X
HOLE_LOWER_SPACING = (6 + 13 / 16) * IN  # between the two lower points, along Y
HOLE_UPPER_RISE = (7 + 7 / 8) * IN  # upper point above the lower row, along Z

# ------------------------------------------------- illustrative, shared
PLATE_T = 3.0
TANK_HOLE_ABOVE_BOTTOM = 60.0  # lower hole row above the tank's bottom edge
HOLE_DIA = 8.0
FILLER_D = 40.0
FILLER_H = 20.0
FILLER_CORNER_INSET = 50.0  # filler-neck centre from the tank's Y-min top corner
OUTLET_CUE_L = 20.0  # length of the hot-air outlet direction cue


@dataclass(frozen=True)
class Variant:
    """Placement values that differ between the two layouts. All illustrative except where tagged."""

    key: str
    title: str
    envelope_w: float  # X, width
    envelope_d: float  # Y, depth
    envelope_h: float  # Z, height
    level_mid_z: float  # bottom face of the middle-level members and heater crossmembers
    heater_axis: str  # "X" or "Y": direction of the 13.4 in body length
    heater_center_x: float
    heater_center_y: float
    crossmember_spacing: float  # centre to centre, measured along Y (widthwise members)
    tank_bottom_z: float
    outlet_end: str | None  # "+Y" etc.: end of the heater that carries the outlet cue, or None
    layout: str  # "stacked" (tank above heater) or "beside" (separate footprints)
    envelope_tag: str
    envelope_source: str

    @property
    def level_z(self) -> tuple[float, float, float]:
        return (0.0, self.level_mid_z, self.envelope_h - PROFILE_MAJOR)

    def params(self) -> list[Param]:
        return [
            Param("ENVELOPE_W", self.envelope_w, "mm", self.envelope_tag, self.envelope_source),
            Param("ENVELOPE_D", self.envelope_d, "mm", self.envelope_tag, self.envelope_source),
            Param("ENVELOPE_H", self.envelope_h, "mm", self.envelope_tag, self.envelope_source),
            Param("LEVEL_Z[1]", self.level_mid_z, "mm", "illustrative", "middle-level height is open (design section 4)"),
            Param("HEATER_AXIS", 0 if self.heater_axis == "X" else 1, "0=X,1=Y", "illustrative", "heater orientation in the frame is open"),
            Param("HEATER_CENTER_X", self.heater_center_x, "mm", "illustrative", "heater position in the frame is open"),
            Param("HEATER_CENTER_Y", self.heater_center_y, "mm", "illustrative", "heater position in the frame is open"),
            Param("CROSSMEMBER_SPACING", self.crossmember_spacing, "mm", "illustrative", "plate fixing pattern not recorded (Q-03)"),
            Param("TANK_BOTTOM_Z", self.tank_bottom_z, "mm", "illustrative", "tank height is open; SR-01 unreconciled"),
        ]


ORIGINAL = Variant(
    key="original",
    title="A Original",
    envelope_w=20 * IN,
    envelope_d=24 * IN,
    envelope_h=38 * IN,
    level_mid_z=350.0,
    heater_axis="X",
    heater_center_x=310.0,
    heater_center_y=24 * IN / 2,
    crossmember_spacing=130.0,
    tank_bottom_z=535.0,
    outlet_end=None,
    layout="stacked",
    envelope_tag="Owner decision, preliminary",
    envelope_source="spec MR-02: 20 x 24 x 38 in",
)

COMPACT = Variant(
    key="compact",
    title="B1 Compact",
    envelope_w=20 * IN,
    envelope_d=22 * IN,
    envelope_h=28 * IN,
    level_mid_z=7 * IN - PROFILE_MAJOR,  # plate bottom face at about 7 in above ground
    heater_axis="Y",
    heater_center_x=390.0,
    heater_center_y=22 * IN / 2,
    crossmember_spacing=100.0,  # must fit under the 138.1 mm plate dimension along Y
    tank_bottom_z=8 * IN,
    outlet_end="+Y",
    layout="beside",
    envelope_tag="Proposed/illustrative",
    envelope_source="owner brief 2026-10-28 (B1 starting values); not in spec.md, MR-02 unchanged",
)

VARIANTS = {v.key: v for v in (ORIGINAL, COMPACT)}
DEFAULT_VARIANT = ORIGINAL

SHARED_PARAMS = [
    Param("PROFILE_MINOR", PROFILE_MINOR, "mm", "Owner decision", "spec MR-01: 20 x 40 mm T-slot"),
    Param("PROFILE_MAJOR", PROFILE_MAJOR, "mm", "Owner decision", "spec MR-01: 20 x 40 mm T-slot"),
    Param("HEATER_L", HEATER_L, "mm", "Manufacturer-stated", "spec C21: 13.4 in (owner tape agrees, User-reported)"),
    Param("HEATER_W", HEATER_W, "mm", "Manufacturer-stated", "spec C21: 4.5 in"),
    Param("HEATER_H", HEATER_H, "mm", "Manufacturer-stated", "spec C21: 5.5 in"),
    Param("PLATE_ALONG", PLATE_ALONG, "mm", "User-reported", "spec section 5: 5 7/16 in, tape measure; which plate side runs along the heater is not recorded"),
    Param("PLATE_ACROSS", PLATE_ACROSS, "mm", "User-reported", "spec section 5: 6 11/16 in, tape measure; as above"),
    Param("OUTLET_D", OUTLET_D, "mm", "Manufacturer-stated", "spec C23: air outlet pipe inner diameter 3 in / 76.5 mm"),
    Param("TANK_Y", TANK_Y, "mm", "User-reported", "spec section 5: about 16 in, tape measure"),
    Param("TANK_Z", TANK_Z, "mm", "User-reported", "spec section 5: about 16 in, tape measure"),
    Param("TANK_X", TANK_X, "mm", "User-reported", "spec section 5: about 3 in excluding filler neck"),
    Param("HOLE_LOWER_SPACING", HOLE_LOWER_SPACING, "mm", "User-reported", "spec section 5: about 6 13/16 in"),
    Param("HOLE_UPPER_RISE", HOLE_UPPER_RISE, "mm", "User-reported", "spec section 5: about 7 7/8 in"),
    Param("PLATE_T", PLATE_T, "mm", "illustrative", "plate thickness not recorded (Q-03)"),
    Param("TANK_HOLE_ABOVE_BOTTOM", TANK_HOLE_ABOVE_BOTTOM, "mm", "illustrative", "hole position on the tank face not recorded"),
    Param("HOLE_DIA", HOLE_DIA, "mm", "illustrative", "boss hole size not recorded (Q-05)"),
    Param("FILLER_D", FILLER_D, "mm", "illustrative", "filler neck size not recorded; orientation cue only"),
    Param("FILLER_H", FILLER_H, "mm", "illustrative", "as above"),
    Param("FILLER_CORNER_INSET", FILLER_CORNER_INSET, "mm", "illustrative", "filler near a top corner per owner brief 2026-10-28; corner, angle, and size unknown"),
    Param("OUTLET_CUE_L", OUTLET_CUE_L, "mm", "illustrative", "direction cue only; the outlet stub length is not recorded"),
]

JOINT_ASSUMPTION = (
    "Uprights are continuous over the full height; every horizontal member butts "
    "between uprights or between perimeter members, with the 40 mm side vertical. "
    "This is one of several possible joint arrangements (design D-01, D-02 open). "
    "Member lengths derived from it are illustrative, not cut lengths."
)

TANK_WALL_ASSUMPTION = (
    "The tank hangs on the X-min inside wall with the two lower points on the lower "
    "rail and the upper point, centred between them, on the upper rail. Which wall "
    "carries the tank (D-03), the tank's height (SR-01), and the upper point's "
    "horizontal position are all open."
)

LAYOUT_NOTE = {
    "stacked": (
        "Tank drawn entirely above the heater to picture the manufacturer's C12 "
        "instruction. This does not address the keep-away warning (C1); SR-01 is unreconciled."
    ),
    "beside": (
        "Tank drawn beside the heater with separate horizontal footprints, its lower "
        "part overlapping the heater's upper part in height only. Horizontal separation "
        "alone establishes no spill, fire, or thermal clearance; SR-01 and SR-02 remain "
        "open and the modelled gaps are bounding-box distances, not clearances."
    ),
}
