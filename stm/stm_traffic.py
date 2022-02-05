# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/12/21
"""

from statemachine import StateMachine, State


class TrafficLightMachine(StateMachine):
    "A traffic light machine"
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    cycle = green.to(yellow) | yellow.to(red) | red.to(green)

    def on_enter_green(self):
        print('Green')

    def on_enter_yellow(self):
        print('Yellow')

    def on_enter_red(self):
        print('Red')


if __name__ == '__main__':
    stm = TrafficLightMachine()
    stm.cycle()
    stm.cycle()
    stm.cycle()
