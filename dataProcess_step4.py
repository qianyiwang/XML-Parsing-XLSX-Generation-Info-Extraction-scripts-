# data process step 4 is used to calculate the global statistic feature and plot

import pandas as pd
import math
import os
import Variables

FILE = 'C:\ClinicServer\Excel'
for subdir, dirs, files in os.walk(FILE):
    for f in files:
        if 'xlsx' not in f:
            continue
        print 'processing on %s' % f

        fileDir = 'C:\ClinicServer\Excel\%s'%f
        book = pd.ExcelFile(fileDir)
        df_end2end = book.parse('Task')
        df_baseline = book.parse('Baseline Task')

        for i in range(0,5):
            if i == 0:
                Variables.end2end_map_duration.append(df_end2end['Task Duration'][i])
                Variables.baseline_map_duration.append(df_baseline['Task Duration'][i])
                Variables.end2end_map_step.append(df_end2end['Task Steps'][i])
                Variables.baseline_map_step.append(df_baseline['Task Steps'][i])
                Variables.end2end_map_velocity.append(df_end2end['Average Velocity'][i])
                Variables.baseline_map_velocity.append(df_baseline['Average Velocity'][i])
                Variables.end2end_map_hr.append(df_end2end['Average HR'][i])
                Variables.baseline_map_hr.append(df_baseline['Average HR'][i])
                Variables.end2end_map_acc.append(df_end2end['Average Acceleration'][i])
                Variables.baseline_map_acc.append(df_baseline['Average Acceleration'][i])
                Variables.end2end_map_brake.append(df_end2end['Average BrakeStatus'][i])
                Variables.baseline_map_brake.append(df_baseline['Average BrakeStatus'][i])
                Variables.end2end_map_laneoff.append(df_end2end['Average LaneOffset'][i])
                Variables.baseline_map_laneoff.append(df_baseline['Average LaneOffset'][i])
                Variables.end2end_map_swa.append(df_end2end['Average SteeringWheelAngle'][i])
                Variables.baseline_map_swa.append(df_baseline['Average SteeringWheelAngle'][i])
                Variables.end2end_map_adas.append(df_end2end['ADAS#'][i])
                Variables.baseline_map_adas.append(df_baseline['ADAS#'][i])
            elif i == 1:
                Variables.end2end_mcs_duration.append(df_end2end['Task Duration'][i])
                Variables.baseline_mcs_duration.append(df_baseline['Task Duration'][i])
                Variables.end2end_mcs_step.append(df_end2end['Task Steps'][i])
                Variables.baseline_mcs_step.append(df_baseline['Task Steps'][i])
                Variables.end2end_mcs_velocity.append(df_end2end['Average Velocity'][i])
                Variables.baseline_mcs_velocity.append(df_baseline['Average Velocity'][i])
                Variables.end2end_mcs_hr.append(df_end2end['Average HR'][i])
                Variables.baseline_mcs_hr.append(df_baseline['Average HR'][i])
                Variables.end2end_mcs_acc.append(df_end2end['Average Acceleration'][i])
                Variables.baseline_mcs_acc.append(df_baseline['Average Acceleration'][i])
                Variables.end2end_mcs_brake.append(df_end2end['Average BrakeStatus'][i])
                Variables.baseline_mcs_brake.append(df_baseline['Average BrakeStatus'][i])
                Variables.end2end_mcs_laneoff.append(df_end2end['Average LaneOffset'][i])
                Variables.baseline_mcs_laneoff.append(df_baseline['Average LaneOffset'][i])
                Variables.end2end_mcs_swa.append(df_end2end['Average SteeringWheelAngle'][i])
                Variables.baseline_mcs_swa.append(df_baseline['Average SteeringWheelAngle'][i])
                Variables.end2end_mcs_adas.append(df_end2end['ADAS#'][i])
                Variables.baseline_mcs_adas.append(df_baseline['ADAS#'][i])
            elif i == 2:
                Variables.end2end_climate_duration.append(df_end2end['Task Duration'][i])
                Variables.baseline_climate_duration.append(df_baseline['Task Duration'][i])
                Variables.end2end_climate_step.append(df_end2end['Task Steps'][i])
                Variables.baseline_climate_step.append(df_baseline['Task Steps'][i])
                Variables.end2end_climate_velocity.append(df_end2end['Average Velocity'][i])
                Variables.baseline_climate_velocity.append(df_baseline['Average Velocity'][i])
                Variables.end2end_climate_hr.append(df_end2end['Average HR'][i])
                Variables.baseline_climate_hr.append(df_baseline['Average HR'][i])
                Variables.end2end_climate_acc.append(df_end2end['Average Acceleration'][i])
                Variables.baseline_climate_acc.append(df_baseline['Average Acceleration'][i])
                Variables.end2end_climate_brake.append(df_end2end['Average BrakeStatus'][i])
                Variables.baseline_climate_brake.append(df_baseline['Average BrakeStatus'][i])
                Variables.end2end_climate_laneoff.append(df_end2end['Average LaneOffset'][i])
                Variables.baseline_climate_laneoff.append(df_baseline['Average LaneOffset'][i])
                Variables.end2end_climate_swa.append(df_end2end['Average SteeringWheelAngle'][i])
                Variables.baseline_climate_swa.append(df_baseline['Average SteeringWheelAngle'][i])
                Variables.end2end_climate_adas.append(df_end2end['ADAS#'][i])
                Variables.baseline_climate_adas.append(df_baseline['ADAS#'][i])
            elif i == 3:
                Variables.end2end_bt_duration.append(df_end2end['Task Duration'][i])
                Variables.baseline_bt_duration.append(df_baseline['Task Duration'][i])
                Variables.end2end_bt_step.append(df_end2end['Task Steps'][i])
                Variables.baseline_bt_step.append(df_baseline['Task Steps'][i])
                Variables.end2end_bt_velocity.append(df_end2end['Average Velocity'][i])
                Variables.baseline_bt_velocity.append(df_baseline['Average Velocity'][i])
                Variables.end2end_bt_hr.append(df_end2end['Average HR'][i])
                Variables.baseline_bt_hr.append(df_baseline['Average HR'][i])
                Variables.end2end_bt_acc.append(df_end2end['Average Acceleration'][i])
                Variables.baseline_bt_acc.append(df_baseline['Average Acceleration'][i])
                Variables.end2end_bt_brake.append(df_end2end['Average BrakeStatus'][i])
                Variables.baseline_bt_brake.append(df_baseline['Average BrakeStatus'][i])
                Variables.end2end_bt_laneoff.append(df_end2end['Average LaneOffset'][i])
                Variables.baseline_bt_laneoff.append(df_baseline['Average LaneOffset'][i])
                Variables.end2end_bt_swa.append(df_end2end['Average SteeringWheelAngle'][i])
                Variables.baseline_bt_swa.append(df_baseline['Average SteeringWheelAngle'][i])
                Variables.end2end_bt_adas.append(df_end2end['ADAS#'][i])
                Variables.baseline_bt_adas.append(df_baseline['ADAS#'][i])
            elif i == 4:
                Variables.end2end_park_duration.append(df_end2end['Task Duration'][i])
                Variables.baseline_park_duration.append(df_baseline['Task Duration'][i])
                Variables.end2end_park_step.append(df_end2end['Task Steps'][i])
                Variables.baseline_park_step.append(df_baseline['Task Steps'][i])
                Variables.end2end_park_velocity.append(df_end2end['Average Velocity'][i])
                Variables.baseline_park_velocity.append(df_baseline['Average Velocity'][i])
                Variables.end2end_park_hr.append(df_end2end['Average HR'][i])
                Variables.baseline_park_hr.append(df_baseline['Average HR'][i])
                Variables.end2end_park_acc.append(df_end2end['Average Acceleration'][i])
                Variables.baseline_park_acc.append(df_baseline['Average Acceleration'][i])
                Variables.end2end_park_brake.append(df_end2end['Average BrakeStatus'][i])
                Variables.baseline_park_brake.append(df_baseline['Average BrakeStatus'][i])
                Variables.end2end_park_laneoff.append(df_end2end['Average LaneOffset'][i])
                Variables.baseline_park_laneoff.append(df_baseline['Average LaneOffset'][i])
                Variables.end2end_park_swa.append(df_end2end['Average SteeringWheelAngle'][i])
                Variables.baseline_park_swa.append(df_baseline['Average SteeringWheelAngle'][i])
                Variables.end2end_park_adas.append(df_end2end['ADAS#'][i])
                Variables.baseline_park_adas.append(df_baseline['ADAS#'][i])


