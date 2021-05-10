from codecs import open as codecs_open
from setuptools import setup, find_packages

with codecs_open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='wms-tile-get',
    version='0.2',
    packages=find_packages(exclude=["ez_setup", "example", "test"]),
    description='Fetch map tiles from WMS server and store them with WMTS convention',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/easz/wms-tile-get',
    install_requires=[
          'requests', 'supermercado', 'mercantile'
    ],
    scripts=['scripts/wms-tile-get'],
    license='MIT'
)
