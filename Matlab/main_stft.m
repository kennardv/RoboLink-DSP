clear, clc, close all
[x, Fs] = audioread('Alarm01.wav');
% sound(x, Fs);

x = x(:, 1);                        % get the first channel
xmax = max(abs(x));                 % find the maximum abs value
x = x/xmax;                         % scalling the signal

% define analysis parameters
xlen = length(x);                   % length of the signal
wlen = 1024;                        % window length (recomended to be power of 2)
h = wlen/4;                         % hop size (recomended to be power of 2)
nfft = 4096;                        % number of fft points (recomended to be power of 2)

% define the coherent amplification of the window
K = sum(hamming(wlen, 'periodic'))/wlen;

% perform STFT
[stft, f, t] = STFT(x, wlen, h, nfft, Fs);

% take the amplitude of fft(x) and scale it, so not to be a
% function of the length of the window and its coherent amplification
stft = abs(stft)/wlen/K;

% correction of the DC & Nyquist component
if rem(nfft, 2)                     % odd nfft excludes Nyquist point
    st(2:end, :) = stft(2:end, :).*2;
else                                % even nfft includes Nyquist point
    stft(2:end-1, :) = stft(2:end-1, :).*2;
end

% % convert amplitude spectrum to dB (min = -120 dB)
% stft = 20*log10(stft + 1e-6);
% 
% % plot the spectrogram
% figure(1)
% imagesc(t, f, stft)
% set(gca,'YDir','normal')
% xlabel('Time, [s]')
% ylabel('Frequency, [Hz]')
% title('Amplitude spectrogram of the signal')
% 
% handl = colorbar;
% ylabel(handl, 'Magnitude, dB')

[x1, Fs1] = ISTFT(stft, h, nfft, Fs);
sound(x1, Fs1);