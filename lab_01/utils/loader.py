import pandas as pd  
import os
from data_class import AIR, EARTH, WATER

cur_path = os.path.dirname(os.getcwd())
data_path = os.path.join(cur_path, 'Dataset')

def load(file_name):
    file_name = os.path.join(data_path, file_name)
    data = pd.read_csv(file_name)
    print(f"Loading file: {file_name}")
    data_set = []
    if 'AIR' in file_name:
        for i in range(data.shape[0]):
            row = data.iloc[i]
            air = AIR(row['Time'], row['Station'], row['Temperature'], row['Moisture'], row['Light'], row['Total_Rainfall'], row['Rainfall'], row['Wind_Direction'], row['PM2.5'], row['PM10'], row['CO'], row['NOx'], row['SO2'])
            data_set.append(air)
    elif 'EARTH' in file_name:
        for i in range(data.shape[0]):
            row = data.iloc[i]
            earth = EARTH(row['Time'], row['Station'], row['Moisture'], row['Temperature'], row['Salinity'], row['pH'], row['Water_Root'], row['Water_Leaf'], row['Water_Level'], row['Voltage'])
            data_set.append(earth)
    elif 'WATER' in file_name:
        for i in range(data.shape[0]):
            row = data.iloc[i]
            water = WATER(row['Time'], row['Station'], row['pH'], row['DO'], row['Temperature'], row['Salinity'])
            data_set.append(water)
    else:
        print('Invalid file name')
        return None
    return data_set

def multi_load(topic_and_file):
    data_set = {}
    for key, value in topic_and_file.items():
        data_set[key] = load(value)
    return data_set