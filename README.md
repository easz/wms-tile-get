# wms-tile-get

Fetch map from WMS server and store them as tiled web map in
[Slippy Map](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) or Google Map convention.
Typically such web map tiles have EPSG:3857 projection.

The output structure:

~~~
.
|- 10/
|  |- 544/
|  |  |- 354.png
|  |  |- 355.png
|  |- 545
|     |- 354.png
|     |- 355.png
|- 11/
|  |- ...
|
|- 12/
|  |- ...
|
~~~

The tool is similar to many others like [wms-tiles-downloader](https://github.com/Luqqk/wms-tiles-downloader)
or QGIS' `gdal2xyz` but it can also accept geojson polygon as area of interest.

## Install

~~~
$ pip install wms-tile-get
~~~

or

~~~
$ conda install -c conda-forge wms-tile-get
~~~

It is highly recommended to use [conda](https://docs.conda.io/en/latest/miniconda.html) to install.
Manual installation with GDAL and others on Windows please see the [instruction](Windows.md).

## Usage

### Fetch tiles for an area (e.g. a city)

~~~
$ cd example/

$ wms-tile-get -s by_wms.json \
               -g munich.boundary.geojson \
               -z 10 \
               -o by_dop80c
~~~

  * `-s` defines configuration file of WMS server parameters.
  * `-g` defines the area(s) of interest (polygon area in geojson).
  * `-z` defines the zoom level(s) of interest.
  * `-o` defines output folder.

An area or boundary shapes (e.g. `munich.boundary.geojson`) of named areas can be downloaded from
[boundary.now](https://haoliangyu.github.io/boundary.now/).

### Fetch tiles for a bbox area

~~~
$ wms-tile-get -s by_wms.json \
               -b 11.43,48.11,11.63,48.26 \
               -z 10 \
               -o by_dop80c
~~~

  * `-b` defines bounding box with longitudes and latitudes coordinates (i.e. EPSG:4326)

A bbox can be calculated [online](https://tools.geofabrik.de/calc/).

### More example

fetch tiles for zoom level 1 to 5, and 10 and 13.
All tiles will be fetched again when the tiles already exist in the output folder.

~~~
$ wms-tile-get -s by_wms.json \
               -g munich.boundary.geojson \
               -z 1-5 10 13  \
               -o by_dop80c  \
               --force
~~~

  * `--force` re-fetch a map tile even it already exists in the output folder

## Requirement:

 - Python3
   - requests
   - [supermercado](https://github.com/mapbox/supermercado)
   - [mercantile](https://github.com/mapbox/mercantile)


## Extra example

We can also only generate tile information with [x, y, z, minx, miny, maxx, maxy] tuples representing WMTS tile id and bbox.

~~~
$ cat munich.boundary.geojson       \
     | supermercado burn 10         \
     | mercantile shapes --mercator \
     | jq -c -r '[ [.id[1:-1]|split(",")|.[]|tonumber], .bbox ] | flatten | join(",")' \
     > munich.tiles.bbox.z10.txt
~~~

The result `munich.tiles.bbox.z10.txt` looks like:

~~~
544,354,10,1252344.2714243277,6144314.081675607,1291480.0299063378,6183449.840157617
545,354,10,1291480.0299063378,6144314.081675607,1330615.7883883482,6183449.840157617
544,355,10,1252344.2714243277,6105178.323193597,1291480.0299063378,6144314.081675607
545,355,10,1291480.0299063378,6105178.323193597,1330615.7883883482,6144314.081675607
~~~

and then we can fetch tiles with such tile information.

~~~
$ wms-tile-get -s by_wms.json \
               -t munich.tiles.bbox.z10.txt \
               -o by_dop80c
~~~

  * `-t` defines tile information input file.

## WMS server definition

A WMS server definition consists mainly `url` and `parameter` which is appended to `url` as HTTP GET method parameters.

Example: `example/by_wms.json`

~~~
{
  "url": "https://geoservices.bayern.de/wms/v2/ogc_dop80_oa.cgi",
  "parameter": {
    "service": "WMS",
    "request": "GetMap",
    "layers": "by_dop80c",
    "styles": "",
    "format": "image/png",
    "transparent": true,
    "version": "1.1.1",
    "width": 256,
    "height": 256,
    "srs": "EPSG:3857",
  },
  "concurrency": 8
}
~~~

Note:

  * The actual parameter `bbox` of a WMS request will be determined automatically.

Additional options:

  * `concurrency`: the maximal number of parallel requests to the WMS server
