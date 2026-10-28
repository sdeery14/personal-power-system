"""Parameters for the PRELIMINARY Diesel Heater Module (002) placeholder model.

PRELIMINARY — NOT FOR FABRICATION.

Every value is in millimetres. Source measurements given in inches are converted
here, once, and nowhere else. Each parameter carries the evidence tag it has in
specs/002-diesel-heater/spec.md. Parameters tagged ``illustrative`` were chosen
only so that a picture can be drawn; the design documents leave them open and
nothing here resolves them.
"""

from dataclasses import dataclass

IN = 25.4  # millimetres per inch; the only conversion factor in the model


@dataclass(frozen=True)
class Param:
    name: str
    value: float
    unit: str
    tag: str  # Owner decision | Manufacturer-stated | User-reported | illustrative
    source: str


# ---------------------------------------------------------------- envelope
ENVELOPE_W = 20 * IN  # X, width
ENVELOPE_D = 24 * IN  # Y, depth
ENVELOPE_H = 38 * IN  # Z, height

# ---------------------------------------------------------------- extrusion
PROFILE_MINOR = 20.0  # T-slot section, short side
PROFILE_MAJOR = 40.0  # T-slot section, long side

# ---------------------------------------------------------------- heater
HEATER_L = 13.4 * IN  # along X in the model
HEATER_W = 4.5 * IN  # along Y
HEATER_H = 5.5 * IN  # along Z
PLATE_X = (5 + 7 / 16) * IN  # plate dimension placed along X
PLATE_Y = (6 + 11 / 16) * IN  # plate dimension placed along Y

# ---------------------------------------------------------------- fuel tank
TANK_Y = 16 * IN  # broad face, along Y (vertical tank against the X-min wall)
TANK_Z = 16 * IN  # broad face, along Z
TANK_X = 3 * IN  # thickness, along X
HOLE_LOWER_SPACING = (6 + 13 / 16) * IN  # between the two lower points, along Y
HOLE_UPPER_RISE = (7 + 7 / 8) * IN  # upper point above the lower row, along Z

# ---------------------------------------------------------------- illustrative
LEVEL_Z = (0.0, 350.0, ENVELOPE_H - PROFILE_MAJOR)  # bottom face of each level's members
PLATE_T = 3.0
CROSSMEMBER_SPACING = 130.0  # centre to centre, along Y
HEATER_CENTER_X = 310.0
HEATER_CENTER_Y = ENVELOPE_D / 2
TANK_BOTTOM_Z = 535.0
TANK_HOLE_ABOVE_BOTTOM = 60.0  # lower hole row above the tank's bottom edge
HOLE_DIA = 8.0
FILLER_D = 40.0
FILLER_H = 20.0

PARAMS = [
    Param("ENVELOPE_W", ENVELOPE_W, "mm", "Owner decision, preliminary", "spec MR-02: 20 in"),
    Param("ENVELOPE_D", ENVELOPE_D, "mm", "Owner decision, preliminary", "spec MR-02: 24 in"),
    Param("ENVELOPE_H", ENVELOPE_H, "mm", "Owner decision, preliminary", "spec MR-02: 38 in"),
    Param("PROFILE_MINOR", PROFILE_MINOR, "mm", "Owner decision", "spec MR-01: 20 x 40 mm T-slot"),
    Param("PROFILE_MAJOR", PROFILE_MAJOR, "mm", "Owner decision", "spec MR-01: 20 x 40 mm T-slot"),
    Param("HEATER_L", HEATER_L, "mm", "Manufacturer-stated", "spec C21: 13.4 in (owner tape agrees, User-reported)"),
    Param("HEATER_W", HEATER_W, "mm", "Manufacturer-stated", "spec C21: 4.5 in"),
    Param("HEATER_H", HEATER_H, "mm", "Manufacturer-stated", "spec C21: 5.5 in"),
    Param("PLATE_X", PLATE_X, "mm", "User-reported", "spec section 5: 5 7/16 in, tape measure"),
    Param("PLATE_Y", PLATE_Y, "mm", "User-reported", "spec section 5: 6 11/16 in, tape measure"),
    Param("TANK_Y", TANK_Y, "mm", "User-reported", "spec section 5: about 16 in, tape measure"),
    Param("TANK_Z", TANK_Z, "mm", "User-reported", "spec section 5: about 16 in, tape measure"),
    Param("TANK_X", TANK_X, "mm", "User-reported", "spec section 5: about 3 in excluding filler neck"),
    Param("HOLE_LOWER_SPACING", HOLE_LOWER_SPACING, "mm", "User-reported", "spec section 5: about 6 13/16 in"),
    Param("HOLE_UPPER_RISE", HOLE_UPPER_RISE, "mm", "User-reported", "spec section 5: about 7 7/8 in"),
    Param("LEVEL_Z[1]", LEVEL_Z[1], "mm", "illustrative", "middle-level height is open (design section 4)"),
    Param("PLATE_T", PLATE_T, "mm", "illustrative", "plate thickness not recorded (Q-03)"),
    Param("CROSSMEMBER_SPACING", CROSSMEMBER_SPACING, "mm", "illustrative", "plate fixing pattern not recorded (Q-03)"),
    Param("HEATER_CENTER_X", HEATER_CENTER_X, "mm", "illustrative", "heater position along the frame is open"),
    Param("TANK_BOTTOM_Z", TANK_BOTTOM_Z, "mm", "illustrative", "tank height is open; SR-01 unreconciled"),
    Param("TANK_HOLE_ABOVE_BOTTOM", TANK_HOLE_ABOVE_BOTTOM, "mm", "illustrative", "hole position on the tank face not recorded"),
    Param("HOLE_DIA", HOLE_DIA, "mm", "illustrative", "boss hole size not recorded (Q-05)"),
    Param("FILLER_D", FILLER_D, "mm", "illustrative", "filler neck size not recorded; orientation cue only"),
    Param("FILLER_H", FILLER_H, "mm", "illustrative", "as above"),
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
