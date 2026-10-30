# Diesel Heater Module (002) — Physical evidence archive (curated photographs and prior reports)

**Status:** photographs and prior reports recovered on 2026-10-29 from the owner's earlier ChatGPT conversations and committed for shared review; manufacturer-document provenance added 2026-10-30. **Not a measurement record, a verification, a fit check, a structural acceptance, or an operating authorization.** The heater equipment is owned; no frame is purchased or built; G1–G5 in [spec.md §10](../spec.md#10-release-gates) stay closed.

| File | Role |
|---|---|
| [`photo-index.md`](photo-index.md) | E-01 to E-10: provenance (original filename and owner-asserted hash), committed-derivative hash and size, what each image visibly shows, what it cannot settle, and the measurement identifiers it relates to |
| [`prior-reports.md`](prior-reports.md) | The owner's earlier dimensions and observations with their evidence tags and dates, the open identifier for each, and the discrepancies between the package as received and the repository record |
| [`photos/`](photos/) | The ten curated JPEG derivatives, named as in the index |
| [`manufacturer-documents.md`](manufacturer-documents.md) | Provenance of the VEVOR documents M1, M2, and M3 (file name, size, SHA-256, PDF dates; M3 not committed), the page-specific findings of the 2026-10-30 reading of M3, the M1-versus-M3 comparison, and what M3 does not state |

## What the photographs are

The images in `photos/` are **cropped derivatives** of photographs the owner uploaded in October 2026 (upload dates are not capture dates). Cropping removed unrelated surroundings; re-encoding left each file with only a JFIF header. Each file was inspected on 2026-10-29 before commit for EXIF, XMP, ICC, and comment segments (none present) and for household or personal detail (none after cropping; see `photo-index.md §1`). The originals remain in the owner's private archive and are not committed; the index carries their filenames and owner-asserted hashes so the owner can match a derivative to its original. These are photographs of the owned parts, not CAD output or generated images.

## How to read them

- **Visually observed** is the only tag a photograph can supply: the visible arrangement of the owned parts in one image. A photograph does not establish installation, fastening, a dimension, a clearance, a load rating, a hole state, or a safe condition. Where an image cannot settle something, the index says so and names the identifier that can.
- **User-reported** figures (the owner's earlier tape readings and estimates) are in `prior-reports.md`, not in the image descriptions. A tape visible in a photograph is not a reading; no value is read off any image here.
- **Measured** is reserved for a dated record under [`../measurements/`](../measurements/README.md) with the instrument, datum, and provisional uncertainty recorded. No prior figure is promoted by this archive.
- **Verified** requires separately documented independent confirmation; nothing here is Verified.

Two things the set does make visible: the four nutted studs around the heater's stubs are distinct from the plate's four corner holes (E-01, E-02), and the shorter plate side runs along the heater's length (E-03, E-04). Both support the way [design.md §5](../design.md#5-heater-mounting) already separates Interface A from Interface B, and neither establishes a load path, a clearance to the crossmembers, or the PLT-14 record. The tank photographs show one face only; the state of the three recess centres is **unresolved** and the two close-ups differ in appearance.

## Process

New physical observations go through the measurement workflow, not this archive: a dated record under `../measurements/` may cite an E-nn image for what it refers to. A further curated photograph may be added here with a new E-nn row, the same provenance columns, the same metadata check, and no original. Nothing in this directory opens G1 purchase readiness, G2 fabrication, G3 electrical, G4 transport, or G5 operation.

**Public-repository note.** The repository is public. Derivatives are committed only after the metadata and content check above; originals never are. If the owner wants any committed image removed or re-cropped, say so in review; the hashes in the index make a replacement traceable.
