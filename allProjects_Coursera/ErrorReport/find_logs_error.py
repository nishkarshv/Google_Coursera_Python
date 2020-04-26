#!/usr/bin/env python3
import csv
import re
import operator

# dictionaries
error = {}
per_user= {}
errorcountperuser = {}
infocountperuser = {}
with open('syslog.log', 'r') as f:
    reads = f.readlines()
    for line in reads:
        if re.search("ERROR ([\w ]*) ([(\w)]*)", line):
            errorkey = re.search("ERROR ([\w ]*) ([(\w)]*)", line).group(1)
            errusername = re.findall(r"\((.*)\)", line)[0]
            #errusername = re.search("ERROR ([\w ]*) ([(\w)]*)", line).group(2)
            if errorkey not in error:
                error[errorkey] = 1
            else:
                error[errorkey]+=1
            if errusername not in errorcountperuser:
                errorcountperuser[errusername] = 1
            else:
                errorcountperuser[errusername] +=1
        elif re.search("INFO ([\w ]*) ([(\w)]*)", line):
            infokey = re.search("INFO ([\w ]*) ([(\w)]*)", line).group(2)
            infusername = re.findall(r"\((.*)\)", line)[0]
            #infusername = re.search("INFO ([\w ]*) ([(\w)]*)", line).group(1)
            if infusername not in infocountperuser:
                infocountperuser[infusername] = 1
            else:
                infocountperuser[infusername]+=1
combdict = {}
for k,v in infocountperuser.items():
    if k not in combdict:
        combdict[k] = (v, errorcountperuser[k])
    else:
        pass
#print(combdict)
#print(errorcountperuser)
errorsorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
combsorted = sorted(combdict.items(), key = operator.itemgetter(0))
#print(combsorted)
listoftuple = []
for items in combsorted:
    key = items[0]
    val1 = items[1][0]
    val2 = items[1][1]
    listoftuple.append((key, val1, val2))
print(listoftuple)
with open('error_message.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['Error','Count'])
    for row in errorsorted:
        csv_out.writerow(row)
with open('user_statistics.csv','w') as out1:
    csv_out=csv.writer(out1)
    csv_out.writerow(['Username','INFO','ERROR'])
    for row in listoftuple:
        csv_out.writerow(row)