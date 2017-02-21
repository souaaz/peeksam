Title: Copy a folder with SCP
Slug: scp_linux    
Summary:  Copy a folder with SCP
Date: 2017-02-20 12:00    
Category: Linux
Tags: copy, scp, ssh
Authors: Samira Ouaaz   



## To move a large number of files using SCP

## SCP using tar (faster)

Tar your files to local.tar

`local$ tar -czvf local.tar directory/ `

Copy the file to the remote location using scp:

`local$ scp local.tar user@remote:/directory`


SSH to the remote location:

`ssh user@remote`


Untar the file:

`remote$ tar -xzvf local.tar`
