import sys
inteface = input('Интерфейс: ')
vlan = input('Вилан: ')
access_template = ['switch mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
print('\n' + '-' * 30)
print('interface {}'.format(inteface))
print('\n'.join(access_template).format(vlan))