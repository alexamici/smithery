
class Miner(object):
    """Base class for smithery miners."""
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        try:
            self.buildout.namespace
        except AttributeError:
            self.buildout.namespace = {}
