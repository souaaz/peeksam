Title: Install Python 3 on Centos 7
Slug: python3_centos7  
Summary:  Install Python 3 on Centos 7
Date: 2017-02-20 12:00    
Category: Linux
Tags: python 3, centos 7, install    
Authors: Samira Ouaaz   


## OPTION 1 - INSTALL through EPEL

The latest EPEL 7 repository offers python3. 

Thus if you are using CentOS 7 or later, you can easily install python3 by enabling EPEL repository as follows.

`$ sudo yum install epel-release`

Then install python 3.4 and its libraries using yum:

`$ sudo yum install python34`

Note that this will not install matching pip.

 To install pip and setuptools, you need to install them separately as follows.

`$ curl -O https://bootstrap.pypa.io/get-pip.py`

`$ sudo /usr/bin/python3.4 get-pip.py`


## OPTION 2 -  INSTALL through SCL

Another way to install python3 is via enabling Software Collections (SCL) repository. The SCL repository is available for CentOS 6.5 or later, and the latest SCL offers python 3.3. Once you enable the SCL repository, go ahead and install python3 as follows.

`$ sudo yum install python33`

To use python3 from the SCL, you need to enable python3 on a per-command basis as follows.

`$ scl enable python33 <command>`


You can also invoke a bash shell with python3 enabled as the default Python interpreter:


