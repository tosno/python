from operator import itemgetter
with open('cam_table.txt') as f:
    vlans = []
    for line in f:
        if 'DYNAMIC' in line:
            vlan = line.split()
            vlan.remove('DYNAMIC')
            vlan[0] = int(vlan[0])
            vlans.append(vlan)
        else:
            continue
vlans.sort(key=itemgetter(0))
for i in vlans:
    print('{:6}    {:14}    {:15}'.format(*i))


