#!/usr/bin/env python3

import sys
import getopt
import re
import dns.resolver

print()
print('██████╗ ███╗   ██╗███████╗     ██████╗ ██████╗ ███╗   ███╗██████╗ ')
print('██╔══██╗████╗  ██║██╔════╝    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗')
print('██║  ██║██╔██╗ ██║███████╗    ██║     ██║   ██║██╔████╔██║██████╔╝')
print('██║  ██║██║╚██╗██║╚════██║    ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ')
print('██████╔╝██║ ╚████║███████║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ')
print('╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ')
print()

def createResolver(resolv):
    resolve_ip = []

    patv4 = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    isIPv4 = patv4.match(resolv)

    if isIPv4:
        resolve_ip = [resolv]
    else:
        records = dns.resolver.resolve(resolv, 'A')
        for data in records:
            resolve_ip.append(str(data))

    new_resolver = dns.resolver.Resolver()
    new_resolver.nameservers = resolve_ip
    return new_resolver

def get_records (domain, type, resolver = None):
    noresolv = []
    resolv = []

    try:
        records = dns.resolver.resolve(domain, type)
        for data in records:
            noresolv.append(data)
    except dns.resolver.NoAnswer:
        noresolv.append('-')
    
    try:
        records = resolver.resolve(domain, type)
        for data in records:
            resolv.append(data)
    except dns.resolver.NoAnswer:
        resolv.append('-')

    print('=====')
    print('{} RECORDS'.format(type))
    print('=====')

    i = 0
    while (i < len(noresolv) or i < len(resolv)):
        has_noresolv = i < len(noresolv)
        has_resolv = i < len(resolv)

        print('{:<50}{:<50}'.format(str(noresolv[i]) if has_noresolv else '-', str(resolv[i]) if has_resolv else '-'))
        i += 1
    print()

def printUsage(status = 0):
    print('dnscomp.py -d <domain.tld> -r <resolver.tld or resolver IPv4>')
    sys.exit(status)

def main(argv):
    domain = None
    resolver = None

    try:
        opts, args = getopt.getopt(argv,'hd:r:')
    except getopt.GetoptError:
        printUsage(2)

    for opt, arg in opts:
        if opt == '-h':
            printUsage()
        elif opt in ('-d', '--domain'):
            domain = arg
        elif opt in ('-r', '--resolver'):
            resolver = createResolver(arg)

    if domain == None or resolver == None:
        printUsage(2)

    get_records(domain, 'A', resolver)
    get_records(domain, 'AAAA', resolver)
    get_records(domain, 'CNAME', resolver)
    get_records(domain, 'MX', resolver)
    get_records(domain, 'TXT', resolver)
    get_records(domain, 'NS', resolver)

if __name__ == '__main__':
    main(sys.argv[1:])
