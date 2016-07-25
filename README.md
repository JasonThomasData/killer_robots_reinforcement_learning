##Reinforcement learning with Python
###Or, how I made killer robots

This project is an example of reinforcement learning, which is a type of machine learning. 

This approach starts with one or more agents that commence their lives with no memory. 

The aim is to reinforce behaviours that lead to good results, and discourage actions that lead to bad results.

###States and actions

The approach is for an agent, or virtual robot, to make observations about its environment and then take an action. At first these actions are random because the agent has no memory of what has worked previously.

For example, if an agent can observe what direction it faces and what direction its target/enemy is in, then for each turn the agent can select the move that has led to good results in previous generations.

My approach is different to most examples of reinforcement learning I've seen where rewards are given for each action. I aim to give my robots the bare minimum of feedback, only whether or not the result of the robot's actions were good or not. 

For that reason, my robots do not receive instant feedback. Instead, each robot pushes a tuple (observed state, action taken) to a list for all its turns.

The important part is at the end of each generation where a robot either succeeds or fails. On a bad result, the agent/robot will iterate over its list of tuples and for each observed state, will search a database for that record and subtract a point from that move's value. For a good result, the move for each corresponding state will increment one point.

This necessarily takes longer to achieve a result tha most reinforcement learning where each action would be rewarded instantly.

However, I find this sandbox approach more interesting and requires less work from me to give the robot feedback each turn - to think of all the edge cases that would affect the outcome.

At first these results will be poor, but after some time, we can expect the agent's cumulative success rate to approach 100%.

###Development environment

