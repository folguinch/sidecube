# sidecube

A package to overplot spectra on maps and visualize it. The program loads a
base layer (e.g. continuum image) and creates an overlay layer with the spectra
in a cube.

# Requirements

The code requires the following programs/packages:

- imagemagick
- python 2.7
- matplotlib
- numpy
- astropy

The code has been tested in a machine with multiple cores. The code run several
tasks in parallel depending on the number of zoom levels requested. In general
the maximum number of processes it can run simultaneously is twice the number
of zoom levels. However, plotting and tiling a base layer will finish before
plotting the overlay layer.

A map with 6 zoom levels and a 200x200 image will take more than 15 minutes.

# Usage

```bash
sidecube [-n|--noredo] [--blc blc_x blc_y ] [--trc trc_x trc_y] [-c|--chanrange  c1 c2]
 [-z|--zoom zoomlevel] base_layer.fits overlay_cube.fits
```

The default zoom level is 6. If for some reason the program was stopped, use
the flag `-n` or `--noredo` to resume.

To generate a map with all the spectra in a box with bottom left corner
(100,100) and top right corner (300,300) and channels between 0 and 50:
```bash
sidecube --blc 100 100 --trc 300 300 -c 0 50 base_layer.fits overlay_cube.fits
```
Note the pixels and channels are zero-based.

We recommend to run the code with no more than 200 pixels per side.

# Implemented features

The following features have been implemented:

- Plot a single base and overlay layers.
- The `index.html` file only supports 6 zoom levels at the moment.
- The overlay layer is tiled from zoom level 4 upwards (transparency does not
  work well with lower levels).
- All the ticked features in Road map.

# Road map

For version v1.0:

- [ ] Plot multiple base layers
- [ ] Plot multiple overlays
- [ ] Coordinate grid overlay
- [ ] Use frequency instead of channels
- [ ] Base layer customization: vmin, vmax, color map, scale

Long term features

- [ ] Improve transparency
- [ ] Convert map units to sky units
- [ ] Verbose mode

