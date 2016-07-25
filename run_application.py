#!/usr/bin/python3

from scenarios import chasing_target, destroy_target
from application import video_control, core_logic, report_writer
import config_application
import sys

if int(sys.version_info.major) < 3:
    sys.stdout.write('You must use Python3 with this program, exiting... \n')
    sys.exit()

def do_scenario(scenario_chosen):
    if scenario_chosen == 'chasing_target':
        config = config_application.ConfigChasingTarget()
        database = config_application.DatabaseConfig(config)
        scenario = chasing_target.ChasingTargetScenario()
        core_logic.process_scenario(config, database, scenario)

    elif scenario_chosen == 'destroy_target':
        config = config_application.ConfigDestroyTarget()
        database = config_application.DatabaseConfig(config)
        scenario = destroy_target.DestroyTargetScenario()
        core_logic.process_scenario(config, database, scenario)

    else:
        print('%s is not a valid scenario' %(scenario_chosen))

def make_report(scenario_chosen):
    if scenario_chosen == 'chasing_target':
        config = config_application.ConfigChasingTarget()
        database = config_application.DatabaseConfig(config)
        report_writer.make_report(database, config.success_string)

    elif scenario_chosen == 'destroy_target':
        config = config_application.ConfigDestroyTarget()
        database = config_application.DatabaseConfig(config)
        report_writer.make_report(database, config.success_string)

    else:
        print('%s is not a valid scenario' %(scenario_chosen))

#def make_video(scenario_chosen):
#    print("from the application folder and animation_control module")

def process_inputs(inputs):
    action_chosen = inputs[1]
    scenario_chosen = inputs[2]
    if action_chosen == 'do_scenario':
        do_scenario(scenario_chosen)
    #elif action_chosen == 'make_video':
    #    make_video(scenario_chosen)
    elif action_chosen == 'make_report':
        make_report(scenario_chosen)
    else:
        print('%s is not a valid action' %(action_chosen))

def receive_inputs():
    inputs = sys.argv
    input_number_required = 3
    if len(inputs) == input_number_required:
        process_inputs(inputs)
    else:
        print('Enter your scenario to process. Eg -'
              ' ```python3 run_application.py do_scenario chasing_target``` '
              'is a valid one')

receive_inputs()
sys.exit()