This project has been tested on Ubuntu 14.04 and Mint _____, and works. I really don't think this project will work on Windows, but haven't tested it on Windows (I don't use Windows sorry).

This project uses Python3.

###Installation

To use Tkinter, which is required, do this:

	sudo apt-get install pytho3-tk

If you do use a virtualenv (which is a great idea) and you've been using Python 2, use this:

	virtualenv --python=/usr/bin/python3 env

That spins up python3 inside your virtualenv. If you don't know how to initialise your virtualenv:

	source env/bin/activate

Pip will install PyMovie and pytest, and any dependencies those need.

###Testing

To run tests for this project, navigate to the tests folder and run this command from the terminal:

	py.test test_robot_sensors.py test_robot_actions.py test_win_lose_conditions.py

###Usage

You must run this program with Python 3. The program will boot you out if the version is not version 3+.

The files are run with the ```run_application.py``` file. You will need to pass in a param via the terminal. Like this: 

	python run_application.py do_scenario chasing_target

That will run through the chasing_target scenario.

To compile the video this scenario produces, do this command:

	python run_application.py make_video chasing_target

###Application structure

Here is a toplevel view of the program.

    python_reinforcement_learning/
        README.md
        requirements.txt
        run_application.py
        config_application.py
        database/
            chasing_target.db #can be deleted to start new test series
            destroy_target.db
        application/
            animation_control.py
            factory.py
            game_environment.py
            projectile_behaviour.py
            robot_decisions.py
            robot_actions.py
            robot_memory.py
            robot_decisions.py
            win_lose_conditions.py
            visual_display.py
            __init__.py
        scenarios/
            chasing_target.py
            destroy_target.py
            __init__.py
        animation/
            chasing_target/
                tmp_frames/
            destroy_target/
                tmp_frames/

Most functions that objects use are public functions stored in modules. To make a robot perform any action, you will need to pass the instance of that robot into the function as a parameter.

The interface for the human user is ```run_application.py```. The ```database```, ```config``` and ```scenario``` objects are created here. The scenario objects all contain a function that evaluates the rules for that particular scenario.

The ```core_logic.py``` module receives the database, config and scenario objects, and processes the (I suppose you would say) game loop. 

The ```animation_control.py``` module takes the contents of ```tmp_frames/``` and converts those to a video, and deletes contents of ```tmp_frames/```. This is one of two modules not run from the ```core_logic.py``` module, as it's a seperate concern from the machine learning task.

The ```report_writer.py``` module returns statistics to the terminal. One of two modules not run from the ```core_logic.py``` module.

The ```factory.py``` has classes for target, robot and projectile objects.

The ```game_environment.py``` has the class that contains the world where the robots live. That object has lists where all other objects are referenced. The world object is passed to other modules.

The ```visual_display.py``` file renders the objects to a canvas so those can be saved in ```tmp_frames```.

The scenarios folder contains modules with classes that receive the ```test_environment``` object as a paramter, and adds new instances of robots and targets accordingly. The scenario objects also have a function to check win conditions.

###Database structure

This project uses ```SQLite3```, which comes out of the box in Python.

Each scenario has its own ```.db``` file and each of those has two tables - a records table and a log table.

I am using integers to save the instances of what agents can observe, as intagers are easier/more efficient to search for than strings.

If the ```chasing_target scenario``` database was a csv file, this is what it would look like:

    state_int, turn_left, turn_right, move_forward
    13604, -3, 3, 0
    12104, -2, -9, 10
    13114, 5, -2, 4

So if an agent observes its board and decides the board corresponds to the ```state_int``` of ```10104``` then previous results tells the agent the best result is ```turn_right```, which depending on how advanced the machine's memory is, may or may not be the best thing to do.

All scenarios can share this schema, and scenarios that don't have certain actions as possibilities for the agents can just have extra zeros in those columns. Extra actions like ```fire_projectile``` can be added as new columns.

###Robot observations

Each robot, before making an action, can observe the state of its environment. For now, the ```state_int``` field (primary key for database) for all robots in all scenarios is -

	robot_id, target_direction, robot_health

So for robot with robot_id 1 that has a target directly in front, with health of 4, the state int will be `13604`.

The target direction needs explaining here. The robot knows which direction is facing and can learn which direction its target is in. However, for the purposes of evaluating its own environment, the robot only cares if its target is in front, left, right or behind, etc.

So this is managed by using triganometry to get the compass angle of the target with the robot at at compass centre. If the robot is facing east, for example, and its target is north then that's the same state as the robot facing north and its target west. So the target's direction is reduced to the context of the robot facing north. For a target east of a robot, where the robot is facing west, we give the robot a direction string of 180, as it's the same as a robot facing north and having its direction south. If the context of the robot's facing direction was not changed, there would be many more (I think 4 times as many) records in each database.

The directions are three character strings that are rounded up to the nearest integer, with a 0 in front. 

There are eight directions that represent targets directly in those directions - North (360), North-East (045), East (090), South-East (135), South (180), South-West (225), West (270), North-West (315).

Where a robot's target is in between those points, the target's direction is returned as in between. For example, for a target at (033), which is in between North and North-East, the direction is returned as the closest whole integer to North-North-East, which is (023).

###Scenarios

The available actions and available observations that robots can make are stored in the relevant config objects, inside the ```config_application.py``` module. Each scenario object is created and passed as a parameter from the main ```run_application.py```interface to the ```core_logic.py``` module. 

#####Chasing target

![Video of scenario](http://www.jason-thomas.xyz/static/assets/2016/RL_chasing_target_result.mp4)

This was the first scenario made for this application. This is where a robot either reaches the target location (success), takes too long (fail) or goes outside the test area (fail).

Each turn, these agents could ```turn_left```, ```turn_right``` and ```move_forward```.
	
    Success rates spanning intervals of 48 generations

    record_interval, test#1
    0, 81.25
    48, 77.08
    96, 93.75
    144, 85.42
    192, 91.67
    240, 85.42
    288, 79.17
    336, 89.58
    384, 97.92
    432, 97.92
    480, 95.83
    528, 95.83
    576, 93.75
    624, 97.92
    672, 97.92
    720, 93.75
    768, 97.92
    816, 95.83
    864, 97.92
    912, 100.00
    960, 100.00
    1008, 95.83
    1056, 100.00
    1104, 100.00
    1152, 97.92

#####Destroy target

![Video of scenario](http://www.jason-thomas.xyz/static/assets/2016/RL_chasing_target_result.mp4)

This scenario is where a robot must seek out and destroy its immobile target (success), or fall from the board or take too long (both fail).

The robot can ```move_forward```, ```move_left```, ```move_right```, ```move_backward```, ```turn_left```, ```turn_right```, ```fire_projectile```.

I was surprised to see the robots here perform better than the robots in the chasing_target scenario.

    Success rates spanning intervals of 48 generations

    record_interval, test#1, Test#2
    0, 45.83, 79.17
    48, 97.92, 95.83
    96, 100, 100
    144, 100, 100
    192, 100, 100
    240, 100, 100
    288, 100, 100
    336, 100, 100
    384, 100, 100
    432, 100, 100
    480, 100, 100
    528, 100, 100
    576, 100, 100
    624, 100, 100
    672, 100, 100
    720, 100, 100
    768, 100, 100
    816, 100, 100
    864, 100, 100
    912, 100, 100
    960, 100, 100
    1008, 100, 100
    1056, 100, 100
    1104, 100, 100
    1152, 100, 100

This scenario has the same states and actions the following scenario has.

#####Killer robots

To do... this is the point and intended result behind this entire project. Previous scenarios are effectively tests.

I'm most interested in creating an environment where agents can face each other in an arena.

It would be most interesting to have a single database for this, but use different tables for each robot, so that their memories can develop in parallel.

THERE CAN BE ONLY ONE.

###Future improvements

One thing I'm not really happy with is how the animation is accomplished. This is the process.
	
	1. Render the environment, including all objects, to a Tkinter canvas.
	2. Save the canvas as a postscript file in the animation folder.
	3. Use the ```os.system()``` to convert this file to a png.
	4. Save that png to the ```tmp_frames``` folder.
	5. Place all images in an image sequence list.
	6. Convert list to video.

This was the least important aspect of my application so I didn't spend too much time on this, but it's a little messy. 

Another option might be to save the board states to a list of states and then render those at the end and use a screen capture, but honestly that's also a messy approach.

I was suprised making canvas animations in Python was this difficult and will research better methods.