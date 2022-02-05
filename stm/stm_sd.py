# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Mengqi Ye on 2021/12/21
"""
from statemachine import StateMachine, State


class SDIOMachine(StateMachine):
    "A SDIO machine"

    power_on = State('power_on', initial=True)
    wait_for_cmd8 = State('wait_for_cmd8')
    response_for_cmd8 = State('response_for_cmd8')
    no_response_for_cmd8 = State('no_response_for_cmd8')
    wait_for_cmd8_response = State('wait_for_cmd8_response')

    fit_sd_2_0 = State('fit_sd_2_0')
    not_fit_sd_2_0 = State('not_fit_sd_2_0')

    CMD00 = power_on.to(wait_for_cmd8)
    CMD08 = wait_for_cmd8.to(wait_for_cmd8_response)

    CardResponse = wait_for_cmd8_response.to(fit_sd_2_0)
    NoCardResponse = wait_for_cmd8_response.to()


class DataTransferModeMachine(StateMachine):
    "SDIO data transfer mode machine"

    # power_on = State('power_on', initial=True)

    inactive = State('inactive', initial=True)

    # Card Identification Mode
    # idle = State('idle')
    # ready = State('ready')
    # identification = State('identification')

    # Data Transfer Mode
    stand_by = State('stand_by')
    transfer = State('transfer')
    sending_data = State('sending_data')
    receive_data = State('receive_data')
    programming = State('programming')
    disconnect = State('disconnect')


    CMD3 = inactive.to(stand_by) | stand_by.to(stand_by)
    CMD4 = stand_by.to(stand_by)
    CMD6 = transfer.to(sending_data)
    CMD7 = sending_data.to(stand_by) \
           | stand_by.to(transfer) \
           | transfer.to(stand_by) \
           | programming.to(disconnect) \
           | disconnect.to(programming)

    # Send Interface Condition Command, SEND_IF_CONT
    CMD8 = inactive.to(stand_by)
    # Stop command
    CMD12 = sending_data.to(transfer)

    # Block Read Operation
    CMD17 = transfer.to(sending_data)
    # Multiple Block Read Operation
    CMD18 = transfer.to(sending_data)
    # Block Write Operation
    CMD24 = transfer.to(receive_data)
    # Multiple Block Write Operation
    CMD25 = transfer.to(receive_data)
    CMD26 = transfer.to(receive_data)
    # CSR Register Programming Operation
    CMD27 = transfer.to(receive_data)
    CMD28 = transfer.to(programming)
    CMD29 = transfer.to(programming)
    # Send write protection staten
    CMD30 = transfer.to(sending_data)

    CMD38 = transfer.to(programming)

    # Execute lock/unlock command
    CMD42 = transfer.to(receive_data)


    # Execute common command under write mode
    CMD56 = transfer.to(receive_data)
    OP_DONE = disconnect.to(stand_by)


