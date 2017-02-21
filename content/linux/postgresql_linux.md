Title: Install POSTGRESQL on Ubuntu
Slug: postgresql_linux    
Summary:  Install POSTGRESQL on Ubuntu
Date: 2017-02-20 12:00    
Category: Linux
Tags: Database, postgresql, install    
Authors: Samira Ouaaz   

This is tutorial to Install POSTGRESQL on Linux 

## INSTALL POSTGRESQL
`sudo apt install postgresql`

Once the installation is complete, you should configure the PostgreSQL server based on your needs, although the default configuration is viable.

## Configuration
PostgreSQL supports multiple client authentication methods. IDENT authentication method is used for postgres and local users, unless otherwise configured. Please refer to the PostgreSQL Administrator's Guide if you would like to configure alternatives like Kerberos.

The following discussion assumes that you wish to enable TCP/IP connections and use the MD5 method for client authentication. PostgreSQLconfiguration files are stored in the /etc/postgresql/<version>/main directory. For example, if you install PostgreSQL 9.1, the configuration files are stored in the /etc/postgresql/9.1/main directory.

To configure ident authentication, add entries to the /etc/postgresql/9.1/main/pg_ident.conf file. There are detailed comments in the file to guide you.

To enable other computers to connect to your PostgreSQL server, edit the file /etc/postgresql/9.1/main/postgresql.conf

Locate the line #listen_addresses = 'localhost' and change it to:

listen_addresses = '*'
To allow both IPv4 and IPv6 connections replace 'localhost' with '::'

You may also edit all other parameters, if you know what you are doing! For details, refer to the configuration file or to the PostgreSQL documentation.

### Password Set up
Now that we can connect to our PostgreSQL server, the next step is to set a password for the postgres user. Run the following command at a terminal prompt to connect to the default PostgreSQL template database:

`sudo -u postgres psql template1`

The above command connects to PostgreSQL database template1 as user postgres. Once you connect to the PostgreSQL server, you will be at a SQL prompt. You can run the following SQL command at the psql prompt to configure the password for the user postgres.

`ALTER USER postgres with encrypted password 'your_password';`

After configuring the password, edit the file /etc/postgresql/9.1/main/pg_hba.conf to use MD5 authentication with the postgres user:

`local   all         postgres                          md5`

Finally, you should restart the PostgreSQL service to initialize the new configuration. From a terminal prompt enter the following to restart PostgreSQL:

`sudo systemctl restart postgresql.service`

The above configuration is not complete by any means. Please refer to the PostgreSQL Administrator's Guide to configure more parameters.

You can test server connections from other machines by using the PostgreSQL client.

`sudo apt install postgresql-client`

`psql -h postgres.example.com -U postgres -W`

Replace the domain name with your actual server domain name.
