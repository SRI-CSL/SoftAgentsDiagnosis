""" Entry points into the antlr4 parser.
"""
from __future__ import print_function

from antlr4 import FileStream, InputStream, CommonTokenStream

from ..antlr.DeviationLexer import DeviationLexer

from ..antlr.DeviationParser import DeviationParser

from .Visitor import Visitor

def parseFromFile(events, filename):
    return parseFromStream(events, FileStream(filename), filename)

def parseFromString(events, string):
    return parseFromStream(events, InputStream(string), "stdin")

def parseFromStream(events, stream, source):
    lexer = DeviationLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = DeviationParser(stream)
    tree = parser.unit()
    visitor = Visitor(events, source)
    return visitor.visitUnit(tree)

# we use the same grammar for parsing configurations

def configurationFromFile(filename):
    return configurationFromStream(FileStream(filename), filename)

def configurationFromString(string):
    return configurationFromStream(InputStream(string), "stdin")

def configurationFromStream(stream, source):
    lexer = DeviationLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = DeviationParser(stream)
    tree = parser.configuration()
    visitor = Visitor(None, source)
    return visitor.visitConfiguration(tree)
