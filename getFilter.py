from scipy import signal as signal
from matplotlib import pyplot as plt
import numpy

def getCoeffs(cutoff, numTap):
    '''inputs: cutoff: cutoff frequency (relative to fs = 1), numTaps: number of taps,
    outputs: filtCoeff: list of filter coefficients'''
    coeffs = signal.firwin(numTaps, cutoff)
    return coeffs

def plotFilt(coeffs):
    w, h = signal.freqz(coeffs)
    fig = plt.figure()
    plt.title('LPF Frequency Response')
    ax1 = plt.subplot(111)
    plt.plot(w, 20 * numpy.log10(abs(h)), 'b')
    plt.ylabel('Amplitude [dB]', color='b')
    plt.xlabel('Frequency [rad/sample]')
    ax2 = ax1.twinx()
    angles = numpy.unwrap(numpy.angle(h))
    plt.plot(w, angles, 'g')
    plt.ylabel('Angle (radians)', color='g')
    plt.grid()
    plt.axis('tight')
    plt.show()


if __name__ == "__main__":
    # cutoff frequency is Fs/2 divided by 5. Since Fs is 10kHz, .2 corresponds to 2 kHz
    cutoff = .2
    numTaps = 27
    coeffs = getCoeffs(cutoff, numTaps)
    plotFilt(coeffs)
    print('FOOBAR')