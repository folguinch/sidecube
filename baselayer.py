import os, argparse

import numpy as np
from astropy.io import fits

from utils import get_figure, select_data

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--blc', nargs=2, type=int,
            help='Bottom left corner of the data box')
    parser.add_argument('--trc', nargs=2, type=int,
            help='Top right corner of the data box')
    parser.add_argument('image', type=str,
            help='FITS file name')
    parser.add_argument('out', type=str,
            help='Output plot file name')
    args = parser.parse_args()

    # Open data
    img = fits.open(os.path.expanduser(args.image))[0]
    data = np.squeeze(img.data)

    # Select data
    npix, x0, x1, y0, y1 = select_data(data.shape, blc=args.blc, trc=args.trc)

    # Create figure
    fig, ax = get_figure(npix)

    # Plot
    if args.trc and args.blc:
        ax.imshow(data[y0:y1,x0:x1])
    else:
        ax.imshow(data)

    # Save
    fig.savefig(args.out, dpi=600)

if __name__=='__main__':
    main()
