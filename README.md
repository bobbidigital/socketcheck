##Description##

The point of this script was to perform automated connectivity checks from a machine.
THe original usecase was testing machines in a lab setup to make sure the more stringent
firewall rules were allowing the correct outbound traffic. But across multiple machines
we needed to make sure we could perform these checks quickly and make it repeatable 
by the operations staff. 

The script is highly tailored to my use case at the time, but I since I wrote it, I'm seeing more uses for it, so I'll make updates as I encounter those use cases.


##Script Execution##

    socketcheck.py <data_file> <application_name> [--timeout 10]


* data file - path to the csv file containing the checks to be made.

* application_name - The name of the application to check. Matches against values in the CSV file.

* timeout (optional) -- The timeout value for the socket connection. Defaults to 10 seconds.


##CSV File Setup##

The application is expecting a CSV file in the format of

\<service name\>,\<IP Address\>*,\<ports\>*,\<app_name\>

* Service Name - This parameter is a friendly name for the service or website
you're attempting to connect to. It's only used in the final output of the command.

* IP Address - The IP addresses that need to be looked at. In my use case I didn't need hostnames, so DNS resolution isn't an option. I'll probably add this at a later point when I need it. Specify multiple values by separating them with a space.

* ports - Specifies which ports to test. Specify multiple ports by separating them with a space. Right now the script assumes that all connections are TCP based.

* app_name - If you have a lot of servers you're validating (like I was) it becomes worthwhile to export all your checks into a single file. This is the value that is compared against as the application variable on the command line.


##Soon To Dos##

Lots of stuff to do and improve on this script. But some things that I'll probably do sooner than later (because I personally need them)

* Specify UDP or TCP

* Make application_name an optional parameter and just default to checking everything.

* Create an output file that can be used as an input later on for checks.
