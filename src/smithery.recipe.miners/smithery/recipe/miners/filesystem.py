
from __future__ import with_statement

from csv import DictReader
from os import listdir
from os.path import isdir, join

from .base import Miner

#
# generic helper functions
#

def listdir2(path):
    """Enhances os.listdir by telling folders from files
    
    Returns a 2-tuple containg a set of the folders and a set of the files present in path"""
    found_names = set(listdir(path))
    found_folders = set(d for d in found_names if isdir(join(path, d)))
    found_files = found_names - found_folders
    return found_folders, found_files


#
# recipes
#

class Namespace(Miner):
    def install(self):
        return tuple()


class File(Miner):
    def install(self):
        return tuple()


class Folder(Miner):
    def install(self):
        return tuple()


class Csv(File):
    def install(self):
        with open(self.options['source']) as csv:
            records = [r for r in DictReader(csv)]
        namespace_key = self.options.get('namespace-key', self.name)
        self.buildout.namespace[namespace_key] = {'records': records}
        return tuple()
