access_template = [
    "Введите номер VLAN",
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]
trunk_template = [
    "Введите разрешенные VLANы",
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]
config = {
    'access': access_template,
    'trunk': trunk_template
    }
mode = input('Введите режим работы интерфейса ({}): '.format('/'.join(list(config.keys()))))
int = input('Введите тип и номер интерфейса: ')
vlan = input('{}: '.format(config[mode][0]))
config_str = '\n'.join(config[mode][1:])
print('interface {}'.format(int))
print(config_str.format(vlan))

