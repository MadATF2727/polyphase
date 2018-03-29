from scipy import signal
import matplotlib

def getCoeffs(cutoff, numTaps):
    '''inputs: cutoff: cutoff frequency in Hz, numTaps: number of taps,
    outputs: filtCoeff: list of filter coefficients'''

if __name__ == "__main__":
    # cutoff frequency is Fs/2 divided by 5. Since Fs is 10kHz, .2 corresponds to 2 kHz
    cutoff = .2
    numTaps = 17
    coeffs = getCoeffs(cutoff, numTaps)