#!/usr/local/bin/python3.2
import re,argparse,sys,os
from argparse import RawTextHelpFormatter
parser=argparse.ArgumentParser(description='create new info file using old info & new source', formatter_class=RawTextHelpFormatter)
parser.add_argument('-i', dest='i_', help="info file as input", default='null')
parser.add_argument('-o', dest='o_', help="output processed info file", default='null')
inputs = parser.parse_args()
i_info=inputs.i_
o_info=inputs.o_
statement="null"
if i_info=="null" and p_info=="null":
	print("Please specify input info file & output file name")
	os.system(os.path.realpath(__file__)+" -h")
	#print(./os.path.realpath(__file__) -h)
	sys.exit()
oi=open(o_info,'w+')
oi.close()
oi=open(o_info,'a')
try:
	ii=open(i_info, 'r')
except IOError:
	print("Error in accessing info file")
	sys.exit()
for line in ii:
	#if os.path.exists(line.split('\n')[0].rstrip()):
	if "SF:" in line:
		if os.path.exists((line.split(':')[1].rstrip()).split('\n')[0].rstrip()):
			oi.write("TN:\n")
			line_1=ii.readline()
			while line_1!="end_of_record\n":
				oi.write(line_1)
			if line_1=="end_of_record\n":
				oi.write(line_1)
				continue
	else:
		print("No"+line)
ii.close()
oi.close()
