# wms-tile-get

Fetch map tiles from WMS server and store them with
[WMTS](https://en.wikipedia.org/wiki/Web_Map_Tile_Service) convention.
Typically the resulting tiles should be with EPSG:3857 projection.

The tool is similar to many others like [wms-tiles-downloader](https://github.com/Luqqk/wms-tiles-downloader)
but accept also geojson polygon as an area of interest.

## Install

~~~
$ pip install wms-tile-get
~~~

## Usage

### Fetch tiles for an area (e.g. a city)

~~~

$ cd example/

$ wms-tile-get -s by_wms.json \
               -g munich.boundary.geojson \
               -z 10 \
               -o by_dop80c
~~~

  `-s` defines WMS server parameters.
  `-g` defines the area(s) of interest (polygon area in geojson).
  `-z` defines the zoom level(s) of interest.
  `-o` defines output folder.

An area or boundary shapes (e.g. `munich.boundary.geojson`) of named areas can be downloaded from
[boundary.now](https://haoliangyu.github.io/boundary.now/).

### Fetch tiles for a bbox area

~~~
$ wms-tile-get -s by_wms.json \
               -b 11.43,48.11,11.63,48.26 \
               -z 10 \
               -o by_dop80c
~~~

  `-b` defines bounding box with longitudes and latitudes coordinates (i.e. EPSG:4326)

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


## Requirement:

 - Python
   - requests
   - [supermercado](https://github.com/mapbox/supermercado)
   - [mercantile](https://github.com/mapbox/mercantile)


## Extra example

We can also only generate tile information with [x, y, z, minx, miny, maxx, maxy] tuples representing WMTS tile id and bbox.

~~~
$ cat munich.boundary.geojson       \
     | supermercado burn 18         \
     | mercantile shapes --mercator \
     | jq -c -r '[ [.id[1:-1]|split(",")|.[]|tonumber], .bbox ] | flatten | join(" ")' \
     > munich.tiles.bbox.z18.txt
~~~

The result `munich.tiles.bbox.z18.txt` looks like:

~~~
139445,90854,18,1280014.4756635614,6148135.933089867,1280167.3497201318,6148288.807146437
139446,90854,18,1280167.3497201318,6148135.933089867,1280320.223776702,6148288.807146437
139447,90854,18,1280320.223776702,6148135.933089867,1280473.0978332725,6148288.807146437
139448,90854,18,1280473.0978332725,6148135.933089867,1280625.971889843,6148288.807146437
139449,90854,18,1280625.971889843,6148135.933089867,1280778.8459464132,6148288.807146437
...
~~~

and then we can fetch tiles with such tile information.

~~~
$ wms-tile-get -s by_wms.json \
               -t munich.tiles.bbox.z10.txt \
               -o by_dop80c
~~~

  `-t` defines tile information input file.


