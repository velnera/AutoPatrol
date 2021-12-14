from __future__ import print_function


from dronekit import connect, Command
import time


#Set up option parsing to get connection string
import argparse  
parser = argparse.ArgumentParser(description='Demonstrates mission import/export from a file.')
parser.add_argument('--connect', 
                   help="Vehicle connection target string. If not specified, SITL automatically started and used.")
parser.add_argument('--mission_file', 
                   help="Mission file to upload.")

args = parser.parse_args()

connection_string = args.connect
mission_file = args.mission_file
#sitl = None


#Start SITL if no connection string specified
#if not connection_string:
#    import dronekit_sitl
#    sitl = dronekit_sitl.start_default()
#    connection_string = sitl.connection_string()


# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True, timeout=120, heartbeat_timeout=120)
vehicle.close()