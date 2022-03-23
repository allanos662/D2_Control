#! /usr/bin/python3
from Eurotherm import growth

class growth():

    def __init__(self, params):
        self.recipe = params['recipe']
        self.logfile = open('path', w)
    
    def log(self, phase, step):
        self.logfile.write(f'{dt.datetime.now] \t {self.gettemp()} \t {self.getpower()'}

    def execute(self, phase, step):
        params = self.recipe[phase]['step_'+str(step)]
        in_progress =  self.recipe[phase]['step_'+str(step)]['in_progress']
       
        if params['type'] = 'ramp':
            print(f'set temp to {params["T_target"]}')
            print(f'set rate to {params["T_rate"]}')
            set in_progress = 1

        if params['type'] = 'soak':
            print(f'set temp to {params["T_soak"]}')
            print(f'set {params["time_start"]} to {datetime.dt.now()}')
            set in_progress = 1

    def step_complete(self, phase, step)
        gettemp = 300
        params = self.recipe[phase]['step_'+str(step)]
        complete =  self.recipe[phase]['step_'+str(step)]['complete']
        in_progress =  self.recipe[phase]['step_'+str(step)]['in_progress']

        if params['type'] = 'ramp':
            print(f'if T =  {params["T_target"]} return 1')
            if gettemp = params["T_target"]:
                complete = 1
                in_progress = 0

                return 1
            else:
                return 0

        if params['type'] = 'soak':
            print(f'if now - {params["time_start"]} ')

    def step_running(self, phase, step): #tells whether the requested step in progress
        in_progress =  self.recipe[phase]['step_'+str(step)]['in_progress']
        if in_progress = 1:
            return 1
        if in_progress = 0:
            return 0

    def step_state(self, phase, step):
        running = 0
        complete = 0

        if step_running(phase, step):
            running = 1

        if step_complete(phase, step):
            complete = 1

        return (running , complete)

    def step_increment(self, phase, step):
        counter = self.recipe['phase']['step_counter']
        counter += 1

    def num_steps(self, phase):
        for key in self.recipe['phase']:
            num_steps += 1
        return num_steps - 1

with open('input.yaml', 'r') as file:
    growth_parameters = yaml.safe_load(file)

cell = growth(growth_parameters['cell_2'])
logfile = 

while(1):
    #degas phase
    phase = 'degas' 
    step = cell.recipe['phase']['step_counter']

    log('everything')

    if cell.step_state(phase, step) = (0, 0):
        #if step of phase hasn't begun or hasn't already been completed
        #then execute that step
        cell.execute(phase, step)

    if cell.step_state(phase, step) = (0, 1)):
        #if step of phase is no longer "in progress" and has been completed,
        #then increment so that the cell begins the next step on subsequent
        #while loop iteration
        cell.step_increment(phase)
        step = cell.recipe['phase']['step_counter']

    if step > cell.num_steps(phase):
        break

