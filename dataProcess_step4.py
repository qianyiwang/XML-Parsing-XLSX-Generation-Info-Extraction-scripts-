# data process step 4 is used to extract features from each subject form

import pandas as pd
import math
from openpyxl import load_workbook

# define functions
def calculateAbsTime(time):
    arr = time.split(':')
    absTime =  (int(arr[0])-10)*3600+int(arr[1])*60+int(arr[2])
    return absTime

def findSteps(startTime, endTime, timeArray):
    steps = 1
    for t in timeArray:
        t = calculateAbsTime(t)
        if t > startTime and t < endTime:
            steps = steps + 1

    return steps

book = pd.ExcelFile('C:/ClinicServer/Excel/Subject8.xlsx')

# 'Data' sheet processing
df_data = book.parse('Data')
road_id_init = '00'
road_id_array = []
for i in range(0, len(df_data['RoadID'])):
    road_id = df_data['RoadID'][i]
    if road_id != road_id_init and not math.isnan(road_id):
        road_id_array.append(i)
        road_id_init = road_id
end2end_mcs_startTime = df_data['SimulatorTime'][road_id_array[1]]
end2end_mcs_startTime = calculateAbsTime(end2end_mcs_startTime)
end2end_climate_startTime = df_data['SimulatorTime'][road_id_array[3]]
end2end_climate_startTime = calculateAbsTime(end2end_climate_startTime)
end2end_bt_startTime = df_data['SimulatorTime'][road_id_array[4]]
end2end_bt_startTime = calculateAbsTime(end2end_bt_startTime)
# end2end_park_startTime = df_data['SimulatorTime'][road_id_array[9]]

#  'Event' sheet processing
df_event = book.parse('Event')

end2end_map_startTime = 'Nan'
for i in range(0, len(df_event['Name'])):
    if df_event['Name'][i] == 'Start Google Map':
        end2end_map_endTime = df_event['SimulatorTime'][i]
        end2end_map_endTime = calculateAbsTime(end2end_map_endTime)
    if df_event['Name'][i] == 'EnterAddressIssued':
        end2end_map_startTime = df_event['SimulatorTime'][i]
        end2end_map_startTime = calculateAbsTime(end2end_map_startTime)
    if df_event['Name'][i] == 'driver_tempUp':
        end2end_climate_endTime = df_event['SimulatorTime'][i]
        end2end_climate_endTime = calculateAbsTime(end2end_climate_endTime)
    if df_event['Name'][i] == 'audio_seekUp':
        end2end_bt_endTime = df_event['SimulatorTime'][i]
        end2end_bt_endTime = calculateAbsTime(end2end_bt_endTime)
    if df_event['Name'][i] == 'MCS_enter':
        end2end_mcs_endTime = df_event['SimulatorTime'][i]
        end2end_mcs_endTime = calculateAbsTime(end2end_mcs_endTime)
    if df_event['Name'][i] == 'Parking Notification':
        end2end_park_startTime = df_event['SimulatorTime'][i]
        end2end_park_startTime = calculateAbsTime(end2end_park_startTime)
    if df_event['Name'][i] == 'PARKING':
        end2end_park_endTime = df_event['SimulatorTime'][i]
        end2end_park_endTime = calculateAbsTime(end2end_park_endTime)
if end2end_map_startTime == 'Nan':
    end2end_map_startTime = end2end_map_endTime

print findSteps(end2end_bt_startTime, end2end_bt_endTime, df_event['SimulatorTime'])

# write into 'Data' sheet
book = load_workbook('C:/ClinicServer/Excel/Subject8.xlsx')
writer = pd.ExcelWriter('C:/ClinicServer/Excel/Subject8.xlsx', engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
update = pd.DataFrame(
{'Task Name':['Open map', 'MCS', 'Climate control', 'BT audio control', 'Parking'],
'Task Start Time':[end2end_map_startTime, end2end_mcs_startTime, end2end_climate_startTime, end2end_bt_startTime, end2end_park_startTime],
'Task End Time':[end2end_map_endTime, end2end_mcs_endTime, end2end_climate_endTime, end2end_bt_endTime, end2end_park_endTime],
'Task Duration': [end2end_map_endTime-end2end_map_startTime, end2end_mcs_endTime-end2end_mcs_startTime, end2end_climate_endTime-end2end_climate_startTime, end2end_bt_endTime-end2end_bt_startTime, end2end_park_endTime-end2end_park_startTime]}
)
update.to_excel(writer, 'Task', columns=['Task Name','Task Start Time', 'Task End Time', 'Task Duration'], index=False)
writer.save()
