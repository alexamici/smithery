"""
Geo-miners are recipes that extract data and metadata from geographic resources.
"""

from owslib.wms import WebMapService

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
