trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]
trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}
def generate_access_config(intf_vlan_mapping, trunk_template):
    config = dict.fromkeys(intf_vlan_mapping.keys())
    for intf, vlans in intf_vlan_mapping.items():
        value = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                value.append(command + ' ' + str(vlans).strip('[]'))
            else:
                value.append(command)
        config[intf] = value
    return config
print(generate_access_config(trunk_config, trunk_mode_template))


