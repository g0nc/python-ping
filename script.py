import os

ons = []
off = []

site = raw_input("insert domain: ")
site = site.upper()
site.replace("http://", "")
site.replace("https://", "")




def check_ping(sub, site):
	
    hostname = sub +"."+site
    response = os.system("ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        #if 0, is online
        ons.append(hostname)
    else:
        #if <> 0 / 1is ff
        off.append(hostname)

file = open("subs.txt", "r")
lines = file.readlines()

for sub in lines:
	sub = sub.replace("\n", "")
	check_ping(sub,site)

#show results
for online in ons:
	print("subdomain online: "+str(online))
for offline in off:
	print("subdomain offline: "+str(offline))


