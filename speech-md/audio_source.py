# Handles I/O Devices, i.e. Voice Input Source

# Imports
import pyaudio

# Variables
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
num_devices = info.get('deviceCount')


class Error(Exception):
    """Base class for other exceptions"""
    pass


class OutOfRangeError(Error):
    """Raised when the input value is not in the index of available devices"""
    pass


def list_index():
    for i in range(0, num_devices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device ID: ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
        elif num_devices == 0:
            print("No input device detected, please ensure your microphone is plugged in and enabled.")
            break


def get_max_input_devices():
    for i in range(0, num_devices):
        max_devices = p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')
        return max_devices


def get_input():
    max_devices = get_max_input_devices()
    while True:
        try:
            device = int(input("Please select a device by ID number: "))
            if device >= max_devices:
                raise OutOfRangeError
            elif device <= -1:
                raise OutOfRangeError
            else:
                return device
        except ValueError:
            print("Please input a valid integer corresponding to you device ID.")
        except OutOfRangeError:
            print("Please enter a valid device ID.")
