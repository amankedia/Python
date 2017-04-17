import numpy as np
import matplotlib.pyplot as pp
import seaborn
import urllib
urllib.urlretrieve('ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt','stations.txt')
open('stations.txt','r').readlines()[:10]
stations = {}
for line in open('stations.txt','r'):
        if 'GSN' in line:
            fields = line.split()
            stations[fields[0]] = ' '.join(fields[4:])
len(stations)
def findstation(s):
        found = {code: name for code,name in stations.items() if s in name}
        print(found)
print(findstation('LIHUE'))
findstation('SAN DIEGO')
findstation('IRKUTSK')
datastations = ['USW00022536','USW00023188','USW00014922','RSM00030710']
open('USW00022536.dly','r').readlines()[:10]
open('readme.txt','r').readlines()[98:121]
def parsefile(filename):
        return np.genfromtxt(filename,
                             delimiter = dly_delimiter,
                             usecols = dly_usecols,
                             dtype = dly_dtype,
                             names = dly_names)
dly_delimiter = [11,4,2,4] + [5,1,1,1] * 31
dly_usecols = [1,2,3] + [4*i for i in range(1,32)]
dly_dtype = [np.int32,np.int32,(np.str_,4)] + [np.int32] * 31
dly_names = ['year','month','obs'] + [str(day) for day in range(1,31+1)]
lihue = parsefile('USW00022536.dly')
def unroll(record):
	startdate = np.datetime64('{}-{:02}'.format(record['year'],record['month']))
	dates = np.arange(startdate,startdate + np.timedelta64(1,'M'),np.timedelta64(1,'D'))
	rows = [(date,record[str(i+1)]/10) for i,date in enumerate(dates)]
	return np.array(rows,dtype=[('date','M8[D]'),('value','d')])
