#! /usr/bin/env python
#*-*- coding: utf8

import sys

def make_link(link):
    '''
    mysql-cluster-program-options-mysqld.html
    mysql-cluster-status-variables.html
    performance-schema-status-variables.html
    server-status-variables.html
    '''
    page, anchor = link.split("#")
    suffix = ""
    if page == "server-status-variables.html":
        suffix = ""
    elif page == "mysql-cluster-status-variables.html" or page == "mysql-cluster-program-options-mysqld.html":
        suffix = "../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md"
    elif page == "performance-schema-status-variables.html":
        suffix = "../Chapter_21/21.13.00_Performance_Schema_Status_Variables.md"
        
    return suffix + "#" + anchor
    
def code_it(code):
    ''' '''
    return "`" + code + "`"
    
def make_scope(scope):
    '''make markdown format scope'''
    scopes = scope.split("|")
    if len(scopes) == 1:
        return code_it(scopes[0])
    elif len(scopes) ==2: 
        return code_it(scopes[0]) + " | " + code_it(scopes[1])

def handle(line):
    ''' '''
    link, name, status_type, scope = line.split("$$$")
    mdlink = make_link(link)
    mdscope = make_scope(scope.strip())
    print "[" + name + "](" + mdlink + ") | " + status_type + " | " + mdscope
    
if __name__ == "__main__":
    f = open(sys.argv[1])
    print "变量名 | 变量类型 | 变量范围"
    print "-------|-------|:-------:"  
    lines = f.readlines()
    for line in lines:
        handle(line)
    f.close()