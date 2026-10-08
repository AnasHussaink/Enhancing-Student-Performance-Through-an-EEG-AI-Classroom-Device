% Load the EEG data from the CSV file
data = readtable('EEG_data_college_students.csv');

% Extract relevant columns
delta = data.Delta;
theta = data.Theta;
alpha = (data.Alpha1 + data.Alpha2) / 2;
beta = (data.Beta1 + data.Beta2) / 2;
gamma = (data.Gamma1 + data.Gamma2) / 2;

% Define the sampling frequency
fs = 256; % Example sampling frequency

% Plot the extracted frequency bands
time = (0:length(delta)-1) / fs;

figure;
subplot(5, 1, 1);
plot(time, delta);
title('Delta Band (1-4 Hz)');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(5, 1, 2);
plot(time, theta);
title('Theta Band (4-8 Hz)');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(5, 1, 3);
plot(time, alpha);
title('Alpha Band (8-12 Hz)');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(5, 1, 4);
plot(time, beta);
title('Beta Band (12-30 Hz)');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(5, 1, 5);
plot(time, gamma);
title('Gamma Band (30-100 Hz)');
xlabel('Time (s)');
ylabel('Amplitude');

% Save the extracted frequency bands to a .mat file
save('extractedBands.mat', 'delta', 'theta', 'alpha', 'beta', 'gamma');
