import os, argparse
from itertools import product

import numpy as np
from astropy.io import fits

from utils import get_figure, select_data

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chanrange', nargs=2, type=int,
            help='Channel range')
    parser.add_argument('--blc', nargs=2, type=int,
            help='Bottom left corner of the data box')
    parser.add_argument('--trc', nargs=2, type=int,
            help='Top right corner of the data box')
    parser.add_argument('--xcoverage', default=0.8, type=float,
            help='Coverage of the spectrum range over each pixel')
    parser.add_argument('cube', type=str,
            help='FITS cube file name')
    parser.add_argument('out', type=str,
            help='Output plot file name')
    args = parser.parse_args()

    # Open cube
    cube = fits.open(os.path.expanduser(args.cube))[0]

    # Select data
    npix, x0, x1, y0, y1 = select_data(cube.shape, blc=args.blc, trc=args.trc)
    if args.chanrange:
        lenspec = abs(args.chanrange[1]-args.chanrange[0]) + 1
        s0, s1 = args.chanrange[0], args.chanrange[1]+1
    else:
        lenspec = cube.shape[-3]
        s0, s1 = 0, lenspec

    # Data scaling
    subcube = cube.data[0, s0:s1, y0:y1, x0:x1]
    scaling = 1.01*np.nanmax(subcube)
    xempty = (1. - args.xcoverage)*0.5
    xaxis = np.linspace(xempty,1.-xempty, lenspec)

    # Create figure
    fig, ax = get_figure(npix, alpha=True)

    # Limits
    ax.set_xlim(0, npix)
    ax.set_ylim(-0.5, npix-0.5)

    # Plot
    for x,y in product(range(npix), range(npix)):
        # Spectrum
        spec = subcube[:, y, x]
        if np.any(np.isnan(spec)):
            continue

        # X axis
        wlg = xaxis+x
        
        # Plot
        ax.plot(wlg, spec/scaling+y, 'k-', lw=0.05)

    fig.savefig(args.out, dpi=600)

if __name__=='__main__':
    main()
