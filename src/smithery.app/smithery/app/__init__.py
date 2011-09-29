# Copyright statement
# -------------------
# 
# Copyright (c) 2011 e-GEOS SpA. All rights reserved.
# Copyright (c) 2011 B-Open Solutions srl. All rights reserved.
# Copyright (c) 2010-2011 Alessandro Amici. All rights reserved.
# 
# This software is subject to the provisions of the Zope Public License, 
# Version 2.1 (ZPL). A copy of the ZPL should accompany this distribution. 
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED 
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS 
# FOR A PARTICULAR PURPOSE.

import logging
from logging.handlers import SMTPHandler
from optparse import OptionParser
from sys import argv

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
        smithery_options = [
            ('smithery', 'log-file', ''),
            ('smithery', 'log-format', '%(asctime)s %(levelname)s %(message)s'),
            ('smithery', 'log-level', 'INFO'),
            ('smithery', 'log-no-stdout', 'false'),
            ('smithery', 'log-email-server', 'localhost:25'),
            ('smithery', 'log-email-alerts-to', ''),
        ]
        for section, k, v in smithery_options:
            if not self[section].has_key(k):
                self[section][k] = v
        self.config_logging()

    run = Buildout.install


    def config_logging(self):
        root_logger = logging.getLogger()
        level = self['smithery']['log-level']
        if level in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
            level = getattr(logging, level)
        else:
            try:
                level = int(level)
            except ValueError:
                raise ValueError("Invalid logging level: %r" % level)
        root_logger.setLevel(level)
        if self['smithery']['log-file']:
            handler = logging.FileHandler(self['smithery']['log-file'])
            formatter = logging.Formatter(self['smithery']['log-format'])
            handler.setFormatter(formatter)
            handler.setLevel(level)
            root_logger.addHandler(handler)
        if self['smithery']['log-no-stdout'] == 'true':
            streams = filter(lambda h: h.__class__ == logging.StreamHandler, root_logger.handlers)
            for stream in streams:
                root_logger.removeHandler(stream)
        if self['smithery']['log-email-alerts-to']:
            server = tuple(self['smithery']['log-email-server'].strip().split(':'))
            from_address = 'no-reply@example.com'
            subject = 'Error message'
            alerts_to = self['smithery']['log-email-alerts-to'].split()
            handler = SMTPHandler(server, from_address, alerts_to, subject)
            handler.setLevel(logging.ERROR)
            root_logger.addHandler(handler)

def main(args=argv[1:]):
    parser = OptionParser()
    parser.add_option("-c", "--config-file", default='smithery.cfg',
        help="read configuration from CONFIG_FILE")
    (keys, args) = parser.parse_args()
    app = Smithery(keys.config_file, [], args=args)
    app.run([])
