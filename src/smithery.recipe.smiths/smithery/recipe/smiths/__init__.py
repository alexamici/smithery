
from os.path import dirname, realpath

from chameleon.zpt.template import PageTemplateFile
from Cheetah.Template import Template

__here__ = realpath(dirname(__file__))

class Cheetah(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        namespaces = [{'options': self.options}]
        try:
            namespaces[0:0] = [self.buildout.namespace]
        except AttributeError:
            pass
        template = Template.compile(file=self.options['template'])
        with file(self.options['target'], 'w') as outfile:
            outfile.write(str(template(namespaces=namespaces)))
        return tuple()


class Chameleon(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        template = PageTemplateFile(self.options['template'])
        with file(self.options['target'], 'w') as outfile:
            outfile.write(str(template(**self.buildout.namespace)))
        return tuple()
