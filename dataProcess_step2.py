# data process step 2 is used to generate excel file for each subject
import xml.etree.ElementTree as ET
import xlsxwriter
import os

rootdir = 'C:\ClinicServer\data_process'
for subdir, dirs, files in os.walk(rootdir):
    for idx in range(1, len(files)/4+1):
        workbook = xlsxwriter.Workbook('Excel/Subject%s.xlsx' % idx)
        worksheet_event = workbook.add_worksheet('Event')
        worksheet_data = workbook.add_worksheet('Data')
        worksheet_baseline_event = workbook.add_worksheet('BaselineEvent')
        worksheet_baseline_data = workbook.add_worksheet('BaselineData')

        # read event tree and write to Event sheet
        print 'Working on data_process/Subject%s_Event.xml' % idx
        eventTree = ET.parse('data_process/Subject%s_Event.xml' % idx)
        root = eventTree.getroot()
        rowNum = len(root)
        columnNum = len(root[0])
        for row in range(0,len(root)):
        	for column in range(0,len(root[row])):
        		if(row == 0):
        			worksheet_event.write(0, column, str(root[0][column].tag))
        		else:
        			worksheet_event.write(row, column, root[row][column].text)

        # read data tree and write to Event sheet
        print 'Working on data_process/Subject%s_Data.xml' % idx
        eventTree = ET.parse('data_process/Subject%s_Data.xml' % idx)
        root = eventTree.getroot()
        rowNum = len(root)
        columnNum = len(root[0])
        for row in range(0,len(root)):
        	for column in range(0,len(root[row])):
        		if(row == 0):
        			worksheet_data.write(0, column, str(root[0][column].tag))
        		else:
        			worksheet_data.write(row, column, root[row][column].text)

        # read baseline event tree and write to Event sheet
        print 'Working on data_process/Subject%s_BaselineEvent.xml' % idx
        eventTree = ET.parse('data_process/Subject%s_BaselineEvent.xml' % idx)
        root = eventTree.getroot()
        rowNum = len(root)
        columnNum = len(root[0])
        for row in range(0,len(root)):
            for column in range(0,len(root[row])):
                if(row == 0):
                    worksheet_baseline_event.write(0, column, str(root[0][column].tag))
                else:
                    worksheet_baseline_event.write(row, column, root[row][column].text)

        # read data tree and write to Event sheet
        print 'Working on data_process/Subject%s_BaselineData.xml' % idx + '\n'
        eventTree = ET.parse('data_process/Subject%s_BaselineData.xml' % idx)
        root = eventTree.getroot()
        for row in range(0,len(root)):
        	for column in range(0,len(root[row])):
        		if(row == 0):
        			worksheet_baseline_data.write(0, column, str(root[0][column].tag))
        		else:
        			worksheet_baseline_data.write(row, column, root[row][column].text)

        workbook.close()
