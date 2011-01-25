"""
Smiths are recipes that process and publish data and metadata
gathered by the miners into the common namespace.
"""

from __future__ import with_statement

# we have quite a few options for the etree interfacae
try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")


from .base import TemplateMixin


class XPath(TemplateMixin):
    """Simple smith that process an XML template with xpath."""

    def do_render(self, template, namespace):
        rule_section = self.buildout[self.options.get('rules', 'xpath_rules')]
        data = self.namespace[self.options.get('namespace-key', 'data')]
        tree = etree.parse(open(template))
        print data['records']
        for option, value in rule_section.items():
            for tag in tree.xpath(option):
                tag.text = data['records'][0][value]
        return etree.tostring(tree)
