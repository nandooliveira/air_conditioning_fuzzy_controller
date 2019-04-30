import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class AirConditioningFuzzyController:
    def __init__(self):
        # linguistic variables
        self.temperature = ctrl.Antecedent(np.arange(0, 46, 1), 'temperature')
        self.humidity = ctrl.Antecedent(np.arange(0, 20, 1), 'humidity')
        self.people_count = ctrl.Antecedent(np.arange(0, 25, 1), 'people_count')
        self.fan_speed = ctrl.Consequent(np.arange(0, 1601, 1), 'fan_speed')

        self.init_temperature_terms()
        self.init_humidity_terms()
        self.init_people_count_terms()
        self.init_fan_speed_terms()

        self.setup_rules()

    def init_temperature_terms(self):
        self.temperature['Too-cold'] = fuzz.trimf(self.temperature.universe, [0, 0, 10])
        self.temperature['cold'] = fuzz.trimf(self.temperature.universe, [5, 10, 20])
        self.temperature['warm'] = fuzz.trimf(self.temperature.universe, [15, 20, 25])
        self.temperature['hot'] = fuzz.trimf(self.temperature.universe, [25, 30, 35])
        self.temperature['Too-hot'] = fuzz.trimf(self.temperature.universe, [35, 40, 40])

    def init_humidity_terms(self):
        self.humidity['low'] = fuzz.trimf(self.humidity.universe, [0, 0, 10])
        self.humidity['medium'] = fuzz.trimf(self.humidity.universe, [5, 10, 15])
        self.humidity['high'] = fuzz.trimf(self.humidity.universe, [10, 15, 20])

    def init_people_count_terms(self):
        self.people_count['low'] = fuzz.trimf(self.people_count.universe, [0, 5, 10])
        self.people_count['medium'] = fuzz.trimf(self.people_count.universe, [5, 15, 20])
        self.people_count['high'] = fuzz.trimf(self.people_count.universe, [15, 20, 25])

    def init_fan_speed_terms(self):
        self.fan_speed['low'] = fuzz.trimf(self.fan_speed.universe, [0, 0, 800])
        self.fan_speed['medium'] = fuzz.trimf(self.fan_speed.universe, [400, 800, 1200])
        self.fan_speed['high'] = fuzz.trimf(self.fan_speed.universe, [800, 1200, 1600])

    def show_temperature_graph(self):
        self.temperature.view()

    def show_humidity_graph(self):
        self.humidity.view()

    def show_people_count_graph(self):
        self.people_count.view()

    def show_fan_speed_graph(self, sim=None):
        self.fan_speed.view(sim=sim) if sim else self.fan_speed.view()

    def setup_rules(self):
        self.rules = [
            ctrl.Rule(self.temperature['hot'] | self.humidity['low'] | self.people_count['high'], self.fan_speed['high']),
            ctrl.Rule(self.temperature['hot'] | self.humidity['high'] | self.people_count['medium'], self.fan_speed['medium']),

            ctrl.Rule(self.humidity['medium'], self.fan_speed['medium']),

            ctrl.Rule(self.temperature['Too-hot'] | self.humidity['low'] | self.people_count['medium'], self.fan_speed['high']),
            ctrl.Rule(self.temperature['Too-hot'] | self.humidity['high'] | self.people_count['medium'], self.fan_speed['medium']),

            ctrl.Rule(self.temperature['cold'] | self.humidity['low'] | self.people_count['low'], self.fan_speed['low']),
            ctrl.Rule(self.temperature['cold'] | self.humidity['high'] | self.people_count['medium'], self.fan_speed['low']),

            ctrl.Rule(self.temperature['warm'] | self.humidity['low'] | self.people_count['low'], self.fan_speed['medium']),
            ctrl.Rule(self.temperature['warm'] | self.humidity['high'] | self.people_count['medium'], self.fan_speed['low']),

            ctrl.Rule(self.temperature['Too-cold'] | self.humidity['low'] | self.people_count['low'], self.fan_speed['low']),
            ctrl.Rule(self.temperature['Too-cold'] | self.humidity['high'] | self.people_count['low'], self.fan_speed['low'])
        ]
