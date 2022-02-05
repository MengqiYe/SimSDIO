# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/12/22
"""

from stm import DataTransferModeMachine


class TestDataTransferModeMachine:
    def setup(self):
        self.machine = DataTransferModeMachine()
        print()

    def test_CMD3(self):
        for i in range(10):
            self.machine.CMD3()
            print(f"Machine state : {self.machine.current_state.name}")

    def test_CMD7_at_stand_by(self):
        self.machine.current_state = self.machine.stand_by
        for i in range(10):
            self.machine.CMD7()
            print(f"Machine state : {self.machine.current_state.name}")

    def test_CMD7_at_disconnect(self):
        self.machine.current_state = self.machine.disconnect
        for i in range(10):
            self.machine.CMD7()
            print(f"Machine state : {self.machine.current_state.name}")


