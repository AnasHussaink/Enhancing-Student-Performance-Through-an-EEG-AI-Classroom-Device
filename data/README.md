# Data sources and handling

[Back to project README](../README.md)

Datasets are deliberately not bundled in this publication package. This keeps public-dataset licensing separate and avoids redistributing local participant records whose provenance and publication consent are not established.

## Public confused-student EEG data

Source: [Confused student EEG dataset on Kaggle](https://www.kaggle.com/wanghaohan/confused-eeg/home).

Obtain the dataset from its publisher, review its current terms, and place the file here:

```text
data/public/EEG_data_college_students.csv
```

The reviewed local copy has 12,811 rows and these 15 columns:

```text
SubjectID, VideoID, Attention, Mediation, Raw, Delta, Theta,
Alpha1, Alpha2, Beta1, Beta2, Gamma1, Gamma2,
predefinedlabel, user-definedlabeln
```

`Mediation` and `user-definedlabeln` preserve the actual column spellings. Changing them without updating the notebook would break its expectations. The supplied copy contains 10 subjects and 10 videos. It is not a dataset collected by this project team.

The notebook expects to run with the `notebooks/` directory as its working directory. The MATLAB scripts use their original input filenames, so configure their working directory or input paths separately.

## Local/transformed file reviewed

The source collection contains `concentration_data.csv` with 1,960 rows and columns:

```text
Timestamp, EEG_Freaquency, Alpha, Beta, Gamma, Attention
```

The spelling `EEG_Freaquency` is from the original file. Its collection or generation script was not established. Review found 58 timestamp strings, no missing values, eight distinct attention values, and a strongly structured relationship between its frequency and attention columns. This does not by itself establish whether it is measured, transformed, or an illustrative dataset.

Before using or sharing it, document the originating device, session protocol, participant count, units, sampling interval, all transformations, and how the attention labels were produced. Do not treat derived labels as independent ground truth.

## New recordings

The desktop prototype writes attention CSVs under `data/local/`. Both data subdirectories are ignored by Git except their placeholders. Do not force-add participant data without verifying consent, de-identification, and the intended release terms.

A future session record should include a pseudonymous session ID, software/configuration version, timestamps, signal quality, relevant feature values, a collection protocol, and any independently obtained labels. Collect only the identifiers needed for the experiment.
