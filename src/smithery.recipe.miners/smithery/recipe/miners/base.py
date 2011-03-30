
class Miner(object):
    """Base class for smithery miners."""
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        try:
            self.buildout.namespace
        except AttributeError:
            self.buildout.namespace = {}

    def set_names(self, names, value):
        next = self.buildout.namespace
        for name in names:
            current = next
            if name not in current:
                current[name] = {}
            next = current[name]
        current[names[-1]] = value
