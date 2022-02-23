import pathlib
import urllib.request;
import re; 
from collections import Counter;

file = pathlib.Path("./http_access_log.txt")
if file.exists ():
    print ("Loading")
else:
    print ("Download is starting")
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url, "./http_access_log.txt")
a1 = 0; a2 =0; a3 = 0; a4 =0; a5 = 0; a6 =0; a7 = 0;
with open("./http_access_log.txt", "r") as fp:
  for line in fp:
    if re.search('(24/Oct/1994|31/Oct/1994|07/Nov/|14/Nov/|21/Nov/|28/Nov/|05/Dec/|12/Dec/|19/Dec/|26/Dec/|02/jan/|09/Jan/|16/Jan/|23/Jan/|30/Jan/|06/Feb/|13/Feb/|20/Feb/|27/Feb/|06/Mar/|13/Mar/|20/Mar/|27/Mar/|03/Apr/|10/Apr/|17/Apr/|24/Apr/|01/May/|08/May/|15/May/|22/May/|29/May/|05/Jun/|12/Jun/|19/Jun/|26/Jun/|03/Jul/|10/Jul/|17/Jul/|24/Jul/|31/Jul/|07/Aug/|14/Aug/|21/Aug/|28/Aug/|04/Sep/|11/Sep/|18/Sep/|25/Sep/|02/Oct/1995|09/Oct/1995)', line):
     a1 += 1
    if re.search('(25/Oct/1994|01/Nov/|08/Nov/|15/Nov/|22/Nov/|29/Nov/|06/Dec/|13/Dec/|20/Dec/|27/Dec/|03/jan/|10/Jan/|17/Jan/|24/Jan/|31/Jan/|07/Feb/|14/Feb/|21/Feb/|28/Feb/|07/Mar/|14/Mar/|21/Mar/|28/Mar/|04/Apr/|11/Apr/|18/Apr/|25/Apr/|02/May/|09/May/|16/May/|23/May/|30/May/|06/Jun/|13/Jun/|20/Jun/|27/Jun/|04/Jul/|11/Jul/|18/Jul/|25/Jul/|01/Aug/|08/Aug/|15/Aug/|22/Aug/|29/Aug/|05/Sep/|12/Sep/|19/Sep/|26/Sep/|03/Oct/1995|10/Oct/1995)', line):
     a2 += 1
    if re.search('(26/Oct/1994|02/Nov/|09/Nov/|16/Nov/|23/Nov/|30/Nov/|07/Dec/|14/Dec/|21/Dec/|28/Dec/|04/jan/|11/Jan/|18/Jan/|25/Jan/|01/Feb/|08/Feb/|15/Feb/|22/Feb/|01/Mar/|08/Mar/|15/Mar/|22/Mar/|29/Mar/|05/Apr/|12/Apr/|19/Apr/|26/Apr/|03/May/|10/May/|17/May/|24/May/|31/May/|07/Jun/|14/Jun/|21/Jun/|28/Jun/|05/Jul/|12/Jul/|19/Jul/|26/Jul/|02/Aug/|09/Aug/|16/Aug/|23/Aug/|30/Aug/|06/Sep/|13/Sep/|20/Sep/|27/Sep/|04/Oct/1995|11/Oct/1995)', line):
     a3 += 1
    if re.search('(27/Oct/1994|03/Nov/|10/Nov/|17/Nov/|24/Nov/|01/Dec/|08/Dec/|15/Dec/|22/Dec/|29/Dec/|05/jan/|12/Jan/|19/Jan/|26/Jan/|02/Feb/|09/Feb/|16/Feb/|23/Feb/|02/Mar/|09/Mar/|16/Mar/|23/Mar/|30/Mar/|06/Apr/|13/Apr/|20/Apr/|27/Apr/|04/May/|11/May/|18/May/|25/May/|01/Jun/|08/Jun/|15/Jun/|22/Jun/|29/Jun/|06/Jul/|13/Jul/|20/Jul/|27/Jul/|03/Aug/|10/Aug/|17/Aug/|24/Aug/|31/Aug/|07/Sep/|14/Sep/|21/Sep/|28/Sep/|05/Oct/1995)', line):
     a4 += 1
    if re.search('(28/Oct/1994|04/Nov/|11/Nov/|18/Nov/|25/Nov/|02/Dec/|09/Dec/|16/Dec/|23/Dec/|30/Dec/|06/jan/|13/Jan/|20/Jan/|27/Jan/|03/Feb/|10/Feb/|17/Feb/|24/Feb/|03/Mar/|10/Mar/|17/Mar/|24/Mar/|31/Mar/|07/Apr/|14/Apr/|21/Apr/|28/Apr/|05/May/|12/May/|19/May/|26/May/|02/Jun/|09/Jun/|16/Jun/|23/Jun/|30/Jun/|07/Jul/|14/Jul/|21/Jul/|28/Jul/|04/Aug/|11/Aug/|18/Aug/|25/Aug/|01/Sep/|08/Sep/|15/Sep/|22/Sep/|29/Sep/|06/Oct/1995)', line):
     a5 += 1
    if re.search('(29/Oct/1994|05/Nov/|12/Nov/|19/Nov/|26/Nov/|03/Dec/|10/Dec/|17/Dec/|24/Dec/|31/Dec/|07/jan/|14/Jan/|21/Jan/|28/Jan/|04/Feb/|11/Feb/|18/Feb/|25/Feb/|04/Mar/|11/Mar/|18/Mar/|25/Mar/|01/Apr/|08/Apr/|15/Apr/|22/Apr/|29/Apr/|06/May/|13/May/|20/May/|27/May/|03/Jun/|10/Jun/|17/Jun/|24/Jun/|01/Jul/|08/Jul/|15/Jul/|22/Jul/|29/Jul/|05/Aug/|12/Aug/|19/Aug/|26/Aug/|02/Sep/|09/Sep/|16/Sep/|23/Sep/|30/Sep/|07/Oct/1995)', line):
     a6 += 1
    if re.search('(30/Oct/1994|06/Nov/|13/Nov/|20/Nov/|27/Nov/|04/Dec/|11/Dec/|18/Dec/|25/Dec/|01/Jan/|08/jan/|15/Jan/|22/Jan/|29/Jan/|05/Feb/|12/Feb/|19/Feb/|26/Feb/|05/Mar/|12/Mar/|19/Mar/|26/Mar/|02/Apr/|09/Apr/|16/Apr/|23/Apr/|30/Apr/|07/May/|14/May/|21/May/|28/May/|04/Jun/|11/Jun/|18/Jun/|25/Jun/|02/Jul/|09/Jul/|16/Jul/|23/Jul/|30/Jul/|06/Aug/|13/Aug/|20/Aug/|27/Aug/|03/Sep/|10/Sep/|17/Sep/|24/Sep/|01/Oct/|08/Oct/1995)', line):
     a7 += 1
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("+	    Each day's average of the week		+")
print("++++++++++++++++++++++++++++++++++++++++++++++")			
print("Average for Monday", round(a1/51,2))
print("Average for Tuesday", round(a2/51,2))
print("Average for Wednesday", round(a3/51,2))
print("Average for Thursday", round(a4/50,2))
print("Average for Friday", round(a5/50,2))
print("Average for Saturday", round(a6/50,2))
print("Average for Sunday", round(a7/50,2))
print("______________________________________")
b1 = 0; b2 =0; b3 = 0; b4 =0; b5 = 0; b6 =0; b7 = 0; b8 =0; b9 = 0; b10 =0; b11 = 0; b12 =0; b13 = 0; 
b14 =0; b15 = 0; b16 =0; b17 = 0; b18 =0; b19 = 0; b20 =0; b21 = 0; b22 =0; b23 = 0; b24 =0; b25 = 0;
b25 =0; b26 = 0; b27 =0; b28 = 0; b29 =0; b30 = 0; b31 =0; b32 = 0; b33 =0; b34 = 0; b35 =0; b36 = 0;
b37 =0; b38 = 0; b39 =0; b40 = 0; b41 =0; b42 = 0; b43 =0; b44 = 0; b45 =0; b46 = 0; b47 =0; b48 = 0;
b49 =0; b50 = 0; b51 =0; 
with open("./http_access_log.txt", "r") as fp:
  for line in fp:
    if re.search('(24/Oct/1994|25/Oct/1994|26/Oct/1994|27/Oct/1994|28/Oct/1994|29/Oct/1994)', line):
     b1 += 1
    if re.search('(30/Oct/1994|31/Oct/1994|01/Nov/|02/Nov/|03/Nov/|04/Nov/|05/Nov/)', line):
     b2 += 1
    if re.search('(06/Nov/|07/Nov/|08/Nov/|09/Nov/|10/Nov/|11/Nov/|12/Nov/)', line):
     b3 += 1
    if re.search('(13/Nov/|14/Nov/|15/Nov/|16/Nov/|17/Nov/|18/Nov/|19/Nov/)', line):
     b4 += 1
    if re.search('(20/Nov/|21/Nov/|22/Nov/|23/Nov/|24/Nov/|25/Nov/|26/Nov/)', line):
     b5 += 1
    if re.search('(27/Nov/|28/Nov/|29/Nov/|30/Nov/|01/Dec/|02/Dec/|03/Dec/)', line):
     b6 += 1
    if re.search('(04/Dec/|05/Dec/|06/Dec|/07/Dec/|08/Dec/|09/Dec/|10/Dec/)', line):
     b7 += 1
    if re.search('(11/Dec/|12/Dec/|13/Dec|/14/Dec/|15/Dec/|16/Dec/|17/Dec/)', line):
     b8 += 1
    if re.search('(18/Dec/|19/Dec/|20/Dec|/21/Dec/|22/Dec/|23/Dec/|24/Dec/)', line):
     b9 += 1
    if re.search('(25/Dec/|26/Dec/|27/Dec|/28/Dec/|29/Dec/|30/Dec/|31/Dec/)', line):
     b10 += 1
    if re.search('(01/Jan/|02/Jan/|03/Jan/|04/Jan/|05/Jan/|06/Jan/|07/Jan/)', line):
     b11 += 1
    if re.search('(08/Jan/|09/Jan/|10/Jan/|11/Jan/|12/Jan/|13/Jan/|14/Jan/)', line):
     b12 += 1
    if re.search('(15/Jan/|16/Jan/|17/Jan/|18/Jan/|19/Jan/|20/Jan/|21/Jan/)', line):
     b13 += 1
    if re.search('(22/Jan/|23/Jan/|24/Jan/|25/Jan/|26/Jan/|27/Jan/|28/Jan/)', line):
     b14 += 1
    if re.search('(29/Jan/|30/Jan/|31/Jan/|01/Feb/|02/Feb/|03/Feb/|04/Feb/)', line):
     b15 += 1
    if re.search('(05/Feb/|06/Feb/|07/Feb/|08/Feb/|09/Feb/|10/Feb/|11/Feb/)', line):
     b16 += 1
    if re.search('(12/Feb/|13/Feb/|14/Feb/|15/Feb/|16/Feb/|17/Feb/|18/Feb/)', line):
     b17 += 1
    if re.search('(19/Feb/|20/Feb/|21/Feb/|22/Feb/|23/Feb/|24/Feb/|25/Feb/)', line):
     b18 += 1
    if re.search('(26/Feb/|27/Feb/|28/Feb/|01/Mar/|02/Mar/|03/Mar/|04/Mar/)', line):
     b19 += 1
    if re.search('(05/Mar/|06/Mar/|07/Mar/|08/Mar/|09/Mar/|10/Mar/|11/Mar/)', line):
     b20 += 1
    if re.search('(12/Mar/|13/Mar/|14/Mar/|15/Mar/|16/Mar/|17/Mar/|18/Mar/)', line):
     b21 += 1
    if re.search('(26/Feb/|27/Feb/|28/Feb/|01/Mar/|02/Mar/|03/Mar/|04/Mar/)', line):
     b19 += 1
    if re.search('(05/Mar/|06/Mar/|07/Mar/|08/Mar/|09/Mar/|10/Mar/|11/Mar/)', line):
     b20 += 1
    if re.search('(12/Mar/|13/Mar/|14/Mar/|15/Mar/|16/Mar/|17/Mar/|18/Mar/)', line):
     b21 += 1
    if re.search('(19/Mar/|20/Mar/|21/Mar/|22/Mar/|23/Mar/|24/Mar/|25/Mar/)', line):
     b22 += 1
    if re.search('(26/Mar/|27/Mar/|28/Mar/|29/Mar/|30/Mar/|31/Mar/|01/Apr/)', line):
     b23 += 1
    if re.search('(02/Apr/|03/Apr/|04/Apr/|05/Apr/|06/Apr/|07/Apr/|08/Apr/)', line):
     b24 += 1
    if re.search('(09/Apr/|10/Apr/|11/Apr/|12/Apr/|13/Apr/|14/Apr/|15/Apr/)', line):
     b25 += 1
    if re.search('(16/Apr/|17/Apr/|18/Apr/|19/Apr/|20/Apr/|21/Apr/|22/Apr/)', line):
     b26 += 1
    if re.search('(23/Apr/|24/Apr/|25/Apr/|26/Apr/|27/Apr/|28/Apr/|29/Apr/)', line):
     b27 += 1
    if re.search('(30/Apr/|01/May/|02/May/|03/May/|04/May/|05/May/|06/May/)', line):
     b28 += 1
    if re.search('(07/May/|08/May/|09/May/|10/May/|11/May/|12/May/|13/May/)', line):
     b29 += 1
    if re.search('(14/May/|15/May/|16/May/|17/May/|18/May/|19/May/|20/May/)', line):
     b30 += 1
    if re.search('(21/May/|22/May/|23/May/|24/May/|25/May/|26/May/|27/May/)', line):
     b31 += 1
    if re.search('(28/May/|29/May/|30/May/|31/May/|01/Jun/|02/Jun/|03/Jun/)', line):
     b32 += 1
    if re.search('(04/Jun/|05/Jun/|06/Jun/|07/Jun/|08/Jun/|09/Jun/|10/Jun/)', line):
     b33 += 1
    if re.search('(11/Jun/|12/Jun/|13/Jun/|14/Jun/|15/Jun/|16/Jun/|17/Jun/)', line):
     b34 += 1
    if re.search('(18/Jun/|19/Jun/|20/Jun/|21/Jun/|22/Jun/|23/Jun/|24/Jun/)', line):
     b35 += 1
    if re.search('(25/Jun/|26/Jun/|27/Jun/|28/Jun/|29/Jun/|30/Jun/|01/Jul/)', line):
     b36 += 1
    if re.search('(02/Jul/|03/Jul/|04/Jul/|05/Jul/|06/Jul/|07/Jul/|08/Jul/)', line):
     b37 += 1
    if re.search('(09/Jul/|10/Jul/|11/Jul/|12/Jul/|13/Jul/|14/Jul/|15/Jul/)', line):
     b38 += 1
    if re.search('(16/Jul/|17/Jul/|18/Jul/|19/Jul/|20/Jul/|21/Jul/|22/Jul/)', line):
     b39 += 1
    if re.search('(23/Jul/|24/Jul/|25/Jul/|26/Jul/|27/Jul/|28/Jul/|29/Jul/)', line):
     b40 += 1
    if re.search('(30/Jul/|31/Jul/|01/Aug/|02/Aug/|03/Aug/|04/Aug/|05/Aug/)', line):
     b41 += 1
    if re.search('(06/Aug/|07/Aug/|08/Aug/|09/Aug/|10/Aug/11/Aug/|12/Aug/)', line):
     b42 += 1
    if re.search('(13/Aug/|14/Aug/|15/Aug/|16/Aug/|17/Aug/18/Aug/|19/Aug/)', line):
     b43 += 1
    if re.search('(20/Aug/|21/Aug/|22/Aug/|23/Aug/|24/Aug/|25/Aug/|26/Aug/)', line):
     b44 += 1
    if re.search('(27/Aug/|28/Aug/|29/Aug/|30/Aug/|31/Aug/|01/Sep/|02/Sep/)', line):
     b45 += 1
    if re.search('(03/Sep/|04/Sep/|05/Sep/|06/Sep/|07/Sep/|08/Sep/|09/Sep/)', line):
     b46 += 1
    if re.search('(10/Sep/|11/Sep/|12/Sep/|13/Sep/|14/Sep/|15/Sep/|16/Sep/)', line):
     b47 += 1
    if re.search('(17/Sep/|18/Sep/|19/Sep/|20/Sep/|21/Sep/|22/Sep/|23/Sep/)', line):
     b48 += 1
    if re.search('(24/Sep/|25/Sep/|26/Sep/|27/Sep/|28/Sep/|29/Sep/|30/Sep/)', line):
     b49 += 1
    if re.search('(01/Oct/1995|02/Oct/1995|03/Oct/1995|04/Oct/1995|05/Oct/1995|06/Oct/1995|07/Oct/1995)', line):
     b50 += 1
    if re.search('(08/Oct/1995|09/Oct/1995|10/Oct/1995|11/Oct/1995)', line):
     b51 += 1
