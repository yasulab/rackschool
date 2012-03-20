#!/bin/sh
if [ $# -eq 0 ]
then
    echo "Usage: create-account USERNAME\n"
else
    #cd $RACKSCHOOL
    if [ -d $1 ]
    #if [ ls $1 &> /dev/null ]
    then
	echo "$1 already exists.\n"
    else
	mkdir -p $RACKSCHOOL/usr/$1
	cp -r $RACKSCHOOL/src/learn-ruby $RACKSCHOOL/usr/$1/
	echo "Successfully created a user '$1'\n"
    fi
fi