import matplotlib.pyplot as plt
import numpy as np

# plot pie chart

def calculateMean(listVal):
    return np.mean(listVal)

end2end_map_duration_mean = calculateMean(Variables.end2end_map_duration)
baseline_map_duration_mean = calculateMean(Variables.baseline_map_duration)

end2end_mcs_duration_mean = calculateMean(Variables.end2end_mcs_duration)
baseline_mcs_duration_mean = calculateMean(Variables.baseline_mcs_duration)

end2end_climate_duration_mean = calculateMean(Variables.end2end_climate_duration)
baseline_climate_duration_mean = calculateMean(Variables.baseline_climate_duration)

end2end_bt_duration_mean = calculateMean(Variables.end2end_bt_duration)
baseline_bt_duration_mean = calculateMean(Variables.baseline_bt_duration)

end2end_park_duration_mean = calculateMean(Variables.end2end_park_duration)
baseline_park_duration_mean = calculateMean(Variables.baseline_park_duration)

means_end2end_duration = (end2end_map_duration_mean, end2end_mcs_duration_mean, end2end_climate_duration_mean, end2end_bt_duration_mean, end2end_park_duration_mean)
means_baseline_duration = (baseline_map_duration_mean, baseline_mcs_duration_mean, baseline_climate_duration_mean, baseline_bt_duration_mean, baseline_park_duration_mean)

