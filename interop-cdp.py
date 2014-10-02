#!/usr/bin/env python

import xmltodict
from device import Device

if __name__ == "__main__":

	switch = Device(ip='192.168.200.50')

	switch.open()

	my_data = switch.show('show cdp neighbors')
	
	result = xmltodict.parse(my_data[1])

	cdp_table = result['ins_api']['outputs']['output']['body'] \
		['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']
			
	for each_neighbor in cdp_table:
		print '=' * 40
		for key, value in each_neighbor.iteritems():
			if key == 'intf_id': print 'Local Interface: ', value
			if key == 'device_id': print 'Neighbor: ', value
			if key == 'port_id': print 'Neighbor Interface: ', value
	print '=' * 40
