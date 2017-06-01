# data process step 1 is used to clean the vehicle data, remove the duplicate in every two seconds

import os
import xml.etree.ElementTree as ET
from lxml import etree
import shutil
rootdir = 'C:\ClinicServer\data'

for subdir, dirs, files in os.walk(rootdir):
    print len(files)
    for file in files:
        fileName = os.path.join(subdir, file)
    	if 'Data' in file:
            print 'Processing ' + file + ' ... '
            try:
                eventTree = ET.parse(fileName)
                root = eventTree.getroot()
                # rowNum = len(root)
                # columnNum = len(root[0])
                root_process = etree.Element(file)

                time = []
                hr = []
                adas = []
                velocity = []
                acceleration = []
                brake_state = []
                steering_wheel_angle = []
                lane_offset = []
                location = []
                simulator_time = []
                road_id = []

                for row in range(0, len(root)):
                    flag = True
                    data_array = []
                    for column in range(0, len(root[row])):
                        data_array.append(root[row][column].text)
                        # print root[row][column].tag, root[row][column].text
                    if row % 2 == 1:
                        simulator = data_array[9]
                        time.append(data_array[0])
                        hr.append(data_array[1])
                        adas.append(data_array[2])
                        velocity.append(data_array[3])
                        acceleration.append(data_array[4])
                        brake_state.append(data_array[5])
                        steering_wheel_angle.append(data_array[6])
                        lane_offset.append(data_array[7])
                        location.append(data_array[8])
                        simulator_time.append(data_array[9])
                        road_id.append(data_array[10])
                root_process = etree.Element('%s' % file)
                for i in range(0, len(hr)):
                    task_process = etree.SubElement(root_process, "Data")
                    etree.SubElement(task_process, "Time").text = time[i]
                    etree.SubElement(task_process, "HR").text = hr[i]
                    etree.SubElement(task_process, "ADAS").text = adas[i]
                    etree.SubElement(task_process, "Velocity").text = velocity[i]
                    etree.SubElement(task_process, "Acceleration").text = acceleration[i]
                    etree.SubElement(task_process, "BrakeState").text = brake_state[i]
                    etree.SubElement(task_process, "SteeringWheelAngle").text = steering_wheel_angle[i]
                    etree.SubElement(task_process, "LaneOffset").text = lane_offset[i]
                    etree.SubElement(task_process, "Location").text = location[i]
                    etree.SubElement(task_process, "SimulatorTime").text = simulator_time[i]
                    etree.SubElement(task_process, "RoadID").text = road_id[i]
                et = etree.ElementTree(root_process)
                et.write('data_process/%s' % file, pretty_print=True)
                print 'Process successfully' + '\n'
            except:
                print 'Unexpected error' + '\n'
        else:
            shutil.copy2(fileName, 'C:\ClinicServer\data_process')
