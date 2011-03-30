"""
Geo-miners are recipes that extract data and metadata from geographic resources.
"""

from os import stat

from owslib.wms import WebMapService
from osgeo.gdal import Open
from osgeo.osr import SpatialReference, CoordinateTransformation

from .base import Miner


class WMS(Miner):
    """Tiny wrapper around OWSLib.wms.WebMapService"""
    default_url = 'http://wms.jpl.nasa.gov/wms.cgi'
    def install(self):
        url = self.options.get('url', self.default_url)
        wms = WebMapService(url)
        if wms.identification.type != 'OGC:WMS':
            raise TypeError('Not a WMS service %r returned %r type' % (url, wms.identification.type))
        print 'WMS from', wms.identification.title
        self.buildout.namespace['wms'] = wms
        return tuple()


class Raster(Miner):
    """Miner for raster geospatial data and imagery based on GDAL"""
    def install(self):
        filepath = self.options.get('filepath', 'image.tif')
        t_srid = self.options.get('t_srid', 'EPSG:4326')
        namespace_key = self.options.get('namespace-key', self.name)

        # stat also tests file existence
        self.set_names((namespace_key, 'fileDimension'), stat(filepath)[7])

        dataset = Open(filepath)
        if dataset is None:
            raise IOError('%r not recognised as a supported file format.' % filepath)

        self.set_names((namespace_key, 'spatialRepresentationInfo', 'column'), dataset.RasterYSize)
        self.set_names((namespace_key, 'spatialRepresentationInfo', 'row'), dataset.RasterXSize)        
        
        print self.buildout.namespace
        return tuple()
