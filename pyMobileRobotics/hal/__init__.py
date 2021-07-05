import os
import sys
import imp

import logging


lib_path = '/usr/local/lib/vmxpi/vmxpi_hal_python.py'

if not(os.path.isfile(lib_path)):
    logging.error("Can't find VMX-HAL library. Do you installed VMX-HAL library?")
    # raise ImportError("Can't find VMX-HAL library. Do you installed VMX-HAL library?")

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', lib_path)