#!/bin/sh
python ~/bin/learn-ruby-goto-file.py > /var/tmp/learn-ruby.target
emacs `cat /var/tmp/learn-ruby.target`
