
from csv import reader


class Namespace(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here
        
        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.
        return tuple()


class File(object):
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


class Folder(object):
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        
        return tuple()

    def update(self):
        """Updater"""
        pass


class Csv(File):
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        with open(self.options['source']) as csv:
            records = [r for r in reader(csv)]
        try:
            self.buildout.namespace
        except AttributeError:
            self.buildout.namespace = {}
        namespace_key = self.options.get('namespace-key', self.name)
        self.buildout.namespace[namespace_key] = {'records': records}
        return tuple()

    def update(self):
        """Updater"""
        pass
