import pandas, math
table = pandas.read_csv('dataset2.csv')
table = table.drop_duplicates(subset=['terreno','casa','recamaras','baños','precio','estacionamiento'])
table = table.reset_index()
for index, row in table.iterrows():
	if row['terreno'] == "" or pandas.isna(row['terreno']):
		row['terreno'] = row['casa']
	if type(row['casa']) == str:
		row['casa'] = row['casa'].split(' ')[0]
	if type(row['terreno']) == str:
		row['terreno'] = row['terreno'].split(' ')[0]
	if type(row['recamaras']) == str:
		row['recamaras'] = row['recamaras'].split(' ')[0]
	if type(row['baños']) == str:
		row['baños'] = row['baños'].split(' ')[0]
	if type(row['estacionamiento']) == str:
		row['estacionamiento'] = row['estacionamiento'].split(' ')[0]
	
	if pandas.isna(row['baños']):
		row['baños'] = table.groupby('recamaras')['baños'].agg(pandas.Series.mode).to_dict()[row['recamaras']]
	if(float(row['terreno']) < float(row['casa'])):
		x = row['terreno']
		row['terreno'] = row['casa']
		row['casa'] = x
	table.iloc[index] = row
table.to_csv('cleaned2.csv',index=False)