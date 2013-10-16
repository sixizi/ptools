#! /usr/bin/env python
#*-*- coding: utf8

import sys

def make_link(link):
    '''
     145 server-system-variables.html
       75 innodb-parameters.html
       23 server-options.html
       22 replication-options-slave.html
       19 mysql-cluster-system-variables.html
       13 replication-options-binary-log.html
        6 mysql-cluster-program-options-mysqld.html
        5 validate-password-plugin.html
        3 audit-log-plugin-options-variables.html
        2 replication-options-master.html
        2 replication-options-gtids.html
        2 mysql-cluster-replication-conflict-resolution.html
        1 replication-options.html
    '''

    page, anchor = link.split("#")
    suffix = ""
    if page == "server-system-variables.html":
        suffix = ""
    elif page == "innodb-parameters.html":
        suffix = "../Chapter_14/14.02.06_InnoDB_Startup_Options_and_System_Variables.md"
    elif page == "server-options.html":
        suffix = "./05.01.03_Server_Command_Options.md"
    elif page in ("replication-options-slave.html", "replication-options-binary-log.html", "replication-options-master.html", "replication-options-gtids.html", "replication-options.html"):
        suffix = "../Chapter_16/16.01.04_Replication_and_Binary_Logging_Options_and_Variables.md"
    elif page == "mysql-cluster-system-variables.html" or page == "mysql-cluster-program-options-mysqld.html":
        suffix = "../Chapter_17/17.03.04_MySQL_Server_Options_and_Variables_for_MySQL_Cluster.md"
    elif page == "validate-password-plugin.html":
        suffix = "../Chapter_06/06.01.02_Keeping_Passwords_Secure.md"
    elif page == "audit-log-plugin-options-variables.html":
        suffix = "../Chapter_06/06.03.11_MySQL_Enterprise_Audit_Log_Plugin.md"
    elif page == "mysql-cluster-replication-conflict-resolution.html":
        suffix = "../Chapter_17/17.06.11_MySQL_Cluster_Replication_Conflict_Resolution.md"
    suffix = suffix.replace("|", "&#124;")
    return suffix + "#" + anchor
    
def code_it(code):
    ''' '''
    return "`" + code.strip() + "`"
    
def make_scope(scope):
    '''make markdown format scope'''
    scopes = scope.split("|")
    if len(scopes) == 1:
        return code_it(scopes[0])
    elif len(scopes) ==2: 
        return code_it(scopes[0]) + " &#124; " + code_it(scopes[1])

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
