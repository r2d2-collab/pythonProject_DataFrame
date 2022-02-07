import pyodbc
import pandas as pd

df = pd.read_csv('../../../../Sample Exercise/DF_Raw_Data.csv')
print(df.info())

server = 'WORKER-ANT'
database = 'PortfolioProject'
username = ''
password = ''
cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

for index, row in df.iterrows():
    cursor.execute("INSERT INTO dbo.Pump_Raw_Data (TimeFrame,VolumetricFlowMeter1,VolumetricFlowMeter2,PumpSpeed,"
                   "PumpTorque,AmbientTemperature,HorsePower,PumpEfficiency,PumpFailure) values(?,?,?,?,?,?,?,?,?)",
                   row.TIMEFRAME,
                   row.VolumetricFlowMeter1, row.VolumetricFlowMeter2,row.PumpSpeed,
                   row.PumpTorque,row.AmbientTemperature,row.HorsePower,row.PumpEfficiency,row.PumpFailure)
cnxn.commit()
cursor.close()
