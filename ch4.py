import csv
from netmiko import ConnectHandler

class Device:
    '''Device Class'''
    def __init__(self, hostname, ip_address, type, username, password):
        '''device values'''
        self.hostname = hostname
        self.ip_address = ip_address
        self.type = type
        self.username = username
        self.password = password

device_list = csv.reader(open('ch4.csv'))

for row in device_list:
    device = Device(row[0], row[1], row[2], row[3], row[4])
    switch = {
        'device_type': 'cisco_ios',
        'ip': device.ip_address,
        'username': device.username,
        'password': device.password,
        'port': 22,
        'secret': 'enable',
    }
    ssh_connect = ConnectHandler(**switch)

    ssh_connect.enable()
    print(f"now connecting to host {device.hostname}")
    print(ssh_connect.send_command('show ip dhcp binding'))
    ssh_connect.disconnect()






