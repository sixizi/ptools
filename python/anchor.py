#! /usr/bin/env python

import sys

def handle(line):
    ''''''
    line = line.split("]")[0].split("[")[1] #line.strip("*").strip()
    #return "* [{0}](#{0})<a> name='{0}' id='{0}'</a>  ".format(line)
    an = "statvar_" + line
    return "* <a name='{0}' href='#{0}'>{1}</a>  ".format(an, line)
    
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
