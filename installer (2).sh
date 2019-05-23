#!/usr/bin/env bash 

# Checking permission
if [ $EUID != 0 ];then
    echo "$(tput setaf 1)error: Permission denied.Run script as root."
    exit 1
fi
echo "$(tput setaf 2)==> Creating directory for radio-qt in /opt ..."
sleep 0.2
echo "$(tput setaf 2)✔"
mkdir /opt/RadioJavan
cp $(pwd) /opt/RadioJavano

echo -e "[Desktop Entry]
Name=Radio Javan
Comment=radio javan qt
Exec=/opt/RadioJavan/radio-qt/radiojavan-qt.py 
Icon=/opt/RadioJavan/radio-qt/icon/icp.png
Type=Application
Categories=Network;RemoteAccess;
StartupNotify=true" > /usr/share/applications/radiojavan.desktop

sleep 0.5 
echo "$(tput setaf 2)==> Creating shortcut to desktop ..."
cp /usr/share/applications/radiojavan.desktop ~/Desktop/Radio-Javan.desktop
echo "$(tput setaf 2)✔ Done "
