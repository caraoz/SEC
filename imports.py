import pandas as pd
import glob
from sqlalchemy import create_engine

engine = create_engine('sqlite:///edgar.db',echo=False)
files = glob.glob('*.tsv')
for file in files:
	#print(file)
	yr = file.split('-')[0]
	qtr = file.split('-')[1].replace('.tsv','')
	df = pd.read_csv(file,sep="|",header = None,names=['CIK','FirmName','FilingType','FilingDate','FileTxt','FileHTML'])
	df['yr'] = yr
	df['qtr'] = qtr
	print(df.shape)
	df.to_sql('master',con=engine,if_exists='append')

