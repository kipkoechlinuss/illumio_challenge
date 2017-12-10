#!/usr/bin/env python3
import sys
import re
import csv
class Firewall(object):
    def __init__(self, args):
        self.args = "/Users/kipkoech/Desktop/illumio/Workbook1.csv"

        #open the csv file and check if the packet properties matches the rules
    def accept(self,direction,protocol,port,ip):
        with open(self.args, 'rU') as my_file:
            reader= csv.reader(my_file)
            data = list(reader)
        for i in range(len(data)-1):
            if((data[i][0] == direction and data[i][1] == protocol and self.checkrange(data[i][2],port)and self.checkrange(self.parse_range(self.match_ips(data[i][3])),ip))):
                return True
            return False              
        #this method deals with the scenario with port range or ip range
    def parse_range(self,rng):
        splitted = []
        if isinstance(rng, int):
            return rng
        splitted = rng.split('-')
        return [i for i in splitted]



        #check if the port or ip matches. Ip and Port had to be handled in different function because they could be in range format
    def checkrange(self,rules_payload, payload):
        result = self.parse_range(rules_payload)
        if(rules_payload == payload):
            return True
        elif(len(result) == 2):
            return (result[0] <= payload and payload <= result[1])
        else:
            return False
    def match_ips(self,IP):
        splitted_IP = []
        splitted_IP = IP.split('.')
        return [i for i in splitted_IP]


        
