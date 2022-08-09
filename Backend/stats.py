import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime



today = ''.join(str(datetime.date(datetime.today())).split('-'))
with open (f'logs/20220807', encoding='UTF8') as f:
    records = [line.rstrip().split(' ') for line in f]
columns = ['date', 'time', 'campus', 'building', 'floor', 'token', 'trash_type', 'rfid', 'amount']
df = pd.DataFrame(records, columns=columns)
df["hour"] = df["time"].str[:2]


stats_campus = df.groupby(["campus", "hour"]).date.count() 
stats_building = df.groupby(["campus", "building", "hour"]).date.count() 
stats_floor = df.groupby(["campus", "building", "floor","hour"]).date.count() 
stats_trashbin = df.groupby(["token", "hour"]).date.count() 
stats_trashbin_type = df.groupby(["campus", "trash_type"]).date.count()
print(stats_campus)
print(stats_building)
print(stats_floor)
print(stats_trashbin)
print(stats_trashbin_type)

