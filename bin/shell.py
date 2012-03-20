#!/usr/bin/python
#! -*- coding: utf-8 -*-

import sys
import re
import os
import math, random

def read_file(filename):
    if os.path.exists('./'+filename) == False:
        print "No such as a file."
        return        
    input = open(filename, "r")
    return input.read()        

def prompt():
    print "Learn Ruby"
    print "----------"
    help = \
    "Commands:\n" \
    + "\tcheck[c]: Check your score.\n" \
    + "\tedit[e] : Edit problems.\n" \
    + "\thelp[h] : Show this.\n" \
    + "\texit    : Exit.\n"
    print help
    while 1:
        try:
            input = raw_input("> ")
        except:
            print "exit"
            exit()
        cmd_list = input.split(" ")
        if cmd_list[0] == "check" or cmd_list[0] == "c":
            os.system('./bin/check-score.sh')
            print
        elif cmd_list[0] == "edit" or cmd_list[0] == "e":
            os.system('./bin/edit-file.sh')
            print
        elif cmd_list[0] == "help" or cmd_list[0] == "h":
            print help
        elif cmd_list[0] == "exit":
            exit()
        elif cmd_list[0] == "":
            continue
        else:
            print "Unknown command: " + cmd_list[0]

if __name__ == "__main__":
    argv_len = len(sys.argv)
    if not argv_len == 1:
        print "Usage: python text-analyzer.py"
        exit()
    prompt()
