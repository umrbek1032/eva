"""
    It installs the packages in the list packages
    
    :param package: The name of the package you want to install
"""
from  os import popen
def install(package):
    popen('pip3 install ' + package).read()
popen('py -m pip install --upgrade pip').read()
packages=['opencv-python==4.6.0.66','Pillow==9.1.1','sounddevice==0.4.4','PyAutoGUI==0.9.53','wavio==0.0.4','requests==2.28.0','numpy==1.23.0','pyTelegramBotAPI','psutil==5.9.1']
for package in packages:
    try:
        install(package)
    except:
        pass
