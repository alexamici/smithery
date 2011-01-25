
from __future__ import with_statement

from errno import EEXIST
from os import makedirs

from chameleon.zpt.template import PageTemplateFile
from Cheetah.Template import Template

#
# generic helper functions
#

def mkdir_p(path):
    """Almost equivalent to 'mkdir -p path'"""
    try:
        makedirs(path)
    except OSError, exc:
        if exc.errno != EEXIST:
            raise

#
# recipes
#

class TemplateMixin(object):
    """Base class for template smiths.
    
    Offers standard methods for parsing recipe options."""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        try:
            self.namespace = self.buildout.namespace
        except AttributeError:
            self.namespace = {}

    def do_render(self, template, namespace):
        """Sub-classes must implement own do_render"""
        raise NotImplementedError

    def render(self, template=None, namespace=None):
        if template is None:
            template = self.options['template']
        if namespace is None:
            namespace = self.namespace
        return self.do_render(template, namespace)

    def render_to_target(self, target=None, **keys):
        if target is None:
            target = self.options['target']
        rendered = self.render(**keys)
        with file(target, 'w') as outfile:
            outfile.write(rendered)
        return target

    def install(self):
        """Main entry-point for the zc.buildout recipe API"""
        target = self.render_to_target()
        return tuple(target)


class Cheetah(TemplateMixin):
    """Simple smith based on Cheetah generic template language."""

    def do_render(self, template, namespace):
        namespaces = [namespace, {'options': self.options}]
        template_obj = Template.compile(file=template)
        return template_obj(namespaces=namespaces).encode('utf-8')


class Chameleon(TemplateMixin):
    """Simple smith based on Chameleon XML template language."""

    def do_render(self, template, namespace):
        template_obj = PageTemplateFile(template)
        return template_obj(**namespace).encode('utf-8')


