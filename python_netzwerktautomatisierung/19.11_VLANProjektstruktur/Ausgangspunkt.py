#!/usr/bin/env python
#Main, Hauptskript

import sys
from send import sendCommands
from vlan_config import PortList, vlanList, trunkList

cmdEthernet='interface FastEthernet0/{}'
cmdVlan='switchport access vlan {}'
commandList=[] 

#Dateiname
default_filename = "switch_commands.txt"

for index,port in enumerate(PortList):
   commandList.append(cmdEthernet.format(port))
   commandList.append('switchport mode access')
   vlan=vlanList[index];
   commandList.append(cmdVlan.format(vlan))
   commandList.append('exit')

for trunkport in trunkList:
   commandList.append(cmdEthernet.format(trunkport))
   commandList.append('switchport mode trunk')
   commandList.append('exit') 

#Überprüfung, ob der Dateiname als Argument übergeben wurde
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = default_filename

# Verwendung der Funktion „sendCommands“
num_commands = sendCommands(commandList, filename)
print(f"Anzahl der Commands:{num_commands}")
print(f"Portiste:{PortList}")