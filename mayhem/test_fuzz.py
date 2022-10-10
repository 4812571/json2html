#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from json2html import *

def testOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    json2html.convert(atheris.ConsumeUnicodeNoSurrogates(64))
        
def main():
    atheris.Setup(sys.argv, testOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()