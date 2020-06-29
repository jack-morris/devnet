from netmiko import ConnectHandler
from paramiko import net_connect
IOS = {
    'device_type': 'ios',
    'ip': '192.168.1.200',
    'username': 'jack',
    'password': 'cisco'
}
net_conect = ConnectHandler(**IOS)
output = net_connect.send_command('show version')
print(output)