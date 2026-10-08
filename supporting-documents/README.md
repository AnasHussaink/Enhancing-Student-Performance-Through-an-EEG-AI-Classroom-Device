# Original project documents

[Project README](../README.md) · [Visual gallery](../docs/GALLERY.md)

These files are complete copies of the supplied originals, renamed for clear repository links. The documents were not rewritten, regenerated, or corrected. They preserve proposals, implementation history, report figures, and claims made at that time.

## Downloads and original filenames

| Packaged file | Original source | Size / extent |
|---|---|---|
| [Project-Presentation.pptx](Project-Presentation.pptx) | `fyp/new working.pptx` | 38 slides; about 16.7 MiB |
| [Project-Presentation-Archive.pdf](Project-Presentation-Archive.pdf) | `fyp/EEG AI Based.pdf` | 61 pages |
| [Results-and-Discussion-Slides.pdf](Results-and-Discussion-Slides.pdf) | `fyp/Results And Disucssion.pdf` | 45 pages |
| [Final-Year-Project-Report.docx](Final-Year-Project-Report.docx) | `fyp/report.docx` | Complete original report; about 69.4 MiB |
| [Research-Manuscript-Draft.pdf](Research-Manuscript-Draft.pdf) | `Mind Track Reasearch paper/Reasearch paper till system model.pdf` | 9 pages; draft |
| [Results-Discussion-Writeup.pdf](Results-Discussion-Writeup.pdf) | `Mind Track Reasearch paper/Result And Disscussion.pdf` | 6 pages |

The 61-page PDF and the 38-slide PPTX are different source documents. The PDF is not represented as a matching export of that PowerPoint.

## Suggested reading order

1. Start with the repository README for the reviewed system architecture and current implementation status.
2. Open the results slides for the physical headband, interface, plots, and reporting screenshots.
3. Open the PowerPoint for the project's presentation narrative and development explorations.
4. Use the full report for methodology and appendices.
5. Consult the manuscript and discussion documents as supplementary drafts.

## How to interpret the originals

- Hardware such as STM32/ESP8266 and cloud/mobile capabilities appears in proposal material, but matching final implementation files were not established.
- MATLAB/EEGLAB screenshots include exploratory and tutorial work. They do not prove that a complete custom raw-signal processing pipeline was implemented in the supplied scripts.
- The slide-36 PowerPoint confusion matrix shows 17 correct entries out of 20. The supplied notebook's saved matrix shows 15/20. These are different historical results; the missing run history prevents treating them as one verified metric.
- The GUI capture documents its layout with empty plots. Separate monitoring figures may come from other prototype versions; no new hardware run was performed to produce these images.
- Power BI screenshots are included, but the editable `.pbix` file and a complete reproducible reporting pipeline were not supplied.
- Original documents/screenshots include names, roll numbers, and photographs. They are retained unchanged; confirm the intended public release of those details before publishing.

See [AI and data](../docs/AI_AND_DATA.md) and [known issues](../docs/KNOWN_ISSUES.md) for the reviewed technical interpretation.

## Uploading the complete collection

The full report exceeds GitHub's browser upload limit of 25 MiB per file. Use GitHub Desktop or command-line Git for the complete repository; the packaged files remain below 100 MiB each. [GitHub file-upload documentation](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

No third-party EEGLAB distribution, research-paper collection, or downloadable public CSV is included. Near-duplicate report versions and the separate large early proposal deck remain in the original local project folder rather than duplicating them here.
