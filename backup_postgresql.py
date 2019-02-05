import subprocess
import datetime

host = "localhost"
port = 5432
username = "postgres"
database = "rwss_assets"

def backup():
    now = datetime.datetime.now()
    cur_datetime = '{0:%Y%m%d_%H%M%S}'.format(now)
    backup_filename = "{0}_{1}.backup".format(cur_datetime, database)

    cmd = "pg_dump.exe --host {0} " \
          "--port {1} --username {2} -w --format custom --encoding UTF8 " \
          "-t chamber -t management -t pipeline -t private_operator " \
          "-t pumping_station -t reservoir -t water_connection -t waterfacilities " \
          "-t watersource -t wss " \
          "--file {3} {4}".format(host, port, username, backup_filename, database)
    subprocess.call(cmd.split())

if __name__ == "__main__":
    backup()