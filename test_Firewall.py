#!/usr/bin/env python3
import sys
import socket
import unittest
from Firewall import Firewall

#from ipaddress import IPv4Address, IPv4Network, IPv4Interface


class FirewallTestCase(unittest.TestCase):

	global firewall
	args = "/Users/kipkoech/Desktop/illumio/Workbook1.csv"

	firewall = Firewall(args)


	def test_parse_range(self):
  		lst1 = ['56','93']
  		lst2 = ['344', '299999']
  		lst3 = ['0', '230000000000']
  		self.assertEqual(firewall.parse_range('56-93'),lst1 )
  		self.assertEqual(firewall.parse_range("344-299999"),lst2 )
  		self.assertEqual(firewall.parse_range("0-230000000000"),lst3 )
  		self.assertEqual(firewall.parse_range("0-230000000000"),lst3 )


	def test_checkrange(self):
		self.assertFalse(firewall.checkrange("12-21",10))
		#self.assertTrue(firewall.checkrange("0-12030303020202", 2))
	def test_match_ips (self):
		args = "/Users/kipkoech/Desktop/illumio/Workbook1.csv"
		firewall = Firewall(args)
		self.assertTrue(firewall.accept('inbound','tcp','80','192.168.1.2'))

		self.assertTrue(firewall.match_ips('192.168.1.1- 192.168.2.5', '192.168.1.'))
		self.assertTrue(firewall.match_ips('192.168.1.1- 192.168.2.5', '192.168.1.2'))

	def test_accept(self):
		args = "/Users/kipkoech/Desktop/illumio/Workbook1.csv"
		args = "/Users/kipkoech/Desktop/illumio/Workbook1.csv"
		self.assertTrue(firewall.accept('inbound','tcp','80','192.168.1.2'))
		self.assertFalse(firewall.accept('inbound','udp','80','192.168.1.2'))
		self.assertTrue(firewall.accept('outbound','udp','1500','52.12.48.92'))





if __name__ == '__main__':
    unittest.main()
