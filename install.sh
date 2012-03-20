#!/bin/sh
export RACKSCHOOL=$PWD
export RACKUSER=$USERNAME

#if [ -d $RACKSCHOOL/usr/$RACKUSER ]
#then
#    echo "'$RACKUSER' already exists.\n"
#    exit 1
#else    
#    sh $RACKSCHOOL/bin/create-account.sh $RACKUSER
#fi

echo "Successfully installed!"
echo "  Installed dir : $RACKSCHOOL"
echo "  Your username : $RACKUSER"
echo "  Your directory: $RACKSCHOOL/usr/$RACKUSER/"
echo "#!/bin/sh" > $RACKSCHOOL/run
echo "sh $RACKSCHOOL/bin/create-account.sh \$RACKUSER" >> $RACKSCHOOL/run
echo "python $RACKSCHOOL/bin/shell.py" >> $RACKSCHOOL/run

chmod a+x run
