#!/usr/bin/python3

import requests as req
import argparse
import sys
import socket

parser = argparse.ArgumentParser(prog="check_dyndns.py", description='Check DynDNS for IP updates.')
parser.add_argument("-d", "--domain", dest='domain',
                    metavar="my-domain.com", help="The name of the domain to check.")
args = parser.parse_args()

# Query the DNS server for the IP address of the domain
ip_list_dns = []
ais = socket.getaddrinfo(args.domain, 0, 0, 0, 0)
for result in ais:
    ip_list_dns.append(result[-1][0])
    ip_list = list(set(ip_list_dns))
ip_list = list(set(ip_list_dns))

# Get the public IP address of the current machine.
try:
    my_ip = req.get("https://v4.ident.me").text
except:
    print("Unknown: Could not get public IP.")
    sys.exit(3)

# Compare the public IP address with the DNS IP address.
if my_ip in ip_list:
    print(f"OK: DynDNS is up to date ({my_ip}).")
else:
    print(f"Critical: DynDNS is not up to date. Current IP: {my_ip}, DNS IP: {', '.join(ip_list)}")
    sys.exit(2)
