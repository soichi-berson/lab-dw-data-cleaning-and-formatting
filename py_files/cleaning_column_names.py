#cleaning column Names 

import numpy as np
import pandas as pd 

def to_lower_case(df: df.DataFrane) -> df.DataFrame:

	'''
	This changes columns in lower case 

	Input: 
	df:df.DataFrame

	Ourput: 
	Another df.DataFrame


	'''

	df2 = df.copy()

	cols = []
	for colname in df2.columns:
    	cols.append(colname.lower())

	df2.columns = cols

	return df2


def column_name(df: df.DataFrane) -> df.DataFrame:


	'''
	Regarding column name, this replaces 'customer' of a column name with 'id', and '(space)' with '_'.   

	Input: 
	df:df.DataFrame

	Ourput: 
	Another df.DataFrame


	'''

	df2 = df.copy()
	#replace 'customer' with 'id'
	if 'customer' in df2.columns:

		df2 = df2.rename(columns={'customer':'id'})

	#replace '(space)' with '_'
	df2.columns = df2.columns.str.replace(' ', '_')



def cleaning_column_names(df: df.DataFrane) -> df.DataFrame:


	'''
	This cleans column names by using two functions above.

	Input: 
	df:df.DataFrame

	Ourput: 
	Another df.DataFrame


	'''

	df2 = df.copy()

	df2 = to_lower_case(df2)
	df2 = column_name(df2)

	return df2
	



