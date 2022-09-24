import pandas as pd, json



# Helper functions
getMethods = lambda obj: [method for method in dir(obj) if not method.startswith('_')]
searchMethods = lambda obj, search_str: [method for method in getMethods(obj) if search_str in method]
toDict = lambda series: series.to_dict(orient='records')
toDF = lambda data: pd.DataFrame(data)
toJsonDF = lambda df: pd.json_normalize(toDict(df))
jprint = lambda obj, indent=2: print(json.dumps(obj, indent=indent))
Help = lambda obj: print(help(obj))




# Testing 

print()
print('getMetohds: ')
print(getMethods(pd))


print()
print('searchMethods: ')
print(searchMethods(pd,'to_'))


print()
print('Sample data: ')
sdata = pd.read_csv('http://bit.ly/kaggletrain')
print(sdata.head())


print()
sdata_top_5_row = toDict(sdata.loc[:5, 'PassengerId':'Age'])
print('toDict: ')
print(sdata_top_5_row)


print()
print('jprint: ')
jprint(sdata_top_5_row)


print()
print('toJsonDF: ')
print(toJsonDF(sdata))

print()
print('Help:')
Help(sdata.isna)
