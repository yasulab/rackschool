#!/bin/sh
export RACKSCHOOL=$PWD
export RACKUSER=$RHB_USERNAME
echo "export RACKSCHOOL=$PWD" >> ~/.bashrc
echo "export RACKSCHOOL=$PWD" >> ~/.zshrc
echo "export RACKUSER=$RHB_USERNAME" >> ~/.bashrc
echo "export RACKUSER=$RHB_USERNAME" >> ~/.zshrc

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
echo ""

echo "#!/bin/sh" > $RACKSCHOOL/run
echo "sh $RACKSCHOOL/bin/create-account.sh \$RACKUSER" >> $RACKSCHOOL/run
echo "python $RACKSCHOOL/bin/shell.py" >> $RACKSCHOOL/run
echo "python $RACKSCHOOL/bin/publish.py" >> $RACKSCHOOL/run

chmod a+x run
