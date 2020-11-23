def get_int_vlan_map(config_filename):
    mode_access = {}
    mode_trunk = {}
    with open(config_filename) as f:
        for line in f:
            if "Ethernet" in line:
                if "vlans" in locals():
                    if len(vlans) > 0:
                        result = [vlan for vlan_list in vlans for vlan in vlan_list] #преобразование в список STR
                        convert = []
                        for vl in result:
                            if "-" in vl:
                                vl_range = [num for num in range(int(vl.split('-')[0]), int(vl.split('-')[1])+1)]
                                for i in vl_range:
                                    convert.append(int(i))
                            else:
                                convert.append(int(vl))
                        mode_trunk[interface] = convert
                interface = line.split()[1]
                vlans = [] #список создается при совпадении "Ethernet"
            if "access vlan" in line:
                mode_access[interface] = int(line.split()[-1])
            if "allowed vlan" in line:
                vlans.append(line.split()[-1].split(',')) #формируется список списков для соответствующего INTERFACE
    return mode_trunk
print(get_int_vlan_map('cisco_config.txt'))

