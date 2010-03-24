
import sys

class Worker(object):
    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

    def collect_sources(self):
        sources = [tok.split(':') for tok in self.options['sources'].split()]
        for source in sources:
            module_name, callable_name, args = source[:2] + [source[2:]]
            # The object returned by the following is the first level module, not
            # the requested one. This looks like a bug in the python standard library.
            module = __import__(module_name)
            # easy work-around
            module = sys.modules[module_name]
            callable = getattr(module, callable_name)
            callable(*args)
        return {}

    def make_targets(self):
        pass

    def install(self):
        self.collect_sources()
        self.make_targets()
        return ()
