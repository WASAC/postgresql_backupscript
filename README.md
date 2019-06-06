# Python Script of backup PostgreSQL

## backup_postgresql.py

A simple tool for backuping from a PostGIS table to create PostgreSQL backup file.

The tool was designed for RWSS department of WASAC in Rwanda.

####Example usage:

To backup:

````
python backup_postgresql.py -d your_database -H localhost -P 5432 -u postgres -f [directory path] -t [minimum/all]
````

For Windows OS, you can use the following two .bat files for backup. Of course, you need to change database settings.
````
run_backup_all.bat
run_backup_minimum.bat
````

Before running the script, please must specify directory path(-f option) for saving backup file and target of backup(-t option).
If you select "all", it will backup the entire database.
If you select "minimum", it will backup the following tables.

````
chamber
management
pipeline
private_operator
pumping_station,
reservoir
water_connection
waterfacilities
watersource
wss
status
````

####Setting of PostgreSQL password for your server:
It cannot give password of database to pg_dump command directly, so kindly do setting of pgpass file.

````.pgpass```` (in Linux) and ````pgpass.conf```` (in Windows)
````
hostname:port:database:username:password
````

In Linux, ````.pgpass```` should be under home directory,
In Windows, ````pgpass.conf```` should be under ````%APPDATA%\postgresql````

####Settings of Task Scheduler:
This backup scripts can be used in task scheduler in your OS.
In Windows, there is the function which is called "Task Scheduler".
In Linux, you can use "crontab" to schedule of backup. You may create Shell script.
````
$ crontab -e
--if you want to backup minimum at 8 am every day, you can do like below.
00 08 * * * python backup_postgresql.py -d your_database -H localhost -P 5432 -u postgres -f G:\postgis_backups -t minimum
--if you want to backup fully on 1st day every month, you can do like below.
00 16 1 * * python backup_postgresql.py -d your_database -H localhost -P 5432 -u postgres -f G:\postgis_backups -t all
````

####About
This script was developed by ````Jin IGARASHI, JICA Expert```` from ````The Project for Strengthening Operation and Maintenance of Rural Water Supply Systems in Rwanda- RWASOM````.