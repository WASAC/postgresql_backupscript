# Python Script of backup PostgreSQL

## backup_postgresql.py

A simple tool for backuping from a PostGIS table to create PostgreSQL backup file.

The tool was designed for RWSS department of WASAC in Rwanda.

####Example usage:

To backup:

````
python backup_postgresql.py
````

Before running the script, kindly check the database settings at ````database```` class on ```` postgis2qfield.py```` .

````
host = "localhost"
port = 5432
username = "postgres"
database = "rwss_assets"
````

It cannot give password of database to pg_dump command directly, so kindly do setting of pgpass file.

````.pgpass```` (in Linux) and ````pgpass.conf```` (in Windows)
````
hostname:port:database:username:password
````

In Linux, ````.pgpass```` should be under home directory,
In Windows, ````pgpass.conf```` should be under ````%APPDATA%\postgresql````

This script was developed by ````Jin IGARASHI, JICA Expert```` from ````The Project for Strengthening Operation and Maintenance of Rural Water Supply Systems in Rwanda- RWASOM````.