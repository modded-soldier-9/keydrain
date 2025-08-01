"""
Code generation modules for the malware builder.
"""

from .source_generator import SourceGenerator
from .polymorphism import PolymorphismEngine

__all__ = ['SourceGenerator', 'PolymorphismEngine'] 