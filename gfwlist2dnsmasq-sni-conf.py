#!/usr/bin/env python  
#coding=utf-8
#  
# This Code based on https://github.com/cokebar/gfwlist2dnsmasq
#  
# Copyright (C) 2014 http://www.shuyz.com   
# Ref https://github.com/gfwlist/gfwlist
#
#
#Use to convert gfwlist to dnsmasq's sni configure file.
#
#

import urllib2 
import re
import os
import datetime
import base64
import shutil

#Your SNI Proxy Server IP here!
sni = '127.0.0.1'



# the url of gfwlist
baseurl = 'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt'
# match comments/title/whitelist/ip address
comment_pattern = '^\!|\[|^@@|^\d+\.\d+\.\d+\.\d+'
domain_pattern = '([\w\-\_]+\.[\w\.\-\_]+)[\/\*]*' 
tmpfile = '/tmp/gfwlisttmp'
# do not write to router internal flash directly
outfile = './sni.conf'
#outfile = './dnsmasq_list.conf'
 
fs =  file(outfile, 'w')
fs.write('# gfw list sni rules for dnsmasq\n')
fs.write('# updated on ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
fs.write('#\n')
 
print 'fetching list...'
content = urllib2.urlopen(baseurl, timeout=15).read().decode('base64')
 
# write the decoded content to file then read line by line
tfs = open(tmpfile, 'w')
tfs.write(content)
tfs.close()
tfs = open(tmpfile, 'r')
 
print 'page content fetched, analysis...'
 
# remember all blocked domains, in case of duplicate records
domainlist = []

 
for line in tfs.readlines():	
	if re.findall(comment_pattern, line):
		print 'this is a comment line: ' + line
		#fs.write('#' + line)
	else:
		domain = re.findall(domain_pattern, line)
		if domain:
			try:
				found = domainlist.index(domain[0])
				print domain[0] + ' exists.'
			except ValueError:
				print 'saving ' + domain[0]
				domainlist.append(domain[0])
				fs.write('address=/%s/%s\n'%(domain[0],sni))

		else:
			print 'no valid domain in this line: ' + line
					
tfs.close()

fs.close();
 
print 'done!'
