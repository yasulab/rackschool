#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os


def read_file(filename):
    if os.path.exists(filename) == False:
        print "No such as a file."
        return
    input = open(filename, "r")
    return input

def main(filename):
    read_flg = False
    given_text = read_file(filename)
    for i,line in enumerate(given_text):
        #print line
        if read_flg:
            #print line
            target_text = line
            read_flg = False
        if line.startswith("Please") == True:
            #print "hoge!"
            read_flg = True
    target_path = target_text[6:].strip().split(":")
    print target_path[0]
    #output = open("/var/tmp/learn-ruby-target-file.txt", "w")
    #output.write(target_path[0])
    
            

if __name__ == "__main__":
    argv_len = len(sys.argv)
    if not argv_len == 2:
        print "Usage: ./learn-ruby-goto-file.py FILENAME"
        exit()
    filename = sys.argv[1]        
    main(filename)

