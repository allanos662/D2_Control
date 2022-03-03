import minimalmodbus
import datetime as dt
import numpy as np
import serial

class Eurotherm3500(minimalmodbus.Instrument): 

    def __init__(self, port, address):
        self.ser = minimalmodbus.Instrument(port, address)

    def get_temp(self):
        return self.ser.read_register(1, 1)
 
    def get_setpoint(self):
        return self.ser.read_register(2, 1)    
   
    def get_output(self):
        return self.ser.read_register(4, 1)    

    def get_OPHi(self):
        return self.ser.read_register(30, 1)    

    def get_OPLo(self):
        return self.ser.read_register(31, 1)    

    def get_Rate(self):
        return self.ser.read_register(35, 1)    

    def get_PIDs(self):
        return [self.ser.read_register(6, 1), self.ser.read_register(8, 1), self.ser.read_register(9, 1)]

    def set_temp(self, new_temp):
        self.ser.write_register(1, new_temp, 1)

    def set_rate(self,new_rate):
        self.ser.write_register(35, new_rate, 1)

    def set_OPHi(self, pow_max):
        return self.ser.read_register(30, pow_max, 1)    

    def set_OPLo(self, pow_min):
        return self.ser.read_register(31, pow_min, 1)

    def set_power(self, power):
        if self.is_manual():
            self.ser.write_register(3, power, new_rate, 1)
        else:
            self.set_manual()
            self.ser.write_register(3, power, new_rate, 1)

    def set_PIDs(self, values):
        self.ser.write_register(6, values[0], 1)
        self.ser.write_register(8, values[1], 1)
        self.ser.write_register(9, values[2], 1)

    def set_manual(self, value = 1):
        self.ser.write_register(273, value, 1)

    def set_auto(self, value = 0):
        self.ser.write_register(273, value, 1)

    def is_manual(self):
        if self.ser.read_register(273, 1):
            return 1
        else:
            return 0

'''
class general(Eurotherm3500):

    def PID_value(self):
      #if mag([self.P(), self.I(), self.D()] - PIDs['high']) < 0.1
            #return 3

      ###if mag([self.P(), self.I(), self.D()] - PIDs['mid']) < 0.1
            #return 2

      ###if mag([self.P(), self.I(), self.D()] - PIDs['low']) < 0.1
            #return 1
        pass

    def checkPIDs(temp_now):
        if temp_now > 700 and self.PID_value() != 3:
            self.ser.setPID(PIDs['high'])
            print('setting PID to "high"')
        if temp_now < 700 and temp_now > 250 and self.PID_value() != 2:
            self.ser.setPID(PIDs['mid'])
            print('setting PID to "mid"')
        if temp_now < 250 and self.PID_value() != 1:
            self.ser.setPID(PIDs['low'])
            print('setting PID to "low"')

    def ramp_temp(self, setpoint, rate):
        self.set_rate(rate)
        self.set_temp(setpoint)


        print('Ramping to setpoint...')

        while(1): #wait for target to be reached
            #log_data

            if abs(setpoint - temp_now) < 0.5:
                if j == 1:
                    print('loop settling...')
                    j = 2

                if self.settled(temp, recent_data):
                    print('settled')
                    #update
                    break

    def hold_temp(self, temp):

    def wait(): #wait for cell to settle

class Manipulator(Eurotherm);
    specifics such as PID parameters and register calls that are unique to this instrument

    self.PID = {'high' : [42.4, 24, 4], 'mid' : [36.2, 37, 6], 'low' : [53.4, 86, 14]}
class HL_cell(general):

class HT_cell(general):

class LT_cell(general):

class Cracker(general):
'''

