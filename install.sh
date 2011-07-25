#!/bin/sh
if [ "`whoami`" != "root" ]
then
    echo "Installer works only from root account."
    exit
fi

originalDir=`pwd`
echo "Preparing X-Session Manager in Python to be installed..."
echo "Checking dependencies..."

# install alang-py (dependency required)
if [ ! -f "/usr/share/alang/python/alang.py" ]
then
    echo "Alang-py not found, installing..."
    mkdir /tmp/alang
    cd /tmp/alang
    git clone git://github.com/webnull/alang-py.git
    ./install.sh
    cd "$originalDir"
    rm -rf /tmp/alang
    if [ -f "/usr/share/alang/python/alang.py" ]
    then
        echo -n " [OK]"
    else
        echo -n " [FAILED]\nInstallation failed, are you root?"
    fi
fi

# install optional dependency if user will agree
if [ -e "/usr/lib/libpybootutils" ]
then
    echo "Libpybootutils already installed."
else
    echo "Libpybootutils package is required for kexec feature, do you want to install it? [y/n]: "
    read option

    if [ "$option" == "y" ]
    then
        echo "Downloading libpybootutils..."
        mkdir /tmp/libpybootutils
        cd /tmp/libpybootutils
        git clone git://github.com/webnull/libpybootutils.git
        cd libpybootutils
        chmod +x setup.py
        ./setup.py
        cd /tmp
        rm -rf /tmp/libpybootutils
        echo -n " [DONE]"
    fi
fi 

echo "Dependencies check finished."
echo "Copying XSM files..."

chmod +x usr/bin/* # make all scripts executable
echo "Copying binaries..."
cp usr/bin/* /usr/bin/ # copy binary files
echo "Copying icons, and locales..."
cp usr/share/* /usr/share -r # copy language files, icons
echo "Creating system groups..."
groupadd xsmpy
echo "Adding entry to /etc/sudoers..."
echo "%xsmpy ALL(root) NOPASSWD: /usr/bin/xsm-exit" >> /etc/sudoers
echo "Please assign users to xsmpy group to allow them using xsm."

if [ -f /usr/bin/xsm-exit ]
then
    echo "X-Session Manager Python installed on your system."
else
    echo "Something went wrong, XSM wasnt installed correctly. Are you root?"
fi
