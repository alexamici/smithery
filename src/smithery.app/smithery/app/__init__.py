
from sys import argv
from optparse import OptionParser

# HACK: this is hopefully a temporary hack around what looks like
#    a circular dependency between setuptools/smithery/zc.buildout
try:
    from zc.buildout.buildout import Buildout
except ImportError:
    class Buildout(object):
        def install(self):
            pass


class Smithery(Buildout):
    """
    Tiny wrapper around the zc.buildout Buildout class intended to override
    behaviours specific to building software.
    
    The intent of this class is to only use Buildout powerful cfg parsing and the recipe engine.
    """
    def __init__(self, config_file, options, args=(), **keys):
        # hijack the zc.buildout command line option API
        # in order to change the Buildout class defaults
        # without being too invasive
        options = [
            # disable bootstrap directories and installed parts tracking
            ('buildout', 'installed', ''),
            ('buildout', 'bin-directory', '.'),
            ('buildout', 'eggs-directory', '.'),
            ('buildout', 'develop-eggs-directory', '.'),
            ('buildout', 'parts-directory', '.'),
            ('buildout', 'offline', 'true'),
            # custom default config
            ('buildout', 'parts', '${smithery:parts}'),
            # override args usage
            ('smithery', 'args', ' '.join(args)),
        ] + options
        Buildout.__init__(self, config_file, options, **keys)

    run = Buildout.install


def main(args=argv[1:]):
    parser = OptionParser()
    parser.add_option("-c", "--config-file", default='smithery.cfg',
        help="read configuration from CONFIG_FILE")
    (keys, args) = parser.parse_args()
    app = Smithery(keys.config_file, [], args=args)
    app.run([])
