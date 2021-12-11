import runpy

import MAX30102
import heartrate_monitor
import hrcalc
from MLX90614 import *
from heartrate_monitor import HeartRateMonitor
import time
import argparse

runpy.run_path(MAX30102);
runpy.run_path(heartrate_monitor);
runpy.run_path(hrcalc)
runpy.run_path(MLX90614);


while(True):
    if __name__ == "__main__":

        sensor = MLX90614()
        print("Object:", sensor.readObjectTemperature())
        print("Ambient:", sensor.readAmbientTemperature())
        time.sleep(3)

parser = argparse.ArgumentParser(description="Read and print data from MAX30102")
parser.add_argument("-r", "--raw", action="store_true",
                    help="print raw data instead of calculation result")
parser.add_argument("-t", "--time", type=int, default=30,
                    help="duration in seconds to read from sensor, default 30")
args = parser.parse_args()

print('sensor starting...')
hrm = HeartRateMonitor(print_raw=args.raw, print_result=(not args.raw))
hrm.start_sensor()
try:
    time.sleep(args.time)
except KeyboardInterrupt:
    print('keyboard interrupt detected, exiting...')

hrm.stop_sensor()
print('sensor stoped!')

