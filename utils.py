import matplotlib.pyplot as plt

def get_figure(npix, dpi=10, styles=['maps'], alpha=False):
    # Styles
    plt.style.use(styles)

    # Figure working size
    imsize = npix/dpi

    # New figure
    fig = plt.figure(figsize=(imsize,imsize), dpi=dpi, frameon=False)
    if alpha:
        fig.patch.set_alpha(0)

    # Axis
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')

    return fig, ax

def select_data(imshape, blc=None, trc=None):
    if trc and blc:
        x0, x1 = blc[0],trc[0]+1
        y0, y1 = blc[1],trc[1]+1
        dim0 = abs(x1-x0)
        dim1 = abs(y1-y0)
        if dim0!=dim1:
            print "WARNING: selected area is not square, using smaller side"
            npix = min(dim0, dim1)
            x1 = x0+npix
            y1 = y0+npix
        else:
            npix = dim0
    else:
        try:
            assert imshape[-2]==imshape[-1]
            npix = imshape[-2]
        except AssertionError:
            print "WARNING: data is not square, using smaller side"
            npix = min(imshape[-2],imshape[-1])
        x0, x1 = 0, npix
        y0, y1 = 0, npix

    return npix, x0, x1, y0, y1

