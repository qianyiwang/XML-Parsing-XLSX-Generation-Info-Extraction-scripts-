# data process step 3 generates task and baseline task sheets and the feature titles for each subject
import pandas
from openpyxl import load_workbook
import os
rootdir = 'C:\ClinicServer\Excel'
for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        print 'processing on %s' % f
        book = load_workbook('C:/ClinicServer/Excel/%s' % f)
        writer = pandas.ExcelWriter('C:/ClinicServer/Excel/%s' % f, engine='openpyxl')
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        df = pandas.DataFrame({'Task Name':[],'Task Start Time':[], 'Task End Time':[], 'Task Duration':[],
        'Task Steps': [], 'Task Mistake #':[], 'Task Assistance #': [], 'Average HR':[],
        'Average Velocity':[], 'Average Acceleration':[], 'Average BrakeStatus':[], 'Average LaneOffset':[], 'ADAS #':[]})
        df.to_excel(writer, "Task", columns=['Task Name','Task Start Time', 'Task End Time', 'Task Duration',
        'Task Steps', 'Task Mistake #', 'Task Assistance #', 'Average HR',
        'Average Velocity', 'Average Acceleration', 'Average BrakeStatus', 'Average LaneOffset', 'ADAS #'], index=False)

        df.to_excel(writer, "Baseline Task", columns=['Task Name','Task Start Time', 'Task End Time', 'Task Duration',
        'Task Steps', 'Task Mistake #', 'Task Assistance #', 'Average HR',
        'Average Velocity', 'Average Acceleration', 'Average BrakeStatus', 'Average LaneOffset', 'ADAS #'], index=False)

        writer.save()
        print '%s is done \n' % f
