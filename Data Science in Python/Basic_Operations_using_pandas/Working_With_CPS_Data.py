db = pd.read_csv('file_location\\algexit2009.csv')
db
db.values
db
db.head(15)
db.tail(5)
db.sort(columns=["total_pass"])
db.sort(columns=["total_pass"], inplace=True)
db.sort(columns=["total_pass"], inplace=True, ascending=False)
db.sort(columns=["total_highpass"], inplace=True, ascending=False)
db.iat[0,2]
db.iat[0,2] / float(db.iat[0,3])
passpercent = []
for i in range(len(db)):
	passpercent.append(db.iat[i,2] / float(db.iat[i,3]))
db['pass percent'] = passpercent
highpasspercent = []
for i in range(len(db)):
	highpasspercent.append(db.iat[i,1] / float(db.iat[i,3]))	
db['high pass percent'] = highpasspercent
db.sort(columns=['pass percent'], inplace=True, ascending=False)
totalpass = []
for i in range(len(db)):
	totalpass.append(db.iat[i,1] + db.iat[i,2])
db.['total pass'] = totalpass
db.sort(columns=['total pass'], inplace=True, ascending=False)	
totalpasspercent = []
for i in range(len(db)):
	totalpasspercent.append(db.iat[i,6] / float(db.iat[i,3]))
db['total pass percent'] = totalpasspercent
db.sort(columns=['total pass percent'], inplace=True, ascending=False)