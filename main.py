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
    filename = "alice.txt"
    given_text = read_file(filename) # init text
    print "Text Analyzer"
    print "-------------"
    help = \
    "Commands:\n" \
    + "\trand NUMBER   : Randomly pick a word given times.\n" \
    + "\tread FILENAME : Read a given file.\n" \
    + "\tstats         : Show stats of recently read text.\n" \
    + "\thelp          : Show this.\n" \
    + "\texit          : Exit.\n"
    print help
    print "Current Text: ", filename
    print ""
    word_dict = analyze(given_text)
    while 1:
        input = raw_input("["+filename+"]> ")
        cmd_list = input.split(" ")
        if cmd_list[0] == "exit":
            exit()
        elif cmd_list[0] == "help":
            print help
        elif cmd_list[0] == "rand":
            if len(cmd_list) == 1:
                print "Give me how many times you pick."
                continue
            times = int(cmd_list[1])
            print "Number of words: %.f" % get_num_of_words(given_text)
            print
            pick_rand(given_text, times)
        elif cmd_list[0] == "read":
            if len(cmd_list) == 1:
                print "Give me a filename."
                continue
            filename = cmd_list[1]
            given_text = read_file(filename)
        elif cmd_list[0] == "stats":
            word_dict = analyze(given_text)
            print "Number of words: %.f" % get_num_of_words(given_text)
            print
            show_dict(word_dict)
        elif cmd_list[0] == "":
            continue
        else:
            print "Unknown command: " + cmd_list[0]

def get_num_of_words(given_text):
    return len(get_word_list(given_text))

def pick_rand(given_text, times):
    word_list = get_word_list(given_text)
    num_of_words = len(word_list)
    i = 0
    word_dict = dict()
    while i < times:
        rand = random.random()*num_of_words
        index = int(math.floor(rand))
        word = word_list[index]
        if not word:
            continue
        word = word.lower()
        word_dict[word] = word_dict.get(word, 0) + 1
        i += 1
    word_dict = [(v,k) for k,v in word_dict.items()]
    word_dict.sort()
    word_dict.reverse()
    show_dict(word_dict)
    return

def get_dict_length(word_dict):
    num_of_words = 0.0
    for count,word in word_dict:
        num_of_words += count
    return num_of_words

def show_dict(word_dict):
    num_of_words = get_dict_length(word_dict)
    print "TOP 10 - MOST FRQUENTLY USED WORDS"
    print "COUNT\t|\tWORD\t|\tPROB [%]\t"
    for count, word in word_dict[:10]:
        print count, "\t|\t", word, "\t|\t", "%.2f" %  (count / num_of_words*100)
    print

def get_word_list(text):
    p = re.compile(r'\W+')
    return  p.split(text)

def analyze(given_text):
    word_list = get_word_list(given_text)
    word_dict = dict()
    num_of_words = 0.0
    for word in word_list:
        if not word:
            continue
        word = word.lower()
        word_dict[word] = word_dict.get(word, 0) + 1
        num_of_words += 1.0
    # sort by count
    word_dict = [(v,k) for k,v in word_dict.items()]
    word_dict.sort()
    word_dict.reverse()
    return word_dict

if __name__ == "__main__":
    argv_len = len(sys.argv)
    if not argv_len == 1:
        print "Usage: python text-analyzer.py"
        exit()
    prompt()
