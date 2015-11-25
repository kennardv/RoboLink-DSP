import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

class LowPassFilter:
    def __init__(self, order, samplerate, cutoff):
        self.order = order
        self.fs = samplerate
        self.cutoff = cutoff

    def butter_lowpass(self):
        nyq = 0.5 * self.fs
        normal_cutoff = self.cutoff / nyq
        # Design Nth order filter and return filter coefficients
        b, a = butter(self.order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_lowpass_filter(self, data):
        b, a = self.butter_lowpass()
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
        plt.title("Lowpass Filter Frequency Response")
        plt.xlabel('Frequency [Hz]')
        plt.grid()
        plt.show()

    def plot(self, signals):
        plt.figure(2)
        
        for element in signals:
            plt.plot(t, element[0], element[1], label=element[2])
            
        plt.xlabel('Time [sec]')
        plt.xlim([0, 0.2])
        plt.grid()
        plt.legend()
        plt.subplots_adjust(hspace=0.35)
        plt.show()
        

# Filter requirements.
order = 6
fs = 30000.0       # sample rate, Hz
cutoff = 200  # desired cutoff frequency of the filter, Hz

lpf = LowPassFilter(order, fs, cutoff)

# Get the filter coefficients so we can check its frequency response.
b, a = lpf.butter_lowpass()
lpf.plot_freq_resp(b, a)


# Demonstrate the use of the filter.
# First make some data to be filtered.
T = 5.0               # seconds
n = int(T * fs) # total number of samples
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 2 Hz signal from this.
f1 = 200
f2 = 1000
sin1 = np.sin(2*np.pi*f1*t)
sin2 = np.sin(2*np.pi*f2*t)
data = sin1 + sin2


# Filter the data
y = lpf.butter_lowpass_filter(data)

# Plot both the original and filtered signals.
# Data, color, description
lpf.plot([[y, 'g-', 'filtered signal'], [sin1, 'r-', 'sin1']])

