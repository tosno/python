ip_address = input('Введите IP адрес: ')
ip = ip_address.split('/')[0].split('.')
mask = int(ip_address.split('/')[1])
mask_bit = list('1' * mask + '0' * (32-mask))
mask_oct = [''.join(mask_bit[0:8]), ''.join(mask_bit[8:16]), ''.join(mask_bit[16:24]), ''.join(mask_bit[24:32])]
ip_template = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
print(ip_template.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))
print(f'''
Mask:
/{mask}
{int(mask_oct[0], 2):<8}  {int(mask_oct[1], 2):<8}  {int(mask_oct[2], 2):<8}  {int(mask_oct[3], 2):<8}
{int(mask_oct[0], 2):08b}  {int(mask_oct[1], 2):08b}  {int(mask_oct[2], 2):08b}  {int(mask_oct[3], 2):08b}
''')





