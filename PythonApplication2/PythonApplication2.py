ip = '192.168.3.1'
ip = ip.split('.')
ip_template = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'
'''
print(ip_template.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))






