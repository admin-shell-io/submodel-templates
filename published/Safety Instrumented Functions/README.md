# Safety Instrumented Functions

This directory holds four Submodel template specifications published together
for functional safety in the process industries, based on IEC 61511.

| Part | Submodel | Document | Folder |
|------|----------|----------|--------|
| 1 | Safety Instrumented Function | IDTA 02064 | [Part 1 Safety Instrumented Function](Part%201%20Safety%20Instrumented%20Function/1/0/) |
| 2 | Safety Instrumented System | IDTA 02097 | [Part 2 Safety Instrumented System](Part%202%20Safety%20Instrumented%20System/1/0/) |
| 3 | Safety Instrumented System Device | IDTA 02079 | [Part 3 Safety Instrumented System Device](Part%203%20Safety%20Instrumented%20System%20Device/1/0/) |
| 4 | Equipment Under Control | IDTA 02096 | [Part 4 Equipment Under Control](Part%204%20Equipment%20Under%20Control/1/0/) |

## How the four parts relate

Equipment Under Control defines the hazard and the SIL allocation. The Safety
Instrumented Function specifies the function that reduces that risk. The Safety
Instrumented System is the system realising the function, and Safety Instrumented
System Device carries the reliability data for each sensor, logic solver and
final element that makes it up. `SRSRequirements` appears in all four as the
shared link to the safety requirements specification.

## Artifacts

Each part provides, for version 1.0:

- `IDTA xxxxx_Submodel_<Name>.pdf` — the specification
- `IDTA xxxxx_Template_<Name>.aasx` — the submodel template (AAS metamodel V3.0)
- `IDTA xxxxx_Template_<Name>.json` — the same template as JSON
- `IDTA xxxxx_Example_<Name>.aasx` — a filled example instance
- `IDTA xxxxx_Example_<Name>.json` — the same example as JSON

The JSON artifacts are generated from the AASX packages and match them exactly.
