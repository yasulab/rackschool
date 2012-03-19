#!/bin/sh
python $RACKSCHOOL/bin/learn-ruby-goto-file.py $RACKSCHOOL/tmp/learn-ruby.tmp  > $RACKSCHOOL/tmp/learn-ruby.target
emacs `cat $RACKSCHOOL/tmp/learn-ruby.target`