fig, ax = plt.subplots()
index = np.arange(5)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_end2end_duration, bar_width,
                 alpha=opacity,
                 color='b',
                 label='End2End')

rects2 = plt.bar(index + bar_width, means_baseline_duration, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Baseline')

plt.xlabel('Tasks')
plt.ylabel('Duration')
plt.title('Duration by Tasks')
plt.xticks(index + bar_width, ('open map', 'mcs', 'climate', 'bluetooth audio', 'park'))
plt.legend()

plt.tight_layout()

end2end_map_step_mean = calculateMean(Variables.end2end_map_step)
baseline_map_step_mean = calculateMean(Variables.baseline_map_step)

end2end_mcs_step_mean = calculateMean(Variables.end2end_mcs_step)
baseline_mcs_step_mean = calculateMean(Variables.baseline_mcs_step)

end2end_climate_step_mean = calculateMean(Variables.end2end_climate_step)
baseline_climate_step_mean = calculateMean(Variables.baseline_climate_step)

end2end_bt_step_mean = calculateMean(Variables.end2end_bt_step)
baseline_bt_step_mean = calculateMean(Variables.baseline_bt_step)

end2end_park_step_mean = calculateMean(Variables.end2end_park_step)
baseline_park_step_mean = calculateMean(Variables.baseline_park_step)

means_end2end_step = (end2end_map_step_mean, end2end_mcs_step_mean, end2end_climate_step_mean, end2end_bt_step_mean, end2end_park_step_mean)
means_baseline_step = (baseline_map_step_mean, baseline_mcs_step_mean, baseline_climate_step_mean, baseline_bt_step_mean, baseline_park_step_mean)

fig, ax = plt.subplots()
index = np.arange(5)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_end2end_step, bar_width,
                 alpha=opacity,
                 color='b',
                 label='End2End')

