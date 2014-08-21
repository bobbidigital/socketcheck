#!/usr/local/python-2.7.8/bin/python2.7
import socket
import argparse
import sys




def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The path to the file used for input processing')
    parser.add_argument('application', help='The application name that we should process for')
    parser.add_argument('--timeout', help='The timeout for socket connections', 
                        action='store', default=10, type=int)
    args = parser.parse_args()
    socket.setdefaulttimeout(args.timeout)
    return args


def connect_to_host(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except BaseException as ex:
        print "Failed to create socket!"
        return False
    try:
        s.connect((host, int(port)))
        s.close()
        return True
    except BaseException as ex:
        print "Failed to connect to server. %s" % ex
        return False

def main():
    args = get_arguments()
    f = open(args.file)
    failures = {}
    for line in f:
        list_of_fails = []
        service, hosts, ports, applications = line.strip().split(",")
        print "Processing %s" % service
        applications = [x.upper() for x in applications.split(" ")]
        if  args.application.upper() in applications:
            for host in hosts.split(" "):
                for port in ports.split(" "):
                    sys.stdout.write("Connecting to %s on port %s......" % (host,
                        port))
                    is_success = connect_to_host(host, port)
                    if is_success:
                        print "SUCCESS"
                    else:
                        list_of_fails.append((host,port))
        if len(list_of_fails) > 0:
            failures[service] = list_of_fails
    display_failures(failures)


def display_failures(failures):
    print "\n\t *** Failure Report *** "
    for failure in failures.keys():
        fails = failures[failure]
        print "\nFailures for %s" % failure
        for fail in fails:
            print "\t\tHost: %s Port: %s" % (fail[0], fail[1])

main()
