portlist=[1,4,6,10,11,12,13,14,17]
vlanlist=[10,10,20,20,10,30,40,30,20]
Trunklist =[2,3]

cmdEthernet="interface FastEthernet0/{}"
cmdVlan="switchport access vlan {}"
cmdTrunk="switchport mode trunk"
cmdVlanDef = "vlan {}"
cmdVlanName = "name vlan{}_ports_{}"
cmdTrunk = "switchport mode trunk"


commandlist=[]

vlan_ports = {}
for index, vlan in enumerate(vlanlist):
 if vlan not in vlan_ports: 
  vlan_ports[vlan] = [] 
 vlan_ports[vlan].append(portlist[index])

for vlan, ports in vlan_ports.items():
    commandlist.append(cmdVlanDef.format(vlan))
    commandlist.append(cmdVlanName.format(vlan, "_".join(map(str, ports))))

for index, port in enumerate(portlist):
    commandlist.append(cmdEthernet.format(port))
    commandlist.append("switch port mode access")
    commandlist.append(cmdVlan.format(vlanlist[index]))
    commandlist.append("exit")

for port in Trunklist:
    commandlist.append(cmdEthernet.format(port))
    commandlist.append(cmdTrunk)
    commandlist.append("exit")

for command in commandlist:
    print(command)



