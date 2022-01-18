#!/usr/bin/env python3
import requests
from time import sleep

#https://developers.whatsonchain.com/#get-address-info
#GET https://api.whatsonchain.com/v1/bsv/main/address/1Hxc4EaHr5AcKo1BzYcuvSTvgs6KffRJxu/balance
#Moneybutton 1DJb6GneEqTvXsBdX3VSnLCRq4ENGNk2YT
#VoltID 1D6Rpk1CHgBt9BA6Qpw8fV2nncKzdyxLxW
#HandCash 1BEMCbBZdnV4cGyuVYLKsvHMKFTvmPZPqP
#RelayX 1DZ3PAfuSMK91PejbnKVmmoDUTmmmmTR2A

#address = "1D6Rpk1CHgBt9BA6Qpw8fV2nncKzdyxLxW"
#address = "1DJb6GneEqTvXsBdX3VSnLCRq4ENGNk2YT"
address = "1DZ3PAfuSMK91PejbnKVmmoDUTmmmmTR2A"
#address = "1BEMCbBZdnV4cGyuVYLKsvHMKFTvmPZPqP"

while True: 

    response = requests.get(
        'https://api.whatsonchain.com/v1/bsv/main/address/' + address + '/balance'
    )
    resp_json = response.json()
    print(resp_json)
    #sleep for half second. WhatsonChain rate limit is 3 requests/second
    sleep(.5)