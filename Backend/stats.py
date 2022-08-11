import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

for i in range(5, 9):
    if i == 6:
        nn = 31
    else:
        nn = 32
    for j in range(1, nn):
        dd = '0' + str(j) if len(str(j)) == 1 else str(j)
        day = '20220' + str(i) + dd        
        with open (f'log_dummy/{day}', encoding='UTF8') as f:
                            records = [line.rstrip().split(' ') for line in f]
        columns = ['date', 'time', 'building', 'floor', 'token', 'trash_type', 'rfid', 'amount']
        df = pd.DataFrame(records, columns=columns)
        df["hour"] = df["time"].str[:2]
        right_data = df.drop_duplicates(subset=['token'])
        left_data = df.groupby(['token', 'hour']).date.count().unstack(fill_value=0)        
        left_data.reset_index(inplace=True)
        left_data.index.name = 'pk'
        labels = ['token', 'hour_00','hour_01','hour_02','hour_03','hour_04','hour_05','hour_06','hour_07','hour_08','hour_09','hour_10','hour_11','hour_12','hour_13','hour_14','hour_15','hour_16','hour_17','hour_18','hour_19','hour_20','hour_21','hour_22','hour_23']
        left_data.columns = labels
        left_data['total'] = left_data.sum(numeric_only=True, axis=1)
        new_df = left_data.merge(right_data, on='token')
        new_df.drop(columns=['time', 'rfid', 'amount', 'hour'], inplace=True)
        new_df.token.astype('str')
        new_df.date.astype('str')

        dic = new_df.to_dict()
        js = new_df.to_json(orient='records', force_ascii=False)
        # with open(f'stats_result/{day}.json', 'w', encoding='utf-8') as json_file:
        #     json.dump(js, json_file, ensure_ascii=False, default=str)