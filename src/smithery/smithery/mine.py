
from os import stat

def default(namespace, options):
    ns = {}
    ns['filepath'] = options['args'].split()[0]
    return ns

def raster(namespace, *args):
    return {}

def file(namespace, *args):
    return {'stat:': stat(namespace['filepath'])}
