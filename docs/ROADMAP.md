# Roadmap and completion criteria

[Back to README](../README.md)

The tasks below are recommended future work. No item is labeled actively in progress because the reviewed files do not establish current development activity.

## Existing baseline

- Physical wearable and enclosure development supported by photographs/design assets.
- Python serial dashboard and attention logging source available.
- MATLAB and EEGLAB exploration scripts available.
- Offline public-data AI notebook with historical outputs available.
- Reports and presentation material reviewed; implementation gaps documented.

## Priority 0: establish trustworthy outputs

| Task | Completion evidence |
|---|---|
| Correct the complete payload parser | Known scalar/power fixtures decode exactly; unknown/extended fields and malformed packets are handled; actual device packets agree |
| Establish signal-quality handling | Poor contact and invalid readings are clearly marked and excluded by documented rules |
| Trace each dataset | Source, license/consent, schema, units, transformations, and label meaning recorded |
| Rebuild notebook sequence construction | Only genuine populated groups included; shapes and counts checked; recurrent sequence axis matches the intended design |
| Redesign ML evaluation | Participant-disjoint partitions, training-only fitted preprocessing, simple baselines, untouched final test, and recorded metrics |

## Priority 1: make the prototype repeatable

| Task | Completion evidence |
|---|---|
| Handle serial failures | Demonstrated disconnect/reconnect, partial packet handling, timeout, and clean application close |
| Preserve sessions | Unique files, final flush, quality/features/timestamps logged, reloadable summaries, and no silent overwrites |
| Document the final hardware | Part-numbered BOM, verified wiring, power measurements, enclosure scale, and assembly photos |
| Verify the software environment | Clean setup tested on a documented machine, dependencies captured, and replay demonstration included |
| Correct plot/metric wording | Units and feature meanings match the actual protocol; device scores distinguished from model outputs |

## Priority 2: add validated AI integration

1. Export the fitted preprocessing together with the selected model and schema/version metadata.
2. Demonstrate that the live device can produce the same features, units, and windowing expected by the model.
3. Run inference on saved replay sessions before connecting it to the GUI.
4. Show device attention and model predictions as separate values with clear meaning.
5. Measure inference latency, missing-data behavior, and performance on new participants/local data.

**Acceptance:** the dashboard loads a versioned artifact and reproduces offline predictions on identical input windows. Separately report whether predictive performance transfers to new students and the live hardware.

## Priority 3: evaluate classroom value

Develop a study that measures usability, comfort, useful recording time, interpretation by educators, and appropriate learning outcomes. Plan participant consent and data access, and avoid using an unvalidated attention proxy as an automated judgment of student ability.

**Acceptance:** documented protocol, traceable data and analysis, comparison conditions, uncertainty, and conclusions supported by the measured outcomes. A rising attention score alone does not prove better academic performance.

## Optional extensions after the baseline is reliable

- Multiple synchronized devices and a teacher-facing overview.
- A persistent local session database and export tools.
- A web/mobile view or managed remote storage where there is an actual use case.
- Improved mechanical comfort and repeatable electrode contact.
- Additional signal features and artifact handling appropriate to the available acquisition channels.

These are extensions, not prerequisites for demonstrating the core engineering work. Choose them based on a specific problem and evaluation plan.

## Suggested future releases

| Suggested milestone | Meaning |
|---|---|
| Documentation baseline | Original work organized with limitations and provenance |
| Reliable acquisition | Correct parser, quality-aware display, resilient logging, verified build instructions |
| Reproducible offline AI | Valid splits, baselines, saved artifacts, and repeatable evaluation |
| Validated integrated prototype | Live inference compatible with the hardware and tested on representative sessions |

These are proposed milestones; no GitHub releases or tags are asserted to exist.
