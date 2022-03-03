#! /usr/bin/python3
import datetime as dt
import numpy as np

class logfile():
    def __init__(self, name, *args):
        self.filename = name
        self.data_array = np.array([np.zeros(len(args) + 2)])

        f = open(name, 'w')
        f.write('%s %s' %('Time(H : M : S)  ', 'Pressure (mbar)   '))

        for arg in args:
            f.write(arg+'   ')
    
    def logdata(self, *args): #writes data to log file
        f = open(self.filename, 'a') 

        f.write('\n%s   ' %(dt.datetime.now().strftime('%H:%M:%S')))

        for arg in args:
            f.write(arg+'   ')

    def update_array(self, now_data):
        self.data_array = np.append(growthlog.data_array, now_data, axis = 0)

start_time = dt.datetime.now()

time_now = dt.datetime.now()

elapsed = time_now - start_time

sample_num = 'DYT080'

#feed cell names from input file into a list. use list index in logfile argument to access

growthlog = logfile('%s_%s_substrate_prep' %(time_now.strftime('%m-%d-%y'), sample_num), 'cell_2_temp', 'cell_4_temp') #i.e. list[0], list[1] will contain cell names

growthlog.logdata(press_now, cell_temp4 ,cell_temp2)

seconds_now = time_now.time() - start_time.time()

growthlog.update_array([[elapsed.total_seconds(), pressure_now, cell_temp4 ,cell_temp2]])
