# Importing the library
import os

import paramiko
import psutil
import datetime
from psutil import virtual_memory


class details:

    def memory_display(self):
        # Calling psutil.cpu_present() for 4 seconds
        print('The CPU usage is: ', psutil.cpu_percent(4))

        # Getting loader15 minutes
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = (load15 / os.cpu_count()) * 100
        print("The CPU usage is : ", cpu_usage)

        # Getting % usage of virtual_memory
        ram_usage = psutil.virtual_memory()[2]
        print('RAM memory % used:', psutil.virtual_memory()[2])
        # Getting usage of virtual_memory in GB
        print('RAM Used (GB):', psutil.virtual_memory()[3] / 1000000000)

        # Getting current date and time using now().
        current_time = datetime.datetime.now()
        print("Time now at greenwich meridian is:", current_time)

        # for memory details
        mem = virtual_memory()
        var = psutil.virtual_memory().total
        print(mem)

        return cpu_usage, ram_usage

    def vm_connection(self):
        host = "192.168.1.9"
        username = "nick"
        password = "12345"

        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        _stdin, _stdout, _stderr = client.exec_command("df")
        print(_stdout.read().decode())
        client.close()
