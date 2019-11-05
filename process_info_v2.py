#!/usr/local/bin/python3.2
import re,argparse,sys,os, shutil
from argparse import RawTextHelpFormatter
#for l in os.listdir("new_c"):
#	print(l)
parser=argparse.ArgumentParser(description='create new info file using old info & new source', formatter_class=RawTextHelpFormatter)
parser.add_argument('-i', dest='i_', help="old info file as input", default='null')
parser.add_argument('-o', dest='o_', help="Directory where new c files storedname for output info file after processing", default='null')
parser.add_argument('-oc', dest='oc_', help="Directory where old c files stored", default='null')
parser.add_argument('-nc', dest='nc_', help="Directory where new c files stored", default='null')
parser.add_argument('-list', dest='list_', help="Text file contaning list of all c file needs to be processed. use getlistc.py to get this text file.", default='null')
inputs = parser.parse_args()
oi=inputs.i_
ni=inputs.o_
oc=inputs.oc_
nc=inputs.nc_
clist=inputs.list_
if oi=="null" and ni=="null":
	print("Please specify input info file & output file name")
	os.system(os.path.realpath(__file__)+" -h")
	#print(./os.path.realpath(__file__) -h)
	sys.exit()

#pi=open(newi,'w+')
#pi.close()
#pi=open(newi,'a')
#if [word for word in " *uraj bachchuwar".split(" ")[0] if word.startswith('*')]:

#while occ_line!="end_of_record":
#	if "};" in occ_line:
#		occ.write(occ_line.split("\n")[0].rstrip()+"replaced");
#		break;
#	occ_line=occ.readline()

#occ.close()


#sys.exit()
def occread():
	try:	
		occ=open("_occ_.txt",'r')
	except IOError:
		print("unable to open file : _occ_.txt")
		sys.exit
def occwrite():
	try:	
		occ=open("_occ_.txt",'w')
	except IOError:
		print("unable to open file : _occ_.txt")
		sys.exit
	
LF=LH=FNF=FNH=i=oiline=niline=oiline_it=BRF=BRH=occured=occ_t=linedone=ocstatement_occ_t=ocstatement_occ_c_da=ocstatement_occ_c_brda=ocstatement_occ_c_fn=which_ocstatement=0
last_brda_oiline=0
last_brda_niline=0
ocstatement=ncstatement="null"
clistp=open(clist,'r')
for clistp_i in clistp:
	if "end_of_record" in clistp_i:
		break
	cfile=clistp_i.split("\n")[0].rstrip()
	print(cfile)
	try:	
		oc_file=open(oc+"/"+cfile,'r')
	except IOError:
		print("unable to open file : " + oc+"/"+cfile)
		continue
	try:	
		nc_file=open(nc+"/"+cfile,'r')
	except IOError:
		print("unable to open file : " + nc+"/"+cfile)
		continue
	#create & open new info with the name of cfile
	try:	
		ni_file=open(ni+"/"+cfile+".info",'w+')
	except IOError:
		print("unable to open file : " + ni+"/"+cfile)
		sys.exit
	ni_file.close()
	try:	
		ni_file=open(ni+"/"+cfile+".info",'a')
	except IOError:
		print("unable to open file : " + ni+"/"+cfile)
		sys.exit
	ni_file.write("TN:\n")
	# Get all lines with its occurence number if it occured more than once
	#first create _occ_.txt file
	occ=open("_occ_.txt",'w+')
	occ.close()
	
	
	for cfileline in oc_file:
		cfileline_t=cfileline.split("\n")[0].rstrip()
		if "#" in cfileline:
			continue
		try:	
			occ2=open("_occ_.txt",'r')
		except IOError:
			print("unable to open file : _occ_.txt")
			sys.exit
		for l2 in occ2:
			print("hi"+l2)
			if cfileline_t==l2.split("::::")[0].rstrip():
				#already done for cfileline
				linedone=1;
				
				break
		if linedone==1:
			linedone=0;
			occ2.close()
			continue
		occ2.close()
		#print("counting occurenc for"+cfileline_t)
		occ_t=0
		try:	
			oc_file2=open(oc+"/"+cfile,'r')
		except IOError:
			print("unable to open file : " + cfile)
			sys.exit
		
		
		for l1 in oc_file2:
			if cfileline_t in l1:
				occ_t+=1
				
		if occ_t>1:
			#print(cfileline_t+"occured"+str(occ_t)+"times")
			try:
				occ=open("_occ_.txt",'a')
			except IOError:
				print("unable to open file : " + "_occ_.txt")
				sys.exit
			#occ.write(cfileline_t+"::::"+str(occ_t)+"::::"+str(occ_t)+"::::\n")
			occ.write(cfileline_t+"::::"+str(occ_t)+"::::"+str(occ_t)+"::::"+str(occ_t)+"::::"+str(occ_t)+"::::\n")#line:Total:DA:BRDA:FN
			occ.close()
		oc_file2.close()
	#occ.close()
	#sys.exit()
	
	try:
		occ=open("_occ_.txt",'a')
	except IOError:
		print("unable to open file : " + "_occ_.txt")
		sys.exit
	occ.write("end_of_record")
	occ.close()
	#oc_file.close()
	oc_file.seek(0,0)
	#sys.exit()
	print("old info directory: "+oi)
	#search cfile in each info & process
	for _info in os.listdir(oi):
		try:
			oi_file=open(oi+"/"+_info, 'r')
			print("open file : " + oi+"/"+_info)
		except IOError:
			print("unable to open file : " + oi+"/"+_info)
			sys.exit()
		if not cfile in oi_file.read():
			oi_file.close()
			print(cfile+" c is not in info")
			continue #If cfile is not in this oi_file then continuw searching in next oi
		print("got "+cfile+" in "+oi+"/"+_info)
		oi_file.seek(0,0)	
		for line in oi_file:
			if cfile in line:
				#cfile is found at line
				print("cfile is found at line")
				ni_file.write(line)
				line_1=oi_file.readline()
				while line_1!="end_of_record\n":
					
					if "LH" in line_1:
						ni_file.write("LH:"+str(LH)+"\n"+"end_of_record\n")
						LH=0
					if "LF" in line_1:
						ni_file.write("LF:"+str(LF)+"\n")
						LF=0
					#global LF,LH,FNF,FNH,i,oiline,oiline_it,niline,ocstatement,ncstatement,BRF,BRH,ocstatement_occ_t,ocstatement_occ_c
					if "BRH" in line_1:
						ni_file.write("BRH:"+str(BRH)+"\n")
						BRH=0
					if "BRF" in line_1:
						ni_file.write("BRF:"+str(BRF)+"\n")
						BRF=0
					if "FNH" in line_1:
						ni_file.write("FNH:"+str(FNH)+"\n")
						FNH=0
					if "FNF" in line_1:
						ni_file.write("FNF:"+str(FNF)+"\n")
						FNF=0
					if "FNDA" in line_1:
						ni_file.write(line_1)
						FNF+=1
						if int(re.findall(r'\:(.*?)\,',line_1)[0])>0:
							FNH+=1
					#-------FN processing
					if "FN" in line_1 and "FNDA" not in line_1 and "FNH" not in line_1 and "FNF" not in line_1:
						print("processing FN statements")
						oiline=(line_1.split(',')[0].rstrip()).split(':')[1].rstrip()#DA line no.
						oiline_it=(line_1.split("\n")[0].rstrip()).split(",")[1]#executed iteration of #DA line no.
						print("DA oiline is"+oiline)
						
						i=1
						while(i<int(oiline)):
							oc_file.readline()
							i+=1
						ocstatement=oc_file.readline()
						oc_file.seek(0,0)
						#--
						i=0
						which_ocstatement=-1
						while(i<int(oiline)):
							searchl=oc_file.readline()
							if ocstatement==searchl:
								which_ocstatement+=1
							i+=1
						oc_file.seek(0,0)
						print("which_ocstatement"+str(which_ocstatement))
						print("looking for"+ocstatement)
						ocstatement_t=ocstatement.split("\n")[0].rstrip()
						try:	
							occ=open("_occ_.txt",'r')
						except IOError:
							print("unable to open file : _occ_.txt")
							sys.exit
						is_ocstatement_in_occ=0
						for occline in occ:
							#if ocstatement_t in occline:
							if ocstatement_t==occline.split("::::")[0].rstrip():
								occ.seek(0,0)
								
								ocstatement_occ_t=occline.split("::::")[1].rstrip()# Total occurence
								ocstatement_occ_c_da=occline.split("::::")[2].rstrip()#current occurence
								#ocstatement_occ_c_da=occline.split("::::")[2].rstrip()#current DA occurence
								ocstatement_occ_c_brda=occline.split("::::")[3].rstrip()#current BRDA occurence
								ocstatement_occ_c_fn=occline.split("::::")[4].rstrip()#current FN occurence
								occline_t=occline
								is_ocstatement_in_occ=1
								break
						occ.close()
						i=1
				#-----------	
						if which_ocstatement>0 and is_ocstatement_in_occ==1:
							ocstatement_occ_c_fn=int(ocstatement_occ_t)-which_ocstatement
				#---------
						ncstatement=nc_file.readline()
						ncstatement_occ=0
						#--
						#if int(ocstatement_occ_c_da)==int(ocstatement_occ_t):
						#	ncstatement_occ=0-which_ocstatement
						#else:
						#	ncstatement_occ=0
						
						while ncstatement!="":
							if ocstatement==ncstatement :	
								print("Found "+ocstatement+"in c at "+str(i))
								if is_ocstatement_in_occ==1:						
									if ncstatement_occ==(int(ocstatement_occ_t)-int(ocstatement_occ_c_fn)):
										niline=i
										break
								else:
									niline=i
									break
								ncstatement_occ+=1
							#ncstatement=nc.readline()
							i+=1
							ncstatement=nc_file.readline()
						nc_file.seek(0,0)
						i=1
						print(ncstatement+"is at line: "+str(niline))
						if ncstatement==ocstatement:
							
							#reduce ocstatement_occ_c_da by 1& write back in file 
							if is_ocstatement_in_occ==1:
								ocstatement_occ_c_fn=int(ocstatement_occ_c_fn)-1
								try:	
									occ=open("_occ_.txt",'r')
								except IOError:
									print("unable to open file : _occ_.txt")
									sys.exit
								occ_contentcopy=occ.read()
								occ.close()
								#occ_contentpaste=occ_contentcopy.replace(occline_t,ocstatement_t+"::::"+str(ocstatement_occ_t)+"::::"+str(ocstatement_occ_c_da)+"::::\n")		
								occ_contentpaste=occ_contentcopy.replace(occline_t,ocstatement_t+"::::"+str(ocstatement_occ_t)+"::::"+str(ocstatement_occ_c_da)+"::::"+str(ocstatement_occ_c_brda)+"::::"+str(ocstatement_occ_c_fn)+"::::\n")	
								try:	
									occ=open("_occ_.txt",'w')
								except IOError:
									print("unable to open file : _occ_.txt")
									sys.exit
								occ.write(occ_contentpaste)
								occ.close()
								ocstatement_occ_t=0
								ocstatement_occ_c_fn=0
								occline_t=0
							print("Found statement in new source")
				
							print("In new c file ocstatement is at line number: "+str(niline))
							#Add niline in new info
							ni_file.write("FN:"+str(niline)+","+str(oiline_it)+"\n")
						else:
							print("statement is missing in new source: "+ ocstatement)
					#------BRDA Processing
					if "BRDA" in line_1:
						print("processing BRDA statements")
						oiline=(line_1.split(',')[0].rstrip()).split(':')[1].rstrip()#BRDA line no.
						
						print("oiline is"+oiline)
						oiline_it=(line_1.split("\n")[0].rstrip()).split(",")[3]#executed iteration of #BRDA line no.
						i=1
						if int(last_brda_oiline)!=int(oiline):
							while(i<int(oiline)):
								oc_file.readline()
								i+=1
							ocstatement=oc_file.readline()
							oc_file.seek(0,0)
							#--
							i=0
							which_ocstatement=-1
							while(i<int(oiline)):
								searchl=oc_file.readline()
								if ocstatement==searchl:
									which_ocstatement+=1
								i+=1
							oc_file.seek(0,0)
							print("which_ocstatement"+str(which_ocstatement))
							print("looking for"+ocstatement)
							ocstatement_t=ocstatement.split("\n")[0].rstrip()
							try:	
								occ=open("_occ_.txt",'r')
							except IOError:
								print("unable to open file : _occ_.txt")
								sys.exit
							is_ocstatement_in_occ=0
							for occline in occ:
								#if ocstatement_t in occline:
								if ocstatement_t==occline.split("::::")[0].rstrip():
									occ.seek(0,0)
								
									ocstatement_occ_t=occline.split("::::")[1].rstrip()# Total occurence
									ocstatement_occ_c_da=occline.split("::::")[2].rstrip()#current DA occurence
									ocstatement_occ_c_brda=occline.split("::::")[3].rstrip()#current BRDA occurence
									ocstatement_occ_c_fn=occline.split("::::")[4].rstrip()#current FN occurence
									occline_t=occline
									is_ocstatement_in_occ=1
									break
							occ.close()
							i=1
					#-----------	
							if which_ocstatement>0 and is_ocstatement_in_occ==1:
								ocstatement_occ_c_brda=int(ocstatement_occ_t)-which_ocstatement
					#---------
							ncstatement=nc_file.readline()
							ncstatement_occ=0
							#--
							#if int(ocstatement_occ_c_brda)==int(ocstatement_occ_t):
							#	ncstatement_occ=0-which_ocstatement
							#else:
							#	ncstatement_occ=0
						
							while ncstatement!="":
								if ocstatement==ncstatement :	
									if is_ocstatement_in_occ==1:						
										if ncstatement_occ==(int(ocstatement_occ_t)-int(ocstatement_occ_c_brda)):
											niline=i
											break
									else:
										niline=i
										break
									ncstatement_occ+=1
								#ncstatement=nc.readline()
								i+=1
								ncstatement=nc_file.readline()
							nc_file.seek(0,0)
							i=1
						else:
							niline=last_brda_niline
						print(ncstatement+"is at line: "+str(niline))
						if ncstatement==ocstatement:
							
							#reduce ocstatement_occ_c_brda by 1& write back in file 
							if int(ocstatement_occ_t)>0 and int(last_brda_oiline)!=int(oiline) and is_ocstatement_in_occ==1:
								ocstatement_occ_c_brda=int(ocstatement_occ_c_brda)-1
								try:	
									occ=open("_occ_.txt",'r')
								except IOError:
									print("unable to open file : _occ_.txt")
									sys.exit
								occ_contentcopy=occ.read()
								occ.close()
								occ_contentpaste=occ_contentcopy.replace(occline_t,ocstatement_t+"::::"+str(ocstatement_occ_t)+"::::"+str(ocstatement_occ_c_da)+"::::"+str(ocstatement_occ_c_brda)+"::::"+str(ocstatement_occ_c_fn)+"::::\n")			
								try:	
									occ=open("_occ_.txt",'w')
								except IOError:
									print("unable to open file : _occ_.txt")
									sys.exit
								occ.write(occ_contentpaste)
								occ.close()
								ocstatement_occ_t=0
								ocstatement_occ_c_brda=0
								occline_t=0
							print("Found statement in new source")
				
							print("In new c file ocstatement is at line number: "+str(niline))
							#Add niline in new info
							ni_file.write("BRDA:"+str(niline)+","+str(line_1.split(',')[1].rstrip())+","+str(line_1.split(',')[2].rstrip())+","+str(oiline_it)+"\n")
							BRF+=1
							if oiline_it.isdigit() and int(oiline_it)>0:
								BRH+=1
						else:
							print("statement is missing in new source: "+ ocstatement)
						last_brda_oiline=oiline
						last_brda_niline=niline

					if "DA" in line_1 and "FNDA" not in line_1 and "BRDA" not in line_1:
						print("processing DA statements")
						oiline=(line_1.split(',')[0].rstrip()).split(':')[1].rstrip()#DA line no.
						print("DA oiline is"+oiline)
						oiline_it=(line_1.split("\n")[0].rstrip()).split(",")[1]#executed iteration of #DA line no.
						i=1
						while(i<int(oiline)):
							oc_file.readline()
							i+=1
						ocstatement=oc_file.readline()
						oc_file.seek(0,0)
						#--
						i=0
						which_ocstatement=-1
						while(i<int(oiline)):
							searchl=oc_file.readline()
							if ocstatement==searchl:
								which_ocstatement+=1
							i+=1
						oc_file.seek(0,0)
						print("which_ocstatement"+str(which_ocstatement))
						print("looking for"+ocstatement)
						ocstatement_t=ocstatement.split("\n")[0].rstrip()
						try:	
							occ=open("_occ_.txt",'r')
						except IOError:
							print("unable to open file : _occ_.txt")
							sys.exit
						is_ocstatement_in_occ=0
						for occline in occ:
							#if ocstatement_t in occline:
							if ocstatement_t==occline.split("::::")[0].rstrip():
								occ.seek(0,0)
								
								ocstatement_occ_t=occline.split("::::")[1].rstrip()# Total occurence
								ocstatement_occ_c_da=occline.split("::::")[2].rstrip()#current occurence
								#ocstatement_occ_c_da=occline.split("::::")[2].rstrip()#current DA occurence
								ocstatement_occ_c_brda=occline.split("::::")[3].rstrip()#current BRDA occurence
								ocstatement_occ_c_fn=occline.split("::::")[4].rstrip()#current FN occurence
								occline_t=occline
								is_ocstatement_in_occ=1
								break
						occ.close()
						i=1
				#-----------	
						if which_ocstatement>0 and is_ocstatement_in_occ==1:
							ocstatement_occ_c_da=int(ocstatement_occ_t)-which_ocstatement
				#---------
						ncstatement=nc_file.readline()
						ncstatement_occ=0
						#--
						#if int(ocstatement_occ_c_da)==int(ocstatement_occ_t):
						#	ncstatement_occ=0-which_ocstatement
						#else:
						#	ncstatement_occ=0
						
						while ncstatement!="":
							if ocstatement==ncstatement :	
								print("Found "+ocstatement+"in c at "+str(i))
								if is_ocstatement_in_occ==1:						
									if ncstatement_occ==(int(ocstatement_occ_t)-int(ocstatement_occ_c_da)):
										niline=i
										break
								else:
									niline=i
									break
								ncstatement_occ+=1
							#ncstatement=nc.readline()
							i+=1
							ncstatement=nc_file.readline()
						nc_file.seek(0,0)
						i=1
						print(ncstatement+"is at line: "+str(niline))
						if ncstatement==ocstatement:
							
							#reduce ocstatement_occ_c_da by 1& write back in file 
							if is_ocstatement_in_occ==1:
								ocstatement_occ_c_da=int(ocstatement_occ_c_da)-1
								try:	
									occ=open("_occ_.txt",'r')
								except IOError:
									print("unable to open file : _occ_.txt")
									sys.exit
								occ_contentcopy=occ.read()
								occ.close()
								#occ_contentpaste=occ_contentcopy.replace(occline_t,ocstatement_t+"::::"+str(ocstatement_occ_t)+"::::"+str(ocstatement_occ_c_da)+"::::\n")		
								occ_contentpaste=occ_contentcopy.replace(occline_t,ocstatement_t+"::::"+str(ocstatement_occ_t)+"::::"+str(ocstatement_occ_c_da)+"::::"+str(ocstatement_occ_c_brda)+"::::"+str(ocstatement_occ_c_fn)+"::::\n")	
								try:	
									occ=open("_occ_.txt",'w')
								except IOError:
									print("unable to open file : _occ_.txt")
									sys.exit
								occ.write(occ_contentpaste)
								occ.close()
								ocstatement_occ_t=0
								ocstatement_occ_c_da=0
								occline_t=0
							print("Found statement in new source")
				
							print("In new c file ocstatement is at line number: "+str(niline))
							#Add niline in new info
							ni_file.write("DA:"+str(niline)+","+str(oiline_it)+"\n")
							LF+=1
							if int(oiline_it)>0:
								LH+=1
						else:
							print("statement is missing in new source: "+ ocstatement)

					line_1=oi_file.readline()
					print(line_1)
		oi_file.close()
		last_brda_oiline=0
		last_brda_niline=0
		#reset occ for next run
		shutil.copyfile("_occ_.txt","_occ_temp.txt")
		occ=open("_occ_.txt",'w+')
		occ.close()
		try:
			occ=open("_occ_.txt",'a')
		except IOError:
			print("unable to open file : " + "_occ_.txt")
		
		try:
			occt=open("_occ_temp.txt",'r')
		except IOError:
			print("unable to open file : " + "_occ_temp.txt")
		for eachline in occt:
			if not "end_of_record" in eachline:
				#occ.write(eachline.split("::::")[0].rstrip()+"::::"+eachline.split("::::")[1].rstrip()+"::::"+eachline.split("::::")[1].rstrip()+"\n")
				occ.write(eachline.split("::::")[0].rstrip()+"::::"+eachline.split("::::")[1].rstrip()+"::::"+eachline.split("::::")[1].rstrip()+"::::"+eachline.split("::::")[1].rstrip()+"::::"+eachline.split("::::")[1].rstrip()+"\n")
		occ.write("end_of_record")
		occt.close()
		occ.close()
		
	ni_file.close()
sys.exit()
for l in os.listdir(nc_):
	print(l)
	try:	
		nc=open(nc_+"/"+l,'r')
	except IOError:
		print("unable to open file : " + nc_)
		continue
	try:
		oc=open(oc_+"/"+l,'r')
	except IOError:
		print("unable to open file : " + oc_)
		continue
	try:
		oi=open(oldi, 'r')
	except IOError:
		print("unable to open file : " + oldi)
		sys.exit()
	
	for line in oi:
		tmp1=open("occured_temp.txt",'w+')
		tmp1.close()
		tmp1=open("occured_temp.txt",'a')
		if l in line:
			print(line)
			pi.write("TN:\n"+line)
			line_1=oi.readline()
			while line_1!="end_of_record\n":
				def getdata():
					global LF,LH,FNF,FNH,i,oiline,oiline_it,niline,ocstatement,ncstatement,BRF,BRH
					oiline=re.findall(r'\:(.*?)\,',line_1)[0]
					#oiline_it=re.findall(r'\,(.*?)',line_1)[0]
					#print([int(s) for s in line_1.split(',') if s.isdigit()])
					if "BRDA" in line_1:
						oiline_it=line_1.split(',')[3].rstrip()
					else:
						oiline_it=line_1.split(',')[1].rstrip()
					print("line number in old info is :"+oiline)#This is line number in old info
					print("executed number: "+oiline_it)
					#list1=re.findall(r'\:(.*?)\,',line_1)
					#print(list1[0])
					#print(re.match(r'\:(.*?)\,',line_1))
					#Start searching for statement which is at oiline number in old c file
					i=1
					while(i<int(oiline)):
						oc.readline()
						i+=1
					ocstatement=oc.readline()
					#check how many times ocstatement is repeated in oldc
					searchline=oc.readline()
					while searchline!="end_of_record\n":
						searchline=oc.readline()
						if ocstatement==searchline:
							occured+=1
					oc.seek(0,0)
					print("statement at oiline in old c is :"+ocstatement)
					#find line number of ocstatement in new c file
					i=1
					ncstatement=nc.readline()
					while ncstatement!="" and ocstatement!=ncstatement:
						i+=1
						ncstatement=nc.readline()
					niline=i
					print("niline is: "+str(niline))
					nc.seek(0,0)

				if "LH" in line_1:
					pi.write("LH:"+str(LH)+"\n"+"end_of_record\n")
					LH=0
				if "LF" in line_1:
					pi.write("LF:"+str(LF)+"\n")
					LF=0

				if "DA" in line_1 and "FNDA" not in line_1 and "BRDA" not in line_1:
					#pi.write(line_1)
					#print(line_1)
					getdata()
						
					if ncstatement==ocstatement:
						print("Found statement in new source")
						
						print("In new c file ocstatement is at line number: "+str(niline))
						#Add niline in new info
						pi.write("DA:"+str(niline)+","+str(oiline_it)+"\n")
						LF+=1
						if int(oiline_it)>0:
							LH+=1
					else:
						print("statement is missing in new source: "+ ocstatement)
					#niline=i
					#print("In new c file ocstatement is at line number: "+str(niline))
					#Add niline in new info
					#pi.write("DA:"+str(niline)+","+oiline_it+"\n")

					
					
				line_1=oi.readline()
	oi.close()
	nc.close()
	oc.close()
	#pi.write("LF:"+str(LF)+"\n"+"LH:"+str(LH)+"\nend_of_record\n")
