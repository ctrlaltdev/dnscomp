#!/usr/bin/env python3

import sys
import getopt
import dns.resolver

print()
print("██████╗ ███╗   ██╗███████╗     ██████╗ ██████╗ ███╗   ███╗██████╗ ")
print("██╔══██╗████╗  ██║██╔════╝    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗")
print("██║  ██║██╔██╗ ██║███████╗    ██║     ██║   ██║██╔████╔██║██████╔╝")
print("██║  ██║██║╚██╗██║╚════██║    ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ")
print("██████╔╝██║ ╚████║███████║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ")
print("╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ")
print()

def get_records (domain, type, resolver = None):
    noresolv = []
    resolv = []

    dns.resolver.restore_system_resolver()

    try:
        records = dns.resolver.resolve(domain, type)
        for data in records:
            noresolv.append(data)
    except dns.resolver.NoAnswer:
        noresolv.append('')

    dns.resolver.override_system_resolver(resolver)
    
    try:
        records = dns.resolver.resolve(domain, type)
        for data in records:
            resolv.append(data)
    except dns.resolver.NoAnswer:
        resolv.append('')

    print('=====')
    print('{} RECORDS'.format(type))
    print('=====')

    i = 0
    while (i < len(noresolv) or i < len(resolv)):
        has_noresolv = i < len(noresolv)
        has_resolv = i < len(resolv)

        print('{:<50}{:<50}'.format(str(noresolv[i]) if has_noresolv else '', str(resolv[i]) if has_resolv else ''))
        i += 1
    print()

def main(argv):
    domain = None
    resolver = None
    try:
        opts, args = getopt.getopt(argv,"hd:r:")
    except getopt.GetoptError:
        print('dnscomp.py -d <domain.tld> -r <resolver.tld>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('dnscomp.py -d <domain.tld> -r <resolver.tld>')
            sys.exit()
        elif opt in ("-d", "--domain"):
            domain = arg
        elif opt in ("-r", "--resolver"):
            resolver = arg

    get_records(domain, 'A', resolver)
    get_records(domain, 'AAAA', resolver)
    get_records(domain, 'CNAME', resolver)
    get_records(domain, 'TXT', resolver)
    get_records(domain, 'NS', resolver)

if __name__ == "__main__":
    main(sys.argv[1:])
