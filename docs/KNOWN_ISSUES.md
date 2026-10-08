# Known issues and evidence

[Back to README](../README.md)

This is a review of the supplied implementation, not a claim that all issues have been fixed. No live hardware test or full model retraining was performed during packaging.

## P0 — Packet decoding

The `0x83` ThinkGear field contains a length byte (`24`) followed by eight unsigned, big-endian, three-byte relative power values. The parser uses offsets without first consuming the length byte.

A fixture containing attention 60 and bands `[101, 202, 303, 404, 505, 606, 707, 808]` should yield:

```text
(attention, high_alpha, high_beta, mid_gamma)
(60, 404, 606, 808)
```

The supplied function returns:

```text
(60, 3080193, 16318466, 12779523)
```

Run `python tools/audit_parser.py` from the repository root to reproduce the issue without opening a serial port. The expected current result is exit code 1. This is a known-defect check, not a passing acceptance test.

Unknown fields are also not skipped using the general protocol length rules. Fixing one offset alone is insufficient for a robust parser. Verify scalar fields, extended fields, field lengths, malformed payloads, and packets captured from the actual device.

Reference: [ThinkGear communications protocol](https://developer.neurosky.com/docs/doku.php?id=thinkgear_communications_protocol).

## P0 — AI evaluation validity

The notebook normalizes before splitting, retains eleven unfilled sequence slots, permits participant overlap, and evaluates on the same portion used for validation. Its LSTM outer time dimension is one. Read [AI and data](AI_AND_DATA.md) before reporting the saved accuracy outputs.

## P1 — Acquisition and storage reliability

| Issue | Consequence | Proposed action |
|---|---|---|
| No serial timeout/recovery strategy | Reader can block or stop after device failure | Bounded reads, explicit state, reconnect workflow |
| No general partial-read validation | Truncated input can fail assumptions | Accumulate bytes and validate complete packets |
| No signal-quality gating | Poor contact can be mistaken for meaningful readings | Decode and surface device quality information |
| Attention and high-alpha required together | Values can be skipped depending on packet composition | Retain validated field state with timestamps |
| Shared mutable histories | Acquisition/display state can be inconsistent | Queue-based delivery and clear state ownership |
| Saves only every ten samples | Last unsaved readings may be lost | Periodic/final flush and graceful shutdown |
| Reused CSV filename | Prior session can be overwritten | Unique session files and append-safe handling |
| Only time and attention saved | Band plots cannot be reconstructed from this CSV | Record validated features and quality |
| Averages exist only in memory | Historical averages disappear on restart | Persist and reload session summaries |

## P1 — Signal interpretation and data provenance

- Device band-power values are relative power, not physical voltage amplitudes or automatically measured frequency values. Correct interface labeling.
- Attention category labels are arbitrary thresholds, not validated classroom performance categories.
- MATLAB scripts assume 256 Hz without establishing that rate from the input data.
- Numeric CSV columns are treated as EEGLAB channels without verifying channel meaning.
- The local concentration dataset lacks a fully established collection/transformation chain.

## P2 — Missing reproducibility assets

Exact hardware identifiers and wiring, a verified dependency lockfile, editable Power BI source, reproducible local labeling records, a deployable model/preprocessing artifact, and a full classroom evaluation protocol are not present in the supplied package.

## Scope of packaging changes

The Python CSV destination/name was made portable, and a historical-status comment was added. The notebook received a warning cell and local dataset/setup paths. Model logic, parser behavior, and saved analytical outputs were retained. MATLAB scripts and STL/image files were copied as supplied. [Hashes and file-level changes](ASSET_PROVENANCE.json) record provenance.

This preserves a traceable baseline for subsequent corrections. Documentation does not imply that those corrections have already been implemented.
