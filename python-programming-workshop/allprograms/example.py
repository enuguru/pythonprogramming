"""example.py

Compute the maximum of a Bessel function and plot it.

"""
import argparse

import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--order", type=int, default=3, help="order of Bessel function")
    parser.add_argument("--output", default="plot.png", help="output image file")
    args = parser.parse_args()

    # Compute maximum
    f = lambda x: -special.jv(args.order, x)
    sol = optimize.minimize(f, 1.0)

    # Plot
    x = np.linspace(0, 10, 5000)
    plt.plot(x, special.jv(args.order, x), '-', sol.x, -sol.fun, 'o')

    # Produce output
    plt.savefig(args.output, dpi=96)

// create a class that can be used to compute the maximum of a Bessel function and plot it
# using a class-based approach
import matplotlib.pyplot as plt
import numpy as np
from scipy import special, optimize

class BesselFunctionPlotter:
    def __init__(self, order=3, output="plot.png"):
        self.order = order
        self.output = output

    def compute_maximum(self):
        f = lambda x: -special.jv(self.order, x)
        sol = optimize.minimize(f, 1.0)
        return sol.x, -sol.fun

    def plot(self):
        x = np.linspace(0, 10, 5000)
        plt.plot(x, special.jv(self.order, x), '-', *self.compute_maximum(), 'o')
        plt.savefig(self.output, dpi=96)

#  Example usage of the class
if __name__ == "__main__":
    plotter = BesselFunctionPlotter(order=3, output="plot.png")
    plotter.plot()
# This code computes the maximum of a Bessel function and plots it using a class-based approach.


if __name__ == "__main__":
    main()

# write a new python class  

