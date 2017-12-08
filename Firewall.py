#!/usr/bin/env python
import sys
import re
class Firewall:
    def __init__(self, args):
        self.args = "/Users/kipkoech/Desktop/illumio/Workbook1"

        #open the csv file and check if the packet properties matches the rules. This is the main function doing the checking
    def openandcheck(self,dir,protocol,port,ip):
        file=open(args)
        reader = csv.reader(file)
        for line in reader:
            lines = line[0],line[1],line[2],line[3]
        return lines[0] == dir and lines[1] == protocol and parse_range(lines[2],port)and parse_range(lines[3],ip) 
        #this method deals with the scenario with port range or ip range
    def parse_range(self,rng):
        parts = rng.split('-')
        #this list is the parsed results put in array form
        list_ = []
        if 1 > len(parts) > 2:
            raise ValueError("Bad range: '%s'" % (rng,))
        parts = [int(i) for i in parts]
        start = parts[0]
        end = start if len(parts) == 1 else parts[1]
        if start > end:
            end, start = start, end
        list_[0] = start
        list_[1] = end
        return list_
        #check if the port or ip matches. Ip and Port had to be handled in different function because they could be in range format
    def checkrange(self,rules_payload, payload):
        result = parse_range(rules_payload)
        if(len(result)) == 1:
            if(result[0] == payload):
                return True
            else:
                return False
        elif(len(result == 2)):
            if(result[0] <= payload or result[1] >= payload):
                return True
            else:
                return False
