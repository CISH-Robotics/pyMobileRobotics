import os
import sys
import imp


lib_path = '/usr/local/lib/vmxpi/vmxpi_hal_python.py'

if not(os.path.isfile(lib_path)):
    raise ImportError("Can't find VMX-HAL library. Are you installed VMX-HAL library?")

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', lib_path)