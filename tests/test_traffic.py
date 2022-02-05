# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/12/22
"""
from stm import TrafficLightMachine


class TestTrafficLightMachine:
    def setup(self):
        self.machine = TrafficLightMachine()

    def test_cycle(self):
        self.machine.cycle()
        self.machine.cycle()
        self.machine.cycle()
