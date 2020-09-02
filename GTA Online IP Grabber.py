import requests
from scapy.all import *
from ip2geotools.databases.noncommercial import DbIpCity

def pc(packet):
    if packet.proto == 17:
        udp = packet.payload


while True:
 x = sniff(filter="udp and port 6672", prn=pc, store=1, count=1)# GTA V Online UDP default Port is 6672
 y = x[0][IP].src
 z = x[0][IP].dst
 if z == "192.168.0.102":#replace with your local IP
     pass
 else:
   print("-----------------------------------------------------------")
   try:
    print(f"Destination: IP Address: [{z}] Country: [{DbIpCity.get(z, api_key='free').country}] Region: [{DbIpCity.get(z, api_key='free').region}] City: [{DbIpCity.get(z, api_key='free').city}]")
   except:
    print(f"Destination: IP Address: [{z}] Country: [{DbIpCity.get(z, api_key='free').country}]")
   print("-----------------------------------------------------------")
