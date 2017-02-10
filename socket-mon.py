import psutil
from operator import itemgetter

#obtain raw process connection data
result = psutil.net_connections()

#select existing connection data in a list
total = []
for s in result:
    if (all(s)):
        each = {
            "pid": s.pid,
            "laddr": str((s.laddr)[0])+"@"+str((s.laddr)[1]),
            "raddr": str((s.raddr)[0])+"@"+str((s.raddr)[1]),
            "status": s.status,
        }
        total.append(each)

#remove duplicates and transfer result to a new list
seen = set()
newList = []
for c in total:
    temp = tuple(c.items())
    if temp not in seen:
        seen.add(temp)
        newList.append(c)


#count the number of connections per process
seen = set()
count = {}
for c in newList:
    temp = c['pid']
    if temp not in seen:
        seen.add(temp)
        count[temp] = 1
    else:
        count[temp]+=1

#sort result list by number of connections per process in decreasing order
countList = sorted(count.items(), key=itemgetter(1), reverse=True)
print "\"pid\",\"laddr\",\"raddr\",\"status\""
for i in countList:
    for r in newList:
        if (i[0] == r['pid']):
            print "\"%s\"," % r['pid'],
            print "\"%s\"," % r['laddr'],
            print "\"%s\"," % r['raddr'],
            print "\"%s\"" % r['status'],
            print
            newList.remove(r)
