from netmiko import ConnectHandler
import getpass

username = input("Masukkan Username: ")
password = getpass.getpass()

login = {
    'device_type' : 'cisco_ios',
    'host' : '131.226.217.143',
    'username' : username,
    'password' : password
}

net_connect = ConnectHandler(**login) 
print("################# SEBELUM CONFIG ###############")
output = net_connect.send_command("show ip int brief")
print(output)
net_connect.send_config_set(['interface loopback 69','ip address 69.69.69.69 255.255.255.0','no shut'])
print("################# SESUDAH CONFIG ###############")
output = net_connect.send_command("show ip int brief")
print(output)