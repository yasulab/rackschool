#!/bin/sh
if [ $# -eq 0 ]
then
    echo "Usage: create-account USERNAME\n"
else
    if [ -d $1 ]
    then
	#exit 1
	#echo "$1 already exists.\n"
	mkdir $RACKSCHOOL/usr/$1
	mkdir $RACKSCHOOL/usr/$1/tmp
	cp -r $RACKSCHOOL/src/learn-ruby $RACKSCHOOL/usr/$1/
	#echo "Successfully created a user '$1'\n"
    else
	exit 1
    fi
fi

