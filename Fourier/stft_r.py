#import modules
import scipy, pylab, wave, numpy

def stft(x, fs, framesz, hop):
    """x is the time-domain signal
    fs is the sampling frequency
    framesz is the frame size, in seconds
    hop is the the time between the start of consecutive frames, in seconds

    """
    framesamp = int(framesz*fs)
    hopsamp = int(hop*fs)
    w = scipy.hamming(framesamp)
    X = scipy.array([scipy.fft(w*x[i:i+framesamp]) 
                     for i in range(0, len(x)-framesamp, hopsamp)])
    return X

def istft(X, fs, T, hop):
    """X is the short-time Fourier transform
    fs is the sampling frequency
    T is the total length of the time-domain output in seconds
    hop is the the time between the start of consecutive frames, in seconds

    """
    x = scipy.zeros(T*fs)
    framesamp = X.shape[1]
    hopsamp = int(hop*fs)
    for n,i in enumerate(range(0, len(x)-framesamp, hopsamp)):
        x[i:i+framesamp] += scipy.real(scipy.ifft(X[n]))
    return x

if __name__ == '__main__':
    f0 = 440         # Compute the STFT of a 440 Hz sinusoid
    fs = 8000        # sampled at 8 kHz
    T = 5            # lasting 5 seconds
    framesz = 0.050  # with a frame size of 50 milliseconds
    hop = 0.020      # and hop size of 20 milliseconds.

    # Create test signal and STFT.
    t = scipy.linspace(0, T, T*fs, endpoint=False)
    x = scipy.sin(2*scipy.pi*f0*t)
    X = stft(x, fs, framesz, hop)

    # WAV file
    wf = wave.open('bensound-happiness.wav', 'rb')
    y = numpy.fromstring(wf.readframes(-1), dtype=numpy.int16)        # read all frames
    y = y[0::2]                                                 # get left channel only
    Y = stft(y, fs, framesz, hop)
    print type(Y)
    print Y.shape
    Ylength = len(Y)
    countX = round(len(Y)/6)
    countY = round(len(Y[0])/5)
    print countY 
    print countX
    Y = Y.real

    # ugly hardcoded values 6x5 = 30 --> A0 tem E5
    iX = 0
    iY = 0
    A0 = Y[iX,iY]
    iX = iX + countX
    A1 = Y[iX,iY]
    iX = iX + countX
    A2 = Y[iX,iY]
    iX = iX + countX
    A3 = Y[iX,iY]
    iX = iX + countX
    A4 = Y[iX,iY]
    iX = iX + countX
    A5 = Y[iX,iY]
    iX = iX + countY
    iX = 0
    B0 = Y[iX,iY]
    iX = iX + countX
    B1 = Y[iX,iY]
    iX = iX + countX
    B2 = Y[iX,iY]
    iX = iX + countX
    B3 = Y[iX,iY]
    iX = iX + countX
    B4 = Y[iX,iY]
    iX = iX + countX
    B5 = Y[iX,iY]
    iX = iX + countY
    iX = 0
    C0 = Y[iX,iY]
    iX = iX + countX
    C1 = Y[iX,iY]
    iX = iX + countX
    C2 = Y[iX,iY]
    iX = iX + countX
    C3 = Y[iX,iY]
    iX = iX + countX
    C4 = Y[iX,iY]
    iX = iX + countX
    C5 = Y[iX,iY]
    iX = iX + countY
    iX = 0
    D0 = Y[iX,iY]
    iX = iX + countX
    D1 = Y[iX,iY]
    iX = iX + countX
    D2 = Y[iX,iY]
    iX = iX + countX
    D3 = Y[iX,iY]
    iX = iX + countX
    D4 = Y[iX,iY]
    iX = iX + countX
    D5 = Y[iX,iY]
    iX = iX + countY
    iX = 0
    E0 = Y[iX,iY]
    iX = iX + countX
    E1 = Y[iX,iY]
    iX = iX + countX
    E2 = Y[iX,iY]
    iX = iX + countX
    E3 = Y[iX,iY]
    iX = iX + countX
    E4 = Y[iX,iY]
    iX = iX + countX
    E5 = Y[iX,iY]

    print A0
    print E5

    # Plot the magnitude spectrogram.
    pylab.figure()
    pylab.imshow(scipy.absolute(Y.T), origin='lower', aspect='auto',
                 interpolation='nearest')
    pylab.xlabel('Time')
    pylab.ylabel('Frequency')
    pylab.show()

    # Compute the ISTFT.
    xhat = istft(Y, fs, T, hop)

    # Plot the input and output signals over 0.1 seconds.
    T1 = int(0.1*fs)

    pylab.figure()
    pylab.plot(t[:T1], x[:T1], t[:T1], xhat[:T1])
    pylab.xlabel('Time (seconds)')

    pylab.figure()
    pylab.plot(t[-T1:], x[-T1:], t[-T1:], xhat[-T1:])
    pylab.xlabel('Time (seconds)')
