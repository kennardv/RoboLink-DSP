clear, clc, close all
[x, Fs] = audioread('Alarm01.wav');
% sound(x, Fs);
x = x(:,1);

% Short-time Fourier transform
% Time instants (values correspond to midpoint of each section
% Cyclical frequencies (length = # rows of stft)
[stft, f, t] = spectrogram(x, [], [], [], Fs);
spectrogram(x, [], [], [], Fs, 'yaxis')