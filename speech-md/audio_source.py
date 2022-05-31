# Handles I/O Devices, i.e. Voice Input Source

# Imports
import pyaudio
import sys

# Variables
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
num_devices = info.get('deviceCount')


# Base class for other exceptions
class Error(Exception):
    pass


# Custom exception; raised when the input value is not in the index of available devices
class OutOfRangeError(Error):
    pass


# Detects and lists input devices
def list_index():

    # Prints devices with an ID number and description/name of device
    for i in range(0, num_devices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device ID: ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

        # Exits if no input device is found
        while num_devices == 0:
            print("No input device detected, please ensure your microphone is plugged in and enabled.")
            sys.exit()


# Retrieves and returns the amount of input devices found as an integer
def get_max_input_devices():

    for i in range(0, num_devices):
        max_devices = p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')
        return max_devices


# Allows user to choose a device by ID, and returns it
def get_input():

    max_devices = get_max_input_devices()
    while True:
        try:
            # Prompts user to select an input device by ID number from list
            device = int(input("Please select a device by ID number: "))

            # Catch errors
            if device >= max_devices:
                raise OutOfRangeError
            elif device <= -1:
                raise OutOfRangeError
            else:
                return device
        # Handle errors
        except ValueError:
            print("Please input a valid integer corresponding to you device ID.")
        except OutOfRangeError:
            print("Please enter a valid device ID.")
