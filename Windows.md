# Installation with Pip on Windows Platform

### GDAL

 - Find the [release packages](https://www.gisinternals.com/release.php)
 - Thre are three components necessary
   - Core (e.g. `gdal-302-1916-x64-core.msi`)
   - Python binding (e.g. `GDAL-3.2.2.win-amd64-py3.7.msi`), **otherwise use `pip install GDAL` instead**
   - Compiled libraries and headers (e.g. `release-XXXX-XXX-gdal-XXX-libs.zip`)

After running Core and Pythoin binding installers,
make sure the environment variables are set properly like this:

~~~
GDAL_DATA        -> C:\Program Files\GDAL
GDAL_DRIVER_PATH -> C:\Program Files\GDAL\gdalplugins
GDAL_VERSION     -> 3.2.2
PATH             -> C:\Program Files\GDAL;C:\Program Files\GDAL\gdal-data;...
~~~

### rasterio and etc

`rasterio` can be tricky to install.

 - at first `pip install` all modules required by `rasterio`. A list of requirement can be shown with `pip show rasterio`
 - Follow the [instruction](https://rasterio.readthedocs.io/en/latest/installation.html#installing-from-the-source-distribution) to install `rasterio` from source
  - clone `rasterio` from `https://github.com/mapbox/rasterio` and switch to release tag (e.g. `1.2.3`)
  - `$ python setup.py build_ext -I<path to gdal include files> -lgdal_i -L<path to gdal library> install`

### wms-tile-get

`pip install wms-tile-get`