print("++++++++++++++++++++++++++++++++++++++")
print("+   Total For Each Week to Week      +")
print("++++++++++++++++++++++++++++++++++++++")
print("total for Oct 24 - Oct 29",  b1)
print("total for Oct 30 - Nov 05",  b2)
print("total for Nov 06 - Nov 12",  b3)
print("total for Nov 13 - Nov 19",  b4)
print("total for Nov 20 - Nov 26",  b5)
print("total for Nov 27 - Dec 03",  b6)
print("total for Dec 04 - Dec 10",  b7)
print("total for Dec 11 - Dec 17",  b8)
print("total for Dec 18 - Dec 24",  b9)
print("total for Dec 25 - Dec 31", b10)
print("total for Jan 01 - Jan 07", b11)
print("total for Jan 08 - Jan 14", b12)
print("total for Jan 15 - Jan 21", b13)
print("total for Jan 22 - Jan 28", b14)
print("total for Jan 29 - Feb 04", b15)
print("total for Feb 05 - Feb 11", b16)
print("total for Feb 12 - Feb 18", b17)
print("total for Feb 19 - Feb 25", b18)
print("total for Feb 26 - Mar 04", b19)
print("total for Mar 05 - Mar 11", b20)
print("total for Mar 12 - Mar 18", b21)
print("total for Mar 19 - Mar 25", b22)
print("total for Mar 26 - Apr 01", b23)
print("total for Apr 02 - Apr 08", b24)
print("total for Apr 09 - Apr 15", b25)
print("total for Apr 16 - Apr 22", b26)
print("total for Apr 23 - Apr 29", b27)
print("total for Apr 30 - May 06", b28)
print("total for May 07 - May 13", b29)
print("total for May 14 - May 20", b30)
print("total for May 21 - May 27", b31)
print("total for May 28 - Jun 03", b32)
print("total for Jun 04 - Jun 10", b33)
print("total for Jun 11 - Jun 18", b34)
print("total for Jun 19 - Jun 25", b35)
print("total for Jun 26 - Jul 02", b36)
print("total for Jul 02 - Jul 08", b37)
print("total for Jul 09 - Jul 15", b38)
print("total for Jul 16 - Jul 22", b39)
print("total for Jul 23 - Jul 29", b40)
print("total for Jul 30 - Aug 05", b41)
print("total for Aug 06 - Aug 12", b42)
print("total for Aug 13 - Aug 19", b43)
print("total for Aug 20 - Aug 26", b44)
print("total for Aug 27 - Sep 02", b45)
print("total for Sep 03 - Sep 09", b46)
print("total for Sep 10 - Sep 16", b47)
print("total for Sep 17 - Sep 23", b48)
print("total for Sep 24 - Sep 30", b49)
print("total for Oct 01 - Oct 07", b50)
print("total for Oct 08 - Oct 11", b51)
print("++++++++++++++++++++++++++++++++++++++++++")


