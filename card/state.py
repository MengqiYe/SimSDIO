# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/12/21
"""
from enum import Enum


class CardState(Enum):
    INACTIVE           = 0,
    IDLE               = 1,
    READY              = 2,
    IDENTIFICATION     = 3,
    STANDBY            = 4,
    TRANSFER           = 5,
    SENDING_DATA       = 6,
    RECEIVE_DATA       = 7,
    PROGRAMMING        = 8,
    DISCONNECT         = 9,


class CardWorkMode(Enum):
    INACTIVE=0,
    CARD_IDENTIFICATION = 1,
    DATA_TRANSFER = 2,
