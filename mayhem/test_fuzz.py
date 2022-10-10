#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from json2html import *

def testOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    input = fdp.ConsumeUnicodeNoSurrogates(64)
    json2html.convert(json = input)
        
def main():
    atheris.Setup(sys.argv, testOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()