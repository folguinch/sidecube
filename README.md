# sidecube

A package to overplot spectra on maps and visualize it. The program loads a
base layer (e.g. continuum image) and creates an overlay layer with the spectra
in a cube.

# Requirements

`sidecube` requires the following programs/packages:

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

A map with 6 zoom levels and a 200x200 image will take more than 15-20 minutes.

# Usage

```bash
sidecube [-v|--verbose] [-n|--noredo] 
[--blc blc_x blc_y ] [--trc trc_x trc_y] [-z|--zoom zoomlevel] 
[[--baselayer base_layer.fits] [--name baselayer1]] ... 
[[--overlay overlay_cube.fits] [-c|--chanrange c1 c2] [--name line1] [--color black] [[--level|--limit level] [--autolimit]] [--every number]] ...
```

The default zoom level is `zoomlevel=6`. If for some reason the program was 
stopped, use the flag `-n` or `--noredo` to resume.

At the moment the program only accepts data with the same size.

The commands `--baselayer` and `--overlay` can be repeated to plot multiple 
layers. The sub-commands configure the preceding base layer or overlay plot 
and are optional. 

The sub-commands for base layers are:
- `name`: assign a name to the layer. This is used in the file names and in the
layer selection of the map web page. If not given a generic name is generated.

The sub-commands for overlays are:
- `name`: same as for base layers.
- `c` or `chanrange`: the channel range. Channels are zero-based.
- `color`: line color (any value accepted by matplotlib).
- `level` or `limit`: a minimum flux limit for the spectrum values.
- `autolimit`: filter out spectra with values within  the mean +/- 3sigma. With 
the mean and sigma calculated over all the values in the selected channels.
- `every`: plot every other pixel from the peak value. It can be combined with 
the two options above.

## Examples

To generate a map with all the spectra in a box with bottom left corner
(100,100) and top right corner (300,300) and channels between 0 and 50:
```bash
sidecube --blc 100 100 --trc 300 300 --baselayer base_layer.fits --overlay overlay_cube.fits -c 0 50
```
Note the pixels and channels are zero-based.

Generate the same map but with 2 overlays with channels between 0-50 and 
150-200, one black and the other blue:
```bash
sidecube --blc 100 100 --trc 300 300 --baselayer base_layer.fits 
--overlay overlay_cube.fits -c 0 50 --color k 
--overlay overlay_cube.fits -c 150 200 --color b
```

We recommend to run the code with no more than 200 pixels per side, and use the limiting parameters.

# Implemented features

The following features have been implemented:

- Plot multiple base and overlay layers.
- The overlay layer is tiled from zoom level 4 upwards (transparency does not
  work well with lower levels).
- All the ticked features in Road map.

# Road map

For version v1.0:

- [x] Plot multiple base layers
- [x] Plot multiple overlays
- [ ] Coordinate grid overlay
- [ ] Use frequency instead of channels
- [ ] Base layer customization: vmin, vmax, color map, scale

Long term features

- [ ] Improve transparency
- [ ] Convert map units to sky units
- [x] Verbose mode

