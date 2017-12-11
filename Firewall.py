#!/usr/bin/env python3
import sys
import re
import csv
class Firewall(object):
    def __init__(self, args):
        self.args = "/Users/kipkoech/Desktop/illumio/Workbook1.csv"

        #open the csv file and check if the packet properties matches the rules. All the four rules have to be met.
    def accept(self,direction,protocol,port,ip):
        ret = False
        with open(self.args, 'rU') as my_file:
            reader= csv.reader(my_file)
            data = list(reader)
        for i in range(0,len(data)):
            
            if(data[i][0] == direction and data[i][1] == protocol and self.checkrange(data[i][2],port)and self.checkrange(self.match_ips(data[i][3]),ip)):
                ret = True
        return ret              
        #this method deals with the scenario with port range or ip range
    def parse_range(self,rng):
        if isinstance(rng, int):
            return rng
        return ([int(i) for i in rng.split('-')])
      
      #check if the port MATCHES. it only checks if i am spliting on '-' . Ip and Port had to be handled in different function because they could be in range format
    def checkrange(self,rules_payload, payload):
        result = []
        for i in self.parse_range(rules_payload):
            result.append(i)
        rt = False
        if isinstance(rules_payload,int):
            if(rules_payload == payload):
                rt = True
        elif(len(result) == 2):
            if (int(result[0]) <= payload and payload <= int(result[1])):
                rt = True
        elif(len(result) == 1):
            if(result[0] == payload):
                rt = True
        else:
            rt = False
        return rt
    #this case checks splits the ip on '.'. 
    def match_ips(self,IP):
        st = ''
        splitted_IP = []
        splitted_IP = IP.split('.')
        return (''.join([i for i in splitted_IP]))
    


        


        
