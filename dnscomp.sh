#!/usr/bin/env bash

while getopts ":d:r:" arg; do
  case ${arg} in
    d) DOMAIN="${OPTARG}";;
    r) RESOLVER="${OPTARG}";;
    \?) echo "Unrecognized argument -${OPTARG}"; exit 1;;
  esac
done

echo;
echo "██████╗ ███╗   ██╗███████╗     ██████╗ ██████╗ ███╗   ███╗██████╗ ";
echo "██╔══██╗████╗  ██║██╔════╝    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗";
echo "██║  ██║██╔██╗ ██║███████╗    ██║     ██║   ██║██╔████╔██║██████╔╝";
echo "██║  ██║██║╚██╗██║╚════██║    ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ";
echo "██████╔╝██║ ╚████║███████║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ";
echo "╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ";
echo;

get_current_records () {
  echo Current Values
  echo "$(dig +short $1 $DOMAIN)"
}

get_resolver_records () {
  echo Resolver Values
  echo "$(dig +short $1 $DOMAIN @$RESOLVER)"
}


echo DOMAIN $DOMAIN; echo;

echo =====; echo A RECORDS; echo =====;
get_current_records A
get_resolver_records A
echo;

echo =====; echo AAAA RECORDS; echo =====;
get_current_records AAAA
get_resolver_records AAAA
echo;

echo =====; echo CNAME RECORDS; echo =====;
get_current_records CNAME
get_resolver_records CNAME
echo;

echo =====; echo MX RECORDS; echo =====;
get_current_records MX
get_resolver_records MX
echo;

echo =====; echo TXT RECORDS; echo =====;
get_current_records TXT
get_resolver_records TXT
echo;

echo =====; echo NS RECORDS; echo =====;
get_current_records NS
get_resolver_records NS
echo;
