Title: Install apiary
Slug: apiary_setup  
Summary:  Install apiary
Date: 2017-02-20 12:00    
Category: api
Tags: apiary, install    
Authors: Samira Ouaaz   


sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT

sudo iptables -A INPUT -p tcp --dport 8000 -j ACCEPT

sudo iptables -L

sudo /sbin/service iptables save

sudo systemctl  iptables save

sudo systemctl  save iptables

sudo systemctl iptables --help

mkdir  /home/samira/scripts

vi  /home/samira/scripts/iptables_setup.bash


curl http://10.10.1.239:8889/cwebs/version/

ls /venv/
source  /venv/web/bin/activate
python --version
sudo yum install nodejs
sudo yum groupinstall 'Development tools'
node --version
npm --version
npm install -g dredd
sudo npm install -g dredd
  

sudo npm install -g dredd
dredd

mkdir api
cd api
vi api-description.api

cd ../
mkdir mock-server

cd mock-server/

npm init

npm install express --save
vi app.js
node app.js &

cd ../api
dredd api-description.api http://localhost:3000
sudo pip install dredd_hooks

git clone https://github.com/souaaz/api_docs.git

ls api_docs/
cd api_docs/

dredd cwebsapi.apib 
dredd cwebsapi.apib 10.10.1.239:8889

dredd init -r apiary -j apiaryApiKey:6eca297aa71694be27952ed2e8b2dad5 -j apiaryApiName:cwebsapi

