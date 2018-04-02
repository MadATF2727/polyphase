import math

# module purpose: split a signal or a filter into
# M sub-signals (or sub-filters) where M is the decimation factor
##############################################################
# inputs:
# N signal samples
# M (decimation factor)
# outputs:
# an array of M sub-signals of length ceil(M/N)


def fillSigArray(sig,M):
    '''inputs: M (decimation factor), L (sub-signal length),
     sig (signal to split)
     outputs: list of lists where each member is one of M sub-signals'''
    # get the length of the sub-signal
    subLen = int(math.ceil(len(sig)/M))
    # if necessary, zero pad
    if len(sig) % M != 0:
        toAppend = M - int(len(sig) % M)
        for i in range(toAppend):
            sig.append(complex(0,0))
    # make an empty list of lists for split signal
    sigArray = [[complex(0,0)]*subLen for i in range(M)]
    # ind counts where in the original signal the loop is
    ind = 0
    # fill list of lists
    for col in range(subLen):
        for row in range(M):
            sigArray[row][col] = sig[ind]
            ind  += 1
    return sigArray

if __name__ == "__main__":
    testSig = [1]*27
    arr = fillSigArray(testSig, 5)
    print('FOOBARBATBAZ')







