#! /usr/bin/env python

import sys

def handle(line):
    ''''''
    line = line.strip("*").strip()
    #return "* [{0}](#{0})<a> name='{0}' id='{0}'</a>  ".format(line)
    return "* [{0}](id:statvar_{0})  ".format(line)
    
if __name__ == "__main__":
    fn = sys.argv[1]
    f = open(fn)
    lines = f.readlines()
    for line in lines:
        if line.startswith("*"):
            line = handle(line)
            print line
        else:
            print line.rstrip()