rects2 = plt.bar(index + bar_width, means_baseline_step, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Baseline')

plt.xlabel('Tasks')
plt.ylabel('Steps')
plt.title('Steps by Tasks')
plt.xticks(index + bar_width, ('open map', 'mcs', 'climate', 'bluetooth audio', 'park'))
plt.legend()

# plt.show()



# plot HR
data = np.array( Variables.end2end_map_hr )
plt.figure('HR Value')
plt.subplot(2,5,1)
plt.ylabel('Heart Rate')
plt.xlabel('Open Map Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_mcs_hr )
plt.subplot(2,5,2)
plt.ylabel('Heart Rate')
plt.xlabel('MCS Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_climate_hr )
plt.subplot(2,5,3)
plt.ylabel('Heart Value')
plt.xlabel('Climate Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_bt_hr )
plt.subplot(2,5,4)
plt.ylabel('Heart Value')
plt.xlabel('Bluetooth Audio Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_park_hr )
plt.subplot(2,5,5)
plt.ylabel('Heart Rate')
plt.xlabel('Parking Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_map_hr )
plt.subplot(2,5,6)
plt.ylabel('Heart Rate')
plt.xlabel('Open Map Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_mcs_hr )
plt.subplot(2,5,7)
plt.ylabel('Heart Rate')
plt.xlabel('MCS Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_climate_hr )
plt.subplot(2,5,8)
plt.ylabel('Heart Rate')
plt.xlabel('Climate Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_bt_hr )
plt.subplot(2,5,9)
plt.ylabel('Heart Rate')
plt.xlabel('Bluetoot Audio Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_park_hr )
plt.subplot(2,5,10)
plt.ylabel('Heart Rate')
plt.xlabel('Park Task Baseline')
plt.boxplot(data, 0, 'gD')

# plot task Duration
data = np.array( Variables.end2end_map_duration )
plt.figure('Task Duration')
plt.subplot(2,5,1)
plt.ylabel('Task Duration')
plt.xlabel('Open Map Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_mcs_duration )
plt.subplot(2,5,2)
plt.ylabel('Task Duration')
plt.xlabel('MCS Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_climate_duration )
plt.subplot(2,5,3)
plt.ylabel('Task Duration')
plt.xlabel('Climate Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_bt_duration )
plt.subplot(2,5,4)
plt.ylabel('Task Duration')
plt.xlabel('Bluetooth Audio Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_park_duration )
plt.subplot(2,5,5)
plt.ylabel('Task Duration')
plt.xlabel('Parking Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_map_duration )
plt.subplot(2,5,6)
plt.ylabel('Task Duration')
plt.xlabel('Open Map Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_mcs_duration )
plt.subplot(2,5,7)
plt.ylabel('Task Duration')
plt.xlabel('MCS Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_climate_duration )
plt.subplot(2,5,8)
plt.ylabel('Task Duration')
plt.xlabel('Climate Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_bt_duration )
plt.subplot(2,5,9)
plt.ylabel('Task Duration')
plt.xlabel('Bluetoot Audio Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_park_duration )
plt.subplot(2,5,10)
plt.ylabel('Task Duration')
plt.xlabel('Park Task Baseline')
plt.boxplot(data, 0, 'gD')

# plot task steps
data = np.array( Variables.end2end_map_step )
plt.figure('Task Steps')
plt.subplot(2,5,1)
plt.ylabel('Task Steps')
plt.xlabel('Open Map Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_mcs_step )
plt.subplot(2,5,2)
plt.ylabel('Task Steps')
plt.xlabel('MCS Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_climate_step )
plt.subplot(2,5,3)
plt.ylabel('Task Steps')
plt.xlabel('Climate Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_bt_step )
plt.subplot(2,5,4)
plt.ylabel('Task Steps')
plt.xlabel('Bluetooth Audio Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_park_step )
plt.subplot(2,5,5)
plt.ylabel('Task Steps')
plt.xlabel('Parking Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_map_step )
plt.subplot(2,5,6)
plt.ylabel('Task Steps')
plt.xlabel('Open Map Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_mcs_step )
plt.subplot(2,5,7)
plt.ylabel('Task Steps')
plt.xlabel('MCS Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_climate_step )
plt.subplot(2,5,8)
plt.ylabel('Task Steps')
plt.xlabel('Climate Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_bt_step )
plt.subplot(2,5,9)
plt.ylabel('Task Steps')
plt.xlabel('Bluetoot Audio Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_park_step )
plt.subplot(2,5,10)
plt.ylabel('Task Steps')
plt.xlabel('Park Task Baseline')
plt.boxplot(data, 0, 'gD')

# plot average velocity
data = np.array( Variables.end2end_map_velocity )
plt.figure('Average Velocity')
plt.subplot(2,5,1)
plt.ylabel('Average Velocity')
plt.xlabel('Open Map Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_mcs_velocity )
plt.subplot(2,5,2)
plt.ylabel('Average Velocity')
plt.xlabel('MCS Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_climate_velocity )
plt.subplot(2,5,3)
plt.ylabel('Average Velocity')
plt.xlabel('Climate Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_bt_velocity )
plt.subplot(2,5,4)
plt.ylabel('Average Velocity')
plt.xlabel('Bluetooth Audio Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_park_velocity )
plt.subplot(2,5,5)
plt.ylabel('Average Velocity')
plt.xlabel('Parking Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_map_velocity )
plt.subplot(2,5,6)
plt.ylabel('Average Velocity')
plt.xlabel('Open Map Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_mcs_velocity )
plt.subplot(2,5,7)
plt.ylabel('Average Velocity')
plt.xlabel('MCS Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_climate_velocity )
plt.subplot(2,5,8)
plt.ylabel('Average Velocity')
plt.xlabel('Climate Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_bt_velocity )
plt.subplot(2,5,9)
plt.ylabel('Average Velocity')
plt.xlabel('Bluetoot Audio Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_park_velocity )
plt.subplot(2,5,10)
plt.ylabel('Average Velocity')
plt.xlabel('Park Task Baseline')
plt.boxplot(data, 0, 'gD')

# plot average ACC
data = np.array( Variables.end2end_map_acc )
plt.figure('Average ACC')
plt.subplot(2,5,1)
plt.ylabel('Average ACC')
plt.xlabel('Open Map Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_mcs_acc )
plt.subplot(2,5,2)
plt.ylabel('Average ACC')
plt.xlabel('MCS Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_climate_acc )
plt.subplot(2,5,3)
plt.ylabel('Average ACC')
plt.xlabel('Climate Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_bt_acc )
plt.subplot(2,5,4)
plt.ylabel('Average ACC')
plt.xlabel('Bluetooth Audio Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_park_acc )
plt.subplot(2,5,5)
plt.ylabel('Average ACC')
plt.xlabel('Parking Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_map_acc )
plt.subplot(2,5,6)
plt.ylabel('Average ACC')
plt.xlabel('Open Map Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_mcs_acc )
plt.subplot(2,5,7)
plt.ylabel('Average ACC')
plt.xlabel('MCS Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_climate_acc )
plt.subplot(2,5,8)
plt.ylabel('Average ACC')
plt.xlabel('Climate Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_bt_acc )
plt.subplot(2,5,9)
plt.ylabel('Average ACC')
plt.xlabel('Bluetoot Audio Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_park_acc )
plt.subplot(2,5,10)
plt.ylabel('Average ACC')
plt.xlabel('Park Task Baseline')
plt.boxplot(data, 0, 'gD')

# plot average Brake Status
data = np.array( Variables.end2end_map_brake )
plt.figure('Average Brake Status')
plt.subplot(2,5,1)
plt.ylabel('Average Brake Status')
plt.xlabel('Open Map Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_mcs_brake )
plt.subplot(2,5,2)
plt.ylabel('Average Brake Status')
plt.xlabel('MCS Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_climate_brake )
plt.subplot(2,5,3)
plt.ylabel('Average Brake Status')
plt.xlabel('Climate Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_bt_brake )
plt.subplot(2,5,4)
plt.ylabel('Average Brake Status')
plt.xlabel('Bluetooth Audio Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_park_brake )
plt.subplot(2,5,5)
plt.ylabel('Average Brake Status')
plt.xlabel('Parking Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_map_brake )
plt.subplot(2,5,6)
plt.ylabel('Average Brake Status')
plt.xlabel('Open Map Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_mcs_brake )
plt.subplot(2,5,7)
plt.ylabel('Average Brake Status')
plt.xlabel('MCS Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_climate_brake )
plt.subplot(2,5,8)
plt.ylabel('Average Brake Status')
plt.xlabel('Climate Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_bt_brake )
plt.subplot(2,5,9)
plt.ylabel('Average Brake Status')
plt.xlabel('Bluetoot Audio Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_park_brake )
plt.subplot(2,5,10)
plt.ylabel('Average Brake Status')
plt.xlabel('Park Task Baseline')
plt.boxplot(data, 0, 'gD')

# plot average LaneOffset
data = np.array( Variables.end2end_map_laneoff )
plt.figure('Average Lane Offset')
plt.subplot(2,5,1)
plt.ylabel('Average LaneOffset')
plt.xlabel('Open Map Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_mcs_laneoff )
plt.subplot(2,5,2)
plt.ylabel('Average LaneOffset')
plt.xlabel('MCS Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_climate_laneoff )
plt.subplot(2,5,3)
plt.ylabel('Average LaneOffset')
plt.xlabel('Climate Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_bt_laneoff )
plt.subplot(2,5,4)
plt.ylabel('Average LaneOffset')
plt.xlabel('Bluetooth Audio Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_park_laneoff )
plt.subplot(2,5,5)
plt.ylabel('Average LaneOffset')
plt.xlabel('Parking Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_map_laneoff )
plt.subplot(2,5,6)
plt.ylabel('Average LaneOffset')
plt.xlabel('Open Map Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_mcs_laneoff )
plt.subplot(2,5,7)
plt.ylabel('Average LaneOffset')
plt.xlabel('MCS Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_climate_laneoff )
plt.subplot(2,5,8)
plt.ylabel('Average LaneOffset')
plt.xlabel('Climate Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_bt_laneoff )
plt.subplot(2,5,9)
plt.ylabel('Average LaneOffset')
plt.xlabel('Bluetoot Audio Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_park_laneoff )
plt.subplot(2,5,10)
plt.ylabel('Average LaneOffset')
plt.xlabel('Park Task Baseline')
plt.boxplot(data, 0, 'gD')

# plot average Steering Wheel Angle
data = np.array( Variables.end2end_map_swa )
plt.figure('Average Steering Wheel Angle')
plt.subplot(2,5,1)
plt.ylabel('Average LaneOffset')
plt.xlabel('Open Map Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_mcs_swa )
plt.subplot(2,5,2)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('MCS Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_climate_swa )
plt.subplot(2,5,3)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('Climate Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_bt_swa )
plt.subplot(2,5,4)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('Bluetooth Audio Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.end2end_park_swa )
plt.subplot(2,5,5)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('Parking Task End2End')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_map_swa )
plt.subplot(2,5,6)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('Open Map Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_mcs_swa )
plt.subplot(2,5,7)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('MCS Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_climate_swa )
plt.subplot(2,5,8)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('Climate Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_bt_swa )
plt.subplot(2,5,9)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('Bluetoot Audio Task Baseline')
plt.boxplot(data, 0, 'gD')

data = np.array( Variables.baseline_park_swa )
plt.subplot(2,5,10)
plt.ylabel('Average Steering Wheel Angle')
plt.xlabel('Park Task Baseline')
plt.boxplot(data, 0, 'gD')

plt.show()
