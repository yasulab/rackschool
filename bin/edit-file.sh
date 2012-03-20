#!/bin/sh
export PATH_TO_TARGET="$RACKSCHOOL/usr/$RACKUSER/tmp/"
python $RACKSCHOOL/bin/edit-file.py $PATH_TO_TARGET/check-score.tmp  > $PATH_TO_TARGET/check-score.target
#echo $PATH_TO_TARGET
emacs `cat $PATH_TO_TARGET/check-score.target`
