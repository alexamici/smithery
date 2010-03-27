
import sys


class Worker(object):
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.namespace = {}

    def collect_sources(self):
        sources = self.options['sources'].split()
        [self.buildout[source]['recipe'] for source in sources]
        return
        sources = [['smithery.mine', 'default', self.options]]
        sources += [tok.split(':') for tok in self.options['sources'].split()]
        for source in sources:
            module_name, callable_name, args = source[:2] + [source[2:]]
            # The object returned by the following is the first level module, not
            # the requested one. This looks like a bug in the python standard library.
            module = __import__(module_name)
            # easy work-around
            module = sys.modules[module_name]
            callable = getattr(module, callable_name)
            extracted_namespace = callable(self.namespace, *args)
            # TODO: this should be some kind of recursive update
            self.namespace.update(extracted_namespace)

    def make_targets(self):
        targets = [tok.split(':') for tok in self.options['targets'].split()]
        for target in targets:
            module_name, callable_name, args = target[:2] + [target[2:]]
            # The object returned by the following is the first level module, not
            # the requested one. This looks like a bug in the python standard library.
            module = __import__(module_name)
            # easy work-around
            module = sys.modules[module_name]
            callable = getattr(module, callable_name)
            callable(self.namespace, *args)

    def install(self):
        self.collect_sources()
        self.make_targets()
        return ()

    def update(self):
        pass
