# Measurement record: <group> — <YYYY-MM-DD>

<!-- Copy this file to YYYY-MM-DD-<group>.md. Fill every header line. Leave a reading blank rather than estimate it. Raw readings go in the first table exactly as displayed; anything worked out goes in the second. See README.md §2 to §7. -->

**This record makes the raw readings listed below Measured. It verifies nothing, establishes no clearance, and opens no gate.**

| Field | Entry |
|---|---|
| Record file | `YYYY-MM-DD-<group>.md` |
| Date of session | YYYY-MM-DD |
| Measured by | |
| Component group(s) | PLT / HTR / EXH / TNK / PMP / FLT / FUL / INT / DUC / ELC / MAS / DOC |
| Datum used | HP / TK / loose parts / masses (README §5) |
| Datum marking | Which physical corner or edge carries the `0` or `L` tape, in words; photograph identifier |
| Heater axis mapping (HP only) | `L = X, T = Y` or `L = Y, T = X`, from PLT-14; or "not yet observed" |
| Setup | What the component rested on; level or not; what was fastened or already assembled; anything loosened to measure, or "nothing disassembled" |
| Instruments and resolution | Each instrument with what it displays or its finest marking, for example "digital calipers, 0.01 mm; steel rule, 1 mm; tape, 1/16 in; kitchen scale, 1 g". None is calibrated |
| Photographs | `P-YYYYMMDD-01` to `P-YYYYMMDD-nn`, held by the owner |

## Raw readings

Exactly as the instrument displayed, in its unit, all digits. Repeats in the same cell separated by a slash; both are kept. Letters after the identifier tell apart the several readings of one feature (`HTR-13a`, `HTR-13b`). The Reference column names both surfaces, the axis, and anything that affects the sign (a rule offset, "outward beyond the X = 0 edge", "protrusion below the plate underside"). Provisional ± is your estimate, not the instrument's accuracy.

| ID | Feature and reading | Reading | Unit | Instrument | Resolution | Provisional ± | Reference (from, to, axis, sign) | Photo | Notes |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

## Calculated values

Only values worked out from rows above: centres, widths from differences, lengths from end positions, signed coordinates from an offset or overhang reading, means of repeats, unit conversions. Each row names the raw rows it came from and how.

| ID | Quantity | Value | Unit | From (raw IDs) | How (formula; which repeat or the mean; factor) |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

## Observations

Non-numeric findings, each with the identifier of the feature it concerns: markings, labels, membranes, directions, materials, which end is which, how parts were found assembled.

- `XXX-nn`:

## Not measured

Identifiers in this group that were in scope for the session but not measured, with the reason (inaccessible, no suitable instrument, needs disassembly, session stopped, deferred).

- `XXX-nn`:

## Discrepancies with earlier records

For any identifier above that an earlier record also measured (README §7): the earlier record file; a check that the two readings are comparable (same feature, datum, reference surfaces, component configuration, unit; a converted comparison goes in the calculated-values table, raw rows untouched); then the two values `a` and `b`, their provisional uncertainties `u1` and `u2`, the difference, and the classification: **compatible** when `abs(a − b) <= u1 + u2`, **discrepancy** when `abs(a − b) > u1 + u2`. Compatible means consistent under the provisional uncertainties, not accurate or verified. A discrepancy puts the identifier in dispute; readings that are not comparable need a documented investigation before either is used. A reconciliation note, if this session settles a dispute: which record is selected, why, and what remains uncertain; both records are kept. Write "none; first record for every identifier above" when that is the case.

-

## Questions raised

Anything the session showed that only VEVOR or an engineering review can answer (orientation, angle, bend radius, rating, clearance, hole preparation). Give the existing question number from design.md §15.2 if one covers it; otherwise describe it for the next free Q number. Do not answer it here.

-
