
import sys


class Worker(object):
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        try:
            self.buildout.namespace
        except AttributeError:
            self.buildout.namespace = {}

    def install(self):
        return ()
