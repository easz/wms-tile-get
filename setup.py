from codecs import open as codecs_open
from setuptools import setup, find_packages

with codecs_open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='wms-tile-get',
    version='0.3',
    packages=find_packages(exclude=["ez_setup", "example", "test"]),
    description='Fetch map from WMS server and store them as tiled web map with Slippy Map or or Google Map convention',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/easz/wms-tile-get',
    install_requires=[
          'requests', 'supermercado', 'mercantile'
    ],
    entry_points={
    'console_scripts': [
        'wms-tile-get=scripts.wms_tile_get:main',
    ],
},
    license='MIT'
)