a = open("oct1994.txt","w"); b = open("nov.txt","w"); c=open("december.txt", "a+");d =open("january.txt", "a+"); 
e=open("february.txt", "a+"); f=open("march.txt", "a+"); 
g=open("april.txt", "a+"); h=open("may.txt", "a+"); i=open("june.txt", "a+");
j=open("july.txt", "a+"); k=open("august.txt", "a+"); l=open("september.txt", "a+");
m=open("oct1995n.txt", "a+");    

oct94 = 0; nov = 0; dec = 0; jan = 0; feb =0; mar =0;
apr = 0; may = 0; jun = 0; jul = 0; aug = 0; sep = 0; oct95 = 0;

with open("./http_access_log.txt") as s:				
		for line in s:
			if re.search('(/Oct/1994)', line):
				oct94+=1
				a.write(line)
			if re.search( '(/Nov/)', line):
				nov+=1
				b.write(line)
			if re.search('(/Dec/)', line):
				dec+=1
				c.write(line)
			if re.search('(/Jan/)',line):					
				jan+=1
				d.write(line)
			if re.search('(/Feb/)',line):
				feb+=1
				e.write(line)
			if re.search('(/Mar/)',line):
				mar+=1
				f.write(line)
			if re.search('(11/Apr/)', line):
				apr+=1
				g.write(line)
			if re.search('(/May/)', line):
				may+=1
				h.write(line)
			if re.search('(/Jun/)', line):
				jun+=1
				i.write(line)
			if re.search('(/Jul/)', line):
				jul+=1
				j.write(line)
			if re.search('(/Aug/)', line):
				aug+=1
				k.write(line)
			if re.search('(/Sep/)', line):
				sep+=1
				l.write(line)
			if re.search('(/Oct/1995)', line):				
				oct95+=1	
				m.write(line)					
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")			
print("Total requests made in last 6 months is:", apr + may + jun + jul + aug + sep + oct95)
requests = len(open("./http_access_log.txt").readlines(  ))
print('Total requests were made in the time period is:' , requests)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Each month's total:")
print("_________________________________________________________")
print("October 1994 total", oct94 )
print("November total", nov)
print("December total", dec)
print("January total", jan)
print("Feburary total", feb)
print("March total", mar)
print("April total", apr)
print("May total", may)
print("June total", jun)
print("July total", jul)
print("August total", aug)
print("September total", sep)
print("October 1995 total", oct95)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
def redirectCodes(requests):							
	redirectCounter = 0.0
	print()
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("+               Status Code Matching                +")
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print()
	with open("./http_access_log.txt") as logs:				
		for line in logs:
			if re.search('\s*(30\d)\s\S+', line):
				redirectCounter += 1
	print("There were ", redirectCounter, "total redirects (30x) in this log file.")
	print("Percentage of all requests that were redirects (30x): {0:.2%}".format(redirectCounter/requests))
def clientErrors(requests):							
	errorCounter = 0.0
	with open("./http_access_log.txt") as logs:				
		for line in logs:
			if re.search('\s*(4\d\d)\s\S+', line):
				errorCounter += 1
	print("There were ", errorCounter, "total client error (4xx) codes in this log file.")
	print("Percentage of client error (4xx) requests: {0:.2%}".format(errorCounter/requests))	
def main(): 
	redirectCodes(requests)
	clientErrors(requests)
main()

def fileCount():
    	print()
print()
filelog = []
leastcommon = []
with open("./http_access_log.txt") as f:
	for line in f:
			try:
				filelog.append(line[line.index("GET")+4:line.index("HTTP")])		
			except:
				pass
	counter = Counter(filelog)
	for count in counter.most_common(1):														
		print("Most commonly requested file: {} with {} requests.".format(str(count[0]), str(count[1])))
	for count in counter.most_common():					
		if str(count[1]) == '1':
			leastcommon.append(count[0])
	if leastcommon:										
		i = input("Looks like there were {} file(s) that were requested only once, show all? (y/n)".format(len(leastcommon)))
		if i == 'y' or i == 'Y':
			for file in leastcommon:
				print(file)
