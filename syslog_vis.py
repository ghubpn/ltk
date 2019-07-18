#!/usr/bin/python3

import matplotlib.pyplot as plt
import re



class Syslog_Entry:
    """Syslog_Entry represents a message entry in syslog."""
    def __init__(self, eid,  entry):
        self.__eid = eid #entry id
        self.__month = entry.split(" ")[0]
        self.__day = entry.split(" ")[1]
        self.__time = entry.split(" ")[2]
        self.__host = entry.split(" ")[3]
        self.__service = re.sub('\[[0-9]+\]:', '', entry.split(" ")[4]).strip(':')
        #self.__pid = re.search('\[[0-9]+\]').strip('[').strip(']')
        self.__message = ' '.join(entry.split(" ")[5:])

    # field getters

    @property
    def get_eid(self):
        return seld.__eid

    @property
    def get_month(self):
        return self.__month

    @property
    def get_day(self):
        return self.__day

    @property
    def get_time(self):
        return self.__time

    @property
    def get_host(self):
        return self.__host

    @property
    def get_service(self):
        return self.__service

    #@property
    #def get_pid(self):
    #    return self.__pid

    @property
    def get_message(self):
        return self.__message

    # more granular get_time methods

    @property
    def get_hour(self):
        return self.__time.split(":")[0]

    @property
    def get_minute(self):
        return self.__time.split(":")[1]

    @property
    def get_second(self):
        return self.__time.split(":")[2]



class Syslog:
    """Represents syslog file in memory"""
    def __init__(self):
        self.__syslog = []
        eid = 0
        with open('/var/log/syslog') as entries:
            for entry in entries:
                self.__syslog.append(Syslog_Entry(eid, entry))
                eid = eid+1

    def get_syslog(self):
        return self.__syslog

    def get_entry(self, i):
        return self.__syslog[i]



print("\nPopulating syslog data structure for analysis...\n")
sl = Syslog()
print("Select visualization:\n")
print("(1) Aggregate by Service")
print("(2) Syslog Time Density")
print("(3) Syslog Time Density for a Service")
print("(4) Aggreate by Servic in Time Range")
print("(5) ...")
print("(6) ...")
print("(7) ...")
print("(8) ...")
print("(9) ...")
print("(0) Quit\n")
cmd = input("> ")



if cmd == "1":
    services = {}
    for i in range(len(sl.get_syslog())):
        services[sl.get_entry(i).get_service] = services.get(sl.get_entry(i).get_service, 0) + 1
    plt.barh(list(services.keys()), list(services.values()))
    plt.xlabel('Occurances')
    plt.title('Syslog Aggregation by Service')
    plt.show()

elif cmd == "2":
    times = []
    eids = []
    for i in range(len(sl.get_syslog())):
        times.append(sl.get_entry(i).get_time)
        eids.append(i)
    plt.scatter(times, eids, s=40)
    plt.axis([0, 100, 0, len(eids)])
    plt.xlabel('Time')
    plt.title('Syslog Time Density')
    plt.show()
    
elif cmd == "3":
    serv = input("Enter the name of a service: ")
    # is there a better way to handle input filtering here?
    times = []
    eids = []
    for i in range(len(sl.get_syslog())):
        if(sl.get_entry(i).get_service == serv):
            times.append(sl.get_entry(i).get_time)
            eids.append(i)
    plt.scatter(times, eids, s=40)
    plt.axis([0, 100, 0, len(sl.get_syslog())])
    plt.xlabel('Time')
    plt.title('Syslog Time Density (' + serv + ')') # ensure that first char of serv is capitalized while rest is lowercase
    plt.show()

elif cmd == "4":
    start = input("Enter time to start analyzing from: ")
    end = input("Enter time to analyze to: ")
    # what happens if format is wrong? HH:MM:SS ...use regex!
    # what happens if that time has not elapsed yet?
    # colour each service differently!
    services = {}
    for i in range(len(sl.get_syslog())):
        if(sl.get_entry(i).get_time >= start and sl.get_entry(i).get_time <= end):
            services[sl.get_entry(i).get_service] = services.get(sl.get_entry(i).get_service, 0) + 1
    plt.barh(list(services.keys()), list(services.values()))
    plt.xlabel('Occurances')
    plt.title('Syslog Aggregation by Service (from ' + start + " to " + end + ")" )
    plt.show()

elif cmd == "5":
    print("This option is not defined yet\n")

elif cmd == "6":
    print("This option is not defined yet\n")

elif cmd == "7":
    print("This option is not defined yet\n")

elif cmd == "8":
    print("This option is not defined yet\n")

elif cmd == "9":
    print("This option is not defined yet\n")

elif cmd == "0":
    print("Exiting...\n")
    exit()

else:
    print("ERROR: " + cmd + " is not a valid option. Exiting...\n")

print("Program run complete. Ending process...\n")
