wllist=[]
import csv
with open('C:\\Users\\4shub\\Desktop\\summertrainning\\worldbank.csv', encoding='latin-1') as csvfile:
    files = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in files:
        wllist.append(row)
dict={}
nt=wllist

for i in range(4,len(nt)):
    if(nt[i][54] == ''):
        gdpv=0
    else:
        gdpv=float(nt[i][54])
    coname=nt[i][0]
    dict[coname]=gdpv
sorted(dict.items(),key = lambda x: x[1], reverse = True)
gdp=dict.values()
import matplotlib.pyplot as plt
plt.hist(gdp)
plt.show()
cname=dict.keys()
gdpv=dict.values()
plt.plot(gdpv)
plt.show()