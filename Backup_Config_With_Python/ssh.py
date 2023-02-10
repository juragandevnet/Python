from netmiko import ConnectHandler
import getpass

username = input ("Masukkan Username: ")
password = getpass.getpass()

r = open('devices.txt','r')

for ip_address in r.readlines():
    ip_address = ip_address.strip('\n')
    login = {
        'device_type' : 'cisco_ios',
        'host': ip_address,
        'username' : username,
        'password' : password}
    net_connect = ConnectHandler(**login)
    backup = net_connect.send_command("show run")
    print("Backup Completed for $s", ip_address)
    backupname = ip_address + '.txt'
    w = open(backupname,"w")
    w.write(backup)
    w.close()