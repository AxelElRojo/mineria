import pandas, requests
table = pandas.read_csv('inside.csv')
table = table.reset_index()
left = pandas.read_csv('calzada.csv')
for index, row in table.iterrows():
	for index2, row2 in left.iterrows():
		if row['direccion'] == row2['direccion']:
			row['calzada'] = 1
			break
	table.iloc[index] = row
table.to_csv('final.csv', index=False)