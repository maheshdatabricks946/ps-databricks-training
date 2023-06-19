#import pytest
import matplotlib.pyplot as plot
import numpy as np

def sine_wave():
    time = np.arange(-8,8, 0.1)
    # amplitude = np.sin(time)
    # plot.plot(time, amplitude)
    # plot.show()

    amplitude = np.cos(time)
    plot.plot(time, amplitude)
    plot.show()

if __name__ == "__main__":
    sine_wave()
