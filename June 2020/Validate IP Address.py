import re
def validIPAddress(IP):
    """
    :type IP: str
    :rtype: str
    """
    ipv4 = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
    ipv6 = re.compile(r'^(([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4}))$')
    if(ipv4.match(IP)):
        return "IPv4"
    elif(ipv6.match(IP)):
        return "IPv6"
    else:
        return "Neither"


print(validIPAddress("2001:0db8:85a3:033:0:8A2E:0370:7334"))