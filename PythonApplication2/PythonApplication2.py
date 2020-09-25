ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_value = ospf_route.strip().split()
ospf_value.remove('via')
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
print(template.format(ospf_value[0], ospf_value[1], ospf_value[2], ospf_value[3], ospf_value[4]))




