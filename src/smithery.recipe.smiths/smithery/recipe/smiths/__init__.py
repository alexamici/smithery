"""
Smiths are recipes that process and publish data and metadata
gathered by the miners into the common namespace.
"""

from .base import TemplateMixin, Cheetah, Chameleon, mkdir_p
from .xpath import XPath

__all__ = ('TemplateMixin', 'Cheetah', 'Chameleon', 
    'mkdir_p')
