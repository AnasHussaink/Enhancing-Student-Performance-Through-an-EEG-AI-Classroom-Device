# Engineering domains and contribution

[Back to README](../README.md)

Anas reports involvement across the project. The supplied work is a team final-year project; this page describes the domains represented without assigning unsupported individual ownership.

## Biomedical instrumentation

The project involves scalp EEG concepts, electrode placement, reference contacts, and interpreting module-generated attention and power features. Practical development centers on integrating an existing TGAM module. It does not establish clinical expertise or a validated diagnostic device.

**Keywords:** EEG, biosignal acquisition, biomedical instrumentation, electrode integration, signal quality, wearable sensing.

## Electronics and system integration

The physical prototype combines an acquisition module, wireless communication, power, and a wearable structure. This supports describing electronics prototyping and hardware/software integration. No supplied controller firmware establishes custom STM32, ESP8266, Arduino, or Raspberry Pi firmware development for the final device.

**Keywords:** hardware integration, module interfacing, Bluetooth serial communication, portable electronics, prototype assembly.

## Mechanical design

Design images and four STL components support enclosure/headband work, component accommodation, and preparation of printable parts. The exact CAD tool and print process should only be named after confirming them from the original work.

**Keywords:** wearable enclosure design, CAD, STL, mechanical integration, 3D-printable parts, prototyping.

## Protocols and application programming

The Python program works with serial framing, checksums, payload interpretation, background acquisition, GUI updates, and CSV export. The parser defect is a concrete opportunity to demonstrate debugging and protocol verification once corrected.

**Keywords:** Python, PySerial, binary parsing, serial communication, checksums, Tkinter, Matplotlib, pandas, NumPy, threading, CSV logging.

## Signal and data analysis

The MATLAB scripts manipulate existing EEG-related features, visualize them, and prepare an EEGLAB structure. More advanced filtering, FFT, ICA, or wavelet expertise should be supported with the corresponding working pipeline before being claimed as a completed implementation.

**Keywords:** MATLAB, EEG feature analysis, time-series visualization, data preprocessing, EEGLAB exploration.

## Machine learning

The notebook demonstrates experimentation with TensorFlow/Keras, CNNs, a bidirectional LSTM, and binary classification on public EEG data. Model evaluation requires revision, so describe this as experimentation rather than validated production deployment.

**Keywords:** TensorFlow, Keras, scikit-learn, CNN, BiLSTM, binary classification, feature transformation, exploratory data analysis, Jupyter Notebook, model evaluation.

## Research, visualization, and communication

The report, presentations, dashboard, and Power BI figures represent literature review, technical writing, and communication of prototype results. Power BI source files are not available in this package, so the original reporting workflow cannot yet be reproduced.

**Keywords:** research documentation, literature review, technical reporting, dashboard development, Power BI visualization, engineering presentation.

## Suggested accurate project description

> Contributed across the design and development of a TGAM-based wearable EEG classroom-monitoring prototype, including enclosure integration, Bluetooth serial acquisition, a Python dashboard, and attention-data logging. Explored EEG feature analysis in MATLAB/EEGLAB and a separate CNN–BiLSTM confused-student classification experiment using public EEG data.

Avoid adding a validated accuracy figure, proven learning improvement, cloud deployment, embedded Linux, or live AI inference unless subsequent work provides evidence for that claim.
