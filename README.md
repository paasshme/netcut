# installation
Avec python3 et pip:


Linux :
```shell
install the deps
$ pip install -r requirement.txt
launch the server with su permissions (required)
$ sudo python serv.py
```

# Documentation
The server use json through websockets to communicate with the client : 
["command", "arg1", "arg2", [...]]
## Here are the request that the server currently recognize : 
* ### nmap_scan
    Return IP of every connected device using nmap
    #### args
    1. (optional) network adress with cidr notation  
    default to "192.168.0.0/24"
    #### returns the list of local devices ip
    example : ["192.168.0.11", "192.168.0.21", "192.168.0.23"]
* ### arp_scan
    Return IP & Mac of every connected client, faster than a nmap scan but less reliable
   #### args
    1. (optional) network adress with cidr notation  
    default to "192.168.0.0/24"
    #### returns the list of local devices ip and mac
    example : [{"ip": "192.168.0.33", "mac": "70:85:c2:83:00:70"}, {"ip": "192.168.0.41", "mac": "68:a3:78:50:67:8a"}, {"ip": "192.168.0.22", "mac": "20:47:da:28:8c:51"}]
* ### arp_spoof

* ### sniff
* ### set_gateway
* ### spoof_stop
* ### sniff_stop

