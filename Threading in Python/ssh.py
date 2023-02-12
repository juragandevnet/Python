username,password,ip_addressfrom netmiko import ConnectHandler
import getpass
from time import strftime,gmtime
from threading import Thread

def DeviceLogin(username,password,ip_address):
    login = {
        'device_type' : 'cisco_ios',
        'ip' : ip_address,
        'username' : username,
        'password' : password
    }
    ip_address = ip_address.strip('\n')
    net_connect = ConnectHandler(**login)
    backup = net_connect.send_command("show run")
    backupname = ip_address + '.txt'
    w = open(backupname,"w")
    w.write(backup)
    w.close()
    waktu = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    print(waktu)
    print("Process Completed For " + ip_address)
    net_connect.disconnect()

### MAIN SCRIPT ###
r = open('devices.txt','r')
username = input("Masukkan Username: ")
password = getpass.getpass()

### FOR LOOP ###
'''
for ip_address in r.readlines():
    DeviceLogin(username,password,ip_address)
'''

### THREADING PROCESS ###

threads=[]
threads = [Thread(target=DeviceLogin, args=(username,password,ip_address)) for ip_address in r.readlines()]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()



