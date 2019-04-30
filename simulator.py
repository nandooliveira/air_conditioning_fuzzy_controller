# -*- coding: utf-8 -*-

from skfuzzy import control as ctrl

from controller import AirConditioningFuzzyController

# simulation
air_conditioning_controller = AirConditioningFuzzyController()

air_conditioning_controller.show_temperature_graph()
temperature = input('Inform the temperature:')

air_conditioning_controller.show_humidity_graph()
humidity = input('Inform the humidity:')

air_conditioning_controller.show_people_count_graph()
people_count = input('Inform the people count:')

air_conditioning_controller.show_fan_speed_graph()

fan_speed_ctrl = ctrl.ControlSystem(air_conditioning_controller.rules)
speed = ctrl.ControlSystemSimulation(fan_speed_ctrl)

speed.input['temperature'] = int(temperature)
speed.input['humidity'] = int(humidity)
speed.input['people_count'] = int(people_count)

speed.compute()
print(speed.output['fan_speed'])
air_conditioning_controller.show_fan_speed_graph(sim=speed)

speed.print_state()

input('Press any key to exit')
