
from os.path import dirname, realpath

from chameleon.zpt.template import PageTemplateFile
from Cheetah.Template import Template

__here__ = realpath(dirname(__file__))

class TemplateMixin(object):

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        try:
            self.namespace = self.buildout.namespace
        except AttributeError:
            self.namespace = {}

    def _render(self, template):
        """Sub-classes must implement own _render"""
        raise NotImplementedError

    def render(self, template=None):
        if template is None:
            template = self.options['template']
        return self._render(template)

    def render_to_target(self, target=None, **keys):
        if target is None:
            target = self.options['target']
        rendered = self.render(**keys)
        with file(target, 'w') as outfile:
            outfile.write(rendered)
        return target

    def install(self):
        target = self.render_to_target()
        return tuple(target)


class Cheetah(TemplateMixin):

    def _render(self, template):
        namespaces = [self.namespace, {'options': self.options}]
        template_obj = Template.compile(file=template)
        return str(template_obj(namespaces=namespaces))


class Chameleon(TemplateMixin):

    def _render(self, template):
        template_obj = PageTemplateFile(template)
        return str(template_obj(**self.namespace))
