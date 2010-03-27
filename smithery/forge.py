
from pprint import pprint

from Cheetah.Template import Template


def cheetah(namespace, templatepath, outpath=None):
    template = Template.compile(file=templatepath)
    with file(outpath or namespace['outpath'], 'w') as outfile:
        outfile.write(str(template()))

def display(namespace, *args):
    pprint(namespace)
