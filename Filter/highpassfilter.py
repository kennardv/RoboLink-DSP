import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

class HighPassFilter:
    def __init__(self, order, samplerate, cutoff):
        self.order = order
        self.fs = samplerate
        self.cutoff = cutoff

    def butter_highpass(self):
        nyq = 0.5 * self.fs
        normal_cutoff = self.cutoff / nyq
        # Design Nth order filter and return filter coefficients
        b, a = butter(self.order, normal_cutoff, btype='high', analog=False)
        return b, a

    def butter_highpass_filter(self, data):
        b, a = self.butter_highpass()
        # Filter data along 1 dimension
        y = lfilter(b, a, data)
        return y

    def plot_freq_resp(self, b, a):
        # Compute frequency response of a digital filter
        w, h = freqz(b, a, worN=8000)
        # Plot the frequency response.
        plt.figure(1)
        plt.plot(0.5*self.fs*w/np.pi, np.abs(h), 'b')
        plt.plot(self.cutoff, 0.5*np.sqrt(2), 'ko')
        plt.axvline(self.cutoff, color='k')
        plt.xlim(0, 0.5*self.fs)
        plt.title("Highpass Filter Frequency Response")
        plt.xlabel('Frequency [Hz]')
        plt.grid()
        plt.show()

    def plot(self, signals):
        plt.figure(2)
        
        for element in signals:
            plt.plot(t, element[0], element[1], label=element[2])
            
        plt.xlabel('Time [sec]')
        plt.grid()
        plt.legend()
        plt.subplots_adjust(hspace=0.35)
        plt.show()
        


# Filter requirements.
order = 6
fs = 30.0       # sample rate, Hz
cutoff = 3.667  # desired cutoff frequency of the filter, Hz

hpf = HighPassFilter(order, fs, cutoff)

# Get the filter coefficients so we can check its frequency response.
b, a = hpf.butter_highpass()
hpf.plot_freq_resp(b, a)


# Demonstrate the use of the filter.
# First make some data to be filtered.
T = 5.0         # seconds
n = int(T * fs) # total number of samples
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

# Filter the data
y = hpf.butter_highpass_filter(data)

# Plot both the original and filtered signals.
# Data, color, description
hpf.plot([[data, 'b-', 'data'], [y, 'g-', 'filtered data']])