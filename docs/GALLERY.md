# Project visual gallery

[Project README](../README.md) · [Original documents](../supporting-documents/README.md)

These 35 figures were extracted from your original presentation, results PDF, and saved notebook outputs. They retain the original pixels, labels, and values. No graph was regenerated or model retrained for this gallery. Source references identify the PowerPoint slide, PDF page, or original notebook cell (zero-based).

## Hardware and electronics

### Assembled headband

![Assembled headband beside a laptop](images/results/assembled-headband.jpg)

**Source:** Results and Discussion slides, page 8. Photograph of the assembled wearable.

### Printed enclosure

![Printed enclosure mounted on the headband](images/results/printed-enclosure.jpg)

**Source:** Results slides, page 8. Physical printed housing and headband. Exact print settings and materials remain undocumented.

### Breadboard exploration

![Breadboard circuit shown in the original presentation](images/presentation/breadboard-exploration.jpeg)

**Source:** Project PowerPoint, slide 14. Preserved as a development/exploration image. The source does not establish that this circuit became the final TGAM-based acquisition hardware or verify ownership of every source illustration.

### Instrumentation amplifier simulation

![Instrumentation amplifier circuit from the PowerPoint](images/presentation/amplifier-simulation.png)

![Oscilloscope response beside the amplifier circuit in the PowerPoint](images/presentation/amplifier-response.png)

**Source:** PowerPoint, slide 11. Circuit and simulated response shown in the presentation. These are not a verified final wearable wiring diagram or a measured transfer-function report.

### Filter circuit explorations

![High-pass filter circuit](images/presentation/high-pass-circuit.png)

![Low-pass filter circuit](images/presentation/low-pass-circuit.png)

**Source:** PowerPoint, slides 12 and 13. Historical circuit-study images. Their component values and captions were not independently validated; use the manufacturer's acquisition guidance for any real build.

## Acquisition and Python GUI

### Serial output

![Serial byte output screenshot](images/presentation/serial-output.png)

**Source:** PowerPoint, slide 15. Early serial inspection output. Displaying received bytes is a development step; it does not establish correct decoding of every EEG field.

### Spreadsheet view

![Spreadsheet containing time, frequency-related fields and attention values](images/presentation/spreadsheet-data.png)

**Source:** PowerPoint, slide 16. The displayed six-column structure differs from the packaged application's two-column attention CSV. The generating/transformation pipeline is not established; see [data provenance](../data/README.md).

### Python interface

![Original Python EEG dashboard](images/results/python-gui.png)

**Source:** Results slides, page 36. Student information, photograph, attention gauge, and plotting areas. This capture has empty plots and zero values; it illustrates the GUI layout rather than proving an active acquisition session. Original identifying details remain in the screenshot.

### EEG monitoring figure

![Historical attention and band monitoring figure](images/results/eeg-monitoring-plots.png)

**Source:** Results slides, page 34. Attention and paired band traces from the historical results. This figure includes more bands than the selected-band display in the supplied Python script. Its exact generating code/run is unconfirmed. Existing band-power decoding issues prevent interpreting large plotted values as independently verified physiological measurements.

## MATLAB and EEGLAB exploration

### Series plot

![Original MATLAB series plot](images/presentation/matlab-series.png)

**Source:** PowerPoint, slide 20. Historical plot of the series used in that analysis. The original label and time axis are retained; the example 256 Hz assumption is not proof of the input's actual sampling rate.

### Three-panel feature plot

![Original MATLAB band-feature plots](images/presentation/matlab-band-plots.png)

**Source:** PowerPoint, slide 21. Feature plots presented during MATLAB exploration. The supplied `eegcode.m` selects/averages existing columns; it does not establish FFT/wavelet extraction from a continuous raw recording.

### EEGLAB spectrum

![EEGLAB spectrum screenshot](images/presentation/eeglab-spectrum.png)

**Source:** PowerPoint, slide 26. The slide refers to a tutorial dataset. This is evidence of EEGLAB exploration, not a locally collected multichannel classroom recording. [Analysis scope](AI_AND_DATA.md#6-matlab-and-eeglab-scope).

## AI experiment and saved model outputs

The original notebook experiment and the slide figures are preserved separately because their reported results differ. Neither source has been rerun or validated in this packaging update. [Evaluation limitations](AI_AND_DATA.md#4-historical-result-and-limitations).

### Feature distributions

![Feature histograms from the original notebook](images/notebook/feature-distributions.png)

**Source:** Original notebook, cell 13. Distributions after the notebook's row filtering.

![Feature histograms after normalization](images/notebook/normalized-distributions.png)

**Source:** Original notebook, cell 17. Historical normalized distributions. The original notebook fits normalization before splitting; this needs correction for valid evaluation.

### Correlation heatmap

![Feature correlation heatmap from the PowerPoint](images/presentation/correlation-heatmap.png)

**Source:** PowerPoint, slide 34. Exploratory associations among features and the label. Correlation is not proof of a causal relationship with student performance.

### Neural-network architecture

![CNN BiLSTM architecture from the PowerPoint](images/presentation/model-architecture.png)

**Source:** PowerPoint, slide 35. Architecture diagram from the historical experiment. The supplied input arrangement gives the recurrent layer an outer sequence length of one; see the [shape review](AI_AND_DATA.md#3-observed-data-dimensions).

### Notebook variant 1: saved results

| Accuracy | Loss |
|---|---|
| ![Notebook variant 1 accuracy](images/notebook/dataset-1-accuracy.png) | ![Notebook variant 1 loss](images/notebook/dataset-1-loss.png) |

![Notebook variant 1 confusion matrix](images/notebook/dataset-1-confusion-matrix.png)

**Source:** Original notebook, cells 31 and 32. The matrix is `[[6, 4], [1, 9]]`: 15 correct predictions out of 20 entries, matching the saved 75% evaluation result. Training/validation divergence is visible. Empty sequence slots, participant overlap, normalization leakage, and validation reuse limit interpretation.

### Notebook variant 2: saved results

| Accuracy | Loss |
|---|---|
| ![Notebook variant 2 accuracy](images/notebook/dataset-2-accuracy.png) | ![Notebook variant 2 loss](images/notebook/dataset-2-loss.png) |

![Notebook variant 2 confusion matrix](images/notebook/dataset-2-confusion-matrix.png)

**Source:** Original notebook, saved outputs in cells 34 and 35. The saved matrix also shows 15/20 correct entries. These are a second representation of the original dataset, not results on a new independent classroom cohort.

### PowerPoint slide 36: different historical results

| Accuracy in slide | Loss in slide |
|---|---|
| ![PowerPoint historical accuracy](images/presentation/presentation-training-accuracy.png) | ![PowerPoint historical loss](images/presentation/presentation-training-loss.png) |

![PowerPoint historical confusion matrix](images/presentation/presentation-confusion-matrix.png)

**Source:** PowerPoint, slide 36. This matrix is `[[7, 3], [0, 10]]`, or 17/20 correct entries (85%). It differs from the supplied notebook's 75% output. The training configuration and run history needed to reconcile them were not supplied. This figure is included for historical completeness, not adopted as the repository's verified accuracy.

## Power BI and result comparisons

These are original reporting screenshots. No editable `.pbix` file was found. The chart labels are preserved, even where feature naming or interpretation needs correction. They must not be treated as a controlled demonstration of improved learning.

### Complete dashboard

![Historical Power BI dashboard](images/results/powerbi-dashboard.png)

**Source:** Results slides, page 37. Daily/monthly charts, a variance graphic, and student details. Original names and roll numbers are retained.

### Daily charts

| Frequency-labeled chart | Attention chart |
|---|---|
| ![Daily frequency chart](images/results/daily-frequency.png) | ![Daily attention chart](images/results/daily-attention.png) |

**Source:** Results slides, pages 39 and 40. These plots document the original reporting output; the underlying transformation pipeline and interpretation of the frequency metric are not established.

### Monthly charts

| Frequency-labeled chart | Attention chart |
|---|---|
| ![Monthly frequency chart](images/results/monthly-frequency.png) | ![Monthly attention chart](images/results/monthly-attention.png) |

**Source:** Results slides, pages 41 and 42. Aggregated examples shown in the presentation. The supplied Python script alone does not reproduce these monthly reports.

### Variance graphic

![Alpha beta gamma variance donut chart](images/results/band-variance.png)

**Source:** Results slides, page 43. Original variance graphic. A similar share among plotted values does not by itself establish a physiological interpretation.

### Student comparison

![Original comparison of two students](images/results/student-comparison.png)

**Source:** Results slides, page 44. Historical two-student comparison. It is a descriptive presentation figure, not a controlled experiment showing that the device improved student performance.

### Attention-series comparison

![Attention and calculated attention series shown in the results](images/results/attention-comparison.png)

**Source:** Results slides, page 45. Original chart labeled `Attention` and `Attention_Cal`. The exact calculation, source records, and independent validation are not established; proximity of the lines alone is not evidence of predictive validity.

## Source files and traceability

- [Original editable presentation](../supporting-documents/Project-Presentation.pptx)
- [Original results slides PDF](../supporting-documents/Results-and-Discussion-Slides.pdf)
- [Packaged notebook with historical-output notice](../notebooks/confused_student_identification.ipynb)
- [Machine-readable visual index](VISUAL_INDEX.json)
- [Source hashes, image locations, and packaging changes](ASSET_PROVENANCE.json)

Extraction retains the original source content. Inclusion does not establish that every diagram/photo in the original documents was authored by the team; asset reuse remains subject to [the license notice](../LICENSE-NOTICE.md).
