% Read the CSV file
data = readtable('concentration_data.csv');

% Exclude non-numeric columns
numericData = data(:, vartype('numeric'));

% Convert to array and transpose if needed
dataArray = table2array(numericData)';
 
% Create an empty EEG structure
EEG = eeg_emptyset; 

% Set EEG parameters
EEG.data = dataArray; % Assign data to EEG structure
EEG.srate = 256; % Set your sampling rate here (adjust based on your data)
EEG.nbchan = size(EEG.data, 1); % Number of channels
EEG.pnts = size(EEG.data, 2); % Number of time points
EEG.trials = 1; % Number of trials (1 if continuous data)
EEG.setname = 'EEG Data from CSV'; % Set dataset name
EEG.filename = 'concentration_data.set'; % Set filename for saving

% Add any additional fields you need
% Use EEGLAB to save the data in .set format
[ALLEEG, EEG, CURRENTSET] = eeg_store(ALLEEG, EEG, 0); % Store EEG data
EEG = pop_saveset(EEG, 'filename', 'concentration_data.set'); % Save data
