#! /usr/bin/python3
import yaml
import threading
import time

#load YAML
with open('input.yaml', 'r') as file:
    growth_parameters = yaml.safe_load(file)

active_cells = {k:v for (k,v) in growth_parameters['cells'].items() if growth_parameters['cells'][k]['use']}

manip = Manipulator('COM2', 1, growth_paramaters['Manipulator'])
cell2 = HT_cell('COM2', 2, growth_paramaters['cell_2'])
cell3 = HT_cell('COM2', 3, growth_paramaters['cell_3'])
cell4 = DF_cell('COM2', 4, growth_paramaters['cell_4'])
cell5 = DF_cell('COM2', 5, growth_paramaters['cell_5'])
cell6 = DF_cell('COM2', 6, growth_paramaters['cell_6'])
cell7 = DF_cell('COM2', 7, growth_paramaters['cell_7'])
cell8 = LT_cell('COM2', 8, growth_paramaters['cell_8'])
cell9 = LT_cell('COM2', 9, growth_paramaters['cell_8'])
cell10 =

cell4.initialize()
cell10.initialize()
manip.initialize()

cell4.degas()
cell10.degas()
manip.degas()

#flux check
print('Ready to measure flux [y/n]')

if y 





#thread 1


print(active_cells)
