# What

I made this tool initially to verify that I migrated all records before switching from one nameserver to another.

That way I could query the records and compare against the one I created on the new NS without actually switching yet.

# How To Use

```sh
./dnscomp.sh -d domain.tld -r resolver.dns.tld
```

example:
```sh
./dnscomp.sh -d ctrlalt.dev -r 208.67.222.222
```
That will compare the records provided by your default DNS settings with the one provided by Open DNS (208.67.222.222)
