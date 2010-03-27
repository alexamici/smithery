
from Cheetah.Template import Template


class Cheetah(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        Template.compile(file=self.options['template'])
        with file(self.options['target'], 'w') as outfile:
            outfile.write(str(template()))
        return tuple()

    def update(self):
        """Updater"""
        pass


class Chameleon(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here
        
        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.
        return tuple()

    def update(self):
        """Updater"""
        pass
