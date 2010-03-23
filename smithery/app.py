
from sys import argv
from optparse import OptionParser

from zc.buildout.buildout import Buildout


class Smithery(Buildout):
    def __init__(self, config_file, options, **keys):
        # hijack the zc.buildout command line option API
        # in order to change the Buildout class defaults
        # without being too invasive
        options = [
            ('buildout', 'parts', 'smithery'), 
            ('smithery', 'recipe', 'smithery.worker'), 
        ] + options
        Buildout.__init__(self, config_file, options, **keys)

    run = Buildout.install


def main(args=argv[1:]):
    parser = OptionParser()
    parser.add_option("-c", "--config-file", default='smithery.cfg',
        help="read configuration from CONFIG_FILE")
    (keys, args) = parser.parse_args()
    app = Smithery(keys.config_file, [])
    app.run(args)
