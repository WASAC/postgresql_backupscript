import argparse
import subprocess
import datetime


def create_argument_parser():
    """
     Create the parameters for the script
    """
    parser = argparse.ArgumentParser(
        description="Create a QField datasets from PostGIS database.",
        epilog="Example usage: python postgis2qfield.py -d yourdatabase -H localhost - p 5432 "
               "-u user -w securePassword -l list_of_distID(seperated by comma)"
    )
    parser.add_argument("-d", "--database", dest="database",
                        type=str, required=True,
                        help="The database to connect to")

    # Python doesn't let you use -h as an option for some reason
    parser.add_argument("-H", "--host", dest="host",
                        default="localhost", type=str,
                        help="Database host. Defaults to 'localhost'")

    parser.add_argument("-p", "--port", dest="port",
                        default="5432", type=str,
                        help="Password for the database user")

    parser.add_argument("-u", "--user", dest="user",
                        default="postgres", type=str,
                        help="Database user. Defaults to 'postgres'")

    parser.add_argument("-f", "--directory", dest="directory",
                        type=str, required=True,
                        default="C:\postgis_backups",
                        help="Directory path for backup file")

    parser.add_argument("-t", "--target", dest="target",
                        type=str, required=True,
                        choices=['minimum', 'all'],
                        default="all",
                        help="It backup all the dat when all was selected. It only backup specific tables when minimum was selected.")

    return parser.parse_args()


def backup(args):
    now = datetime.datetime.now()
    cur_datetime = '{0:%Y%m%d_%H%M%S}'.format(now)
    backup_filename = "{0}\{1}_{2}_{3}.backup".format(args.directory, cur_datetime, args.database, args.target)

    cmd = "pg_dump.exe --host {0} --port {1} --username {2} -w --format custom --encoding UTF8 ".format(args.host, args.port, args.user)
    if args.target == "minimum":
        tables = ["chamber", "management", "pipeline", "private_operator", "pumping_station",
                  "reservoir", "water_connection", "waterfacilities", "watersource", "wss", "status"]
        for t in tables:
            cmd += " -t {0} ".format(t)
    cmd += "--file {0} {1}".format(backup_filename, args.database)
    subprocess.call(cmd.split())


if __name__ == "__main__":
    params = create_argument_parser()
    backup(params)
