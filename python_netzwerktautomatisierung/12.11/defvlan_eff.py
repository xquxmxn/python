def generate_vlan_commands(vlan_ports):
    commands = []
    for vlan, ports in vlan_ports.items():
        commands.append(f"vlan {vlan}")
        commands.append(f"name vlan{vlan}_ports_{'_'.join(map(str, ports))}")
    return commands

def generate_port_commands(portlist, vlanlist):
    commands = []
    for port, vlan in zip(portlist, vlanlist):
        commands.extend([
            f"interface FastEthernet0/{port}",
            "switchport mode access",
            f"switchport access vlan {vlan}",
            "exit"
        ])
    return commands

def generate_trunk_commands(trunklist):
    commands = []
    for port in trunklist:
        commands.extend([
            f"interface FastEthernet0/{port}",
            "switchport mode trunk",
            "exit"
        ])
    return commands

def main():
    portlist = [1, 4, 6, 10, 11, 12, 13, 14, 17]
    vlanlist = [10, 10, 20, 20, 10, 30, 40, 30, 20]
    trunklist = [2, 3]

    vlan_ports = {}
    for port, vlan in zip(portlist, vlanlist):
        vlan_ports.setdefault(vlan, []).append(port)

    commands = []
    commands.extend(generate_vlan_commands(vlan_ports))
    commands.extend(generate_port_commands(portlist, vlanlist))
    commands.extend(generate_trunk_commands(trunklist))

    for command in commands:
        print(command)

if __name__ == "__main__":
    main()