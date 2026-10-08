# Publish this repository on GitHub

[Back to README](../README.md)

The prepared folder contains the repository contents. It has not been uploaded to your GitHub account by creating this package.

**For this expanded package, use GitHub Desktop or command-line Git:** the complete report is approximately 69.4 MiB, which exceeds the browser's 25 MiB per-file limit. All packaged files are below 100 MiB. [GitHub upload limits](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

## 1. Extract the package

Extract the supplied ZIP. Open the `EEG-AI-Classroom-Device` folder and confirm that `README.md`, `docs`, `software`, `notebooks`, `matlab`, `hardware`, `data`, and `supporting-documents` are visible inside it.

Upload these contents into the root of the intended repository. Do not upload only the ZIP, and do not add an unnecessary extra enclosing folder above `README.md`.

## 2. Recommended: update your existing repository using GitHub Desktop

1. Clone your existing GitHub repository in GitHub Desktop, or open its existing local checkout.
2. Open that checkout in File Explorer.
3. Copy the prepared repository's contents into the checkout's root, preserving all subfolders. Review replacements of matching files and retain unrelated work.
4. Review the changes in GitHub Desktop. Confirm the images and supporting documents appear, including the full report.
5. Commit with a message such as `Add presentation visuals, GUI, graphs and supporting documents`.
6. Push the commit, then check the README and gallery on GitHub.

The file is below GitHub's 100 MiB limit for Git uploads. For repeated future revisions of large binary reports, consider a release attachment or Git LFS to avoid growing repository history unnecessarily.

## 3. Browser upload for the smaller files

The following method works for the smaller files, but **cannot upload the full DOCX report**. Upload that report through Git before considering the repository complete; otherwise its README download link will be broken.

1. Open your existing project repository, or create a repository such as `EEG-AI-Classroom-Device`.
2. Choose **Add file → Upload files**.
3. From File Explorer, select the extracted files and folders inside the prepared repository and drag them onto the upload area. Folder drag-and-drop preserves the paths; a file chooser may only let you select files.
4. Check that paths such as `docs/images/headband-design.jpg` remain intact.
5. Use a commit message such as `Document EEG classroom prototype and add project assets`.
6. Review the uploaded paths and commit the intended changes.

If your browser cannot upload folders, use GitHub Desktop to copy the complete folder structure into a local checkout, review the changes, commit, and push. Do not flatten every image into the repository root: the README uses relative paths into `docs/images/`.

For an existing repository, compare any existing files before replacing matching paths. Retain unrelated project work.

## 4. Verify after publishing

- The repository homepage renders the README.
- The headband image, real prototype, annotated hardware image, and dimension drawing appear.
- Both Mermaid diagrams render in the README.
- Links to the domain documentation and STL files open.
- The notebook is viewable and its historical-status notice appears first.
- The GUI, graphs, and visual gallery load, and all six supporting documents can be downloaded.
- Original screenshots/documents retain student names, roll numbers, and photographs. Check that these details are intended for public release; this package has not anonymized them.
- No additional private local recordings were accidentally included.

## 5. Suggested repository description

> TGAM-based wearable EEG classroom-monitoring prototype with a Python dashboard, enclosure files, MATLAB exploration, and an offline confused-student AI experiment.

Suggested topics: `eeg`, `tgam`, `wearable`, `python`, `tkinter`, `bluetooth`, `matlab`, `eeglab`, `tensorflow`, `student-engagement`.

## 6. Release scope and reuse

This package includes a known-issues register because the original prototype and ML evaluation still need correction. Do not label the initial publication a production-ready or clinically validated system. Agree on the licensing of team code and assets before selecting a repository license; see [license notice](../LICENSE-NOTICE.md).
