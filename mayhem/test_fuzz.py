#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from json2html import *

def testOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    num = fdp.ConsumeIntInRange(0, 1)

    if num == 0:
        in_str_1 = fdp.ConsumeUnicodeNoSurrogates(1024)
        json2html.convert(json=in_str_1)
    if num == 1:
        in_str_1 = fdp.ConsumeUnicodeNoSurrogates(1024)
        in_str_2 = fdp.ConsumeUnicodeNoSurrogates(1024)
        json2html.convert(json=in_str_1, table_attributes=in_str_2)
        
def main():
    atheris.Setup(sys.argv, testOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()