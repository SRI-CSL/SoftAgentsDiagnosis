#! /usr/bin/env python

import subprocess


deviate = '/usr/local/bin/deviate'


args = [
    [ 'initS1aObs4-2EventsEnv', 'protocol0'],
    [ 'initS1aensfmEventsEnv', 'protocol0'],
    [ 'initS1alocsf1EventsEnv', 'protocol0'],
    [ 'initS1amvaf1EventsEnv', 'protocol0'],
    [ 'initS1amvaf1xEventsEnv', 'protocol0'],
    [ 'initS2ensf0EventsEnv', 'protocol0'],
    [ 'initS2ensf1EventsEnv', 'protocol0'],
    [ 'initS2locsf0xEventsEnv', 'protocol0'],
    [ 'initS2locsf1EventsEnv', 'protocol0'],
    [ 'initS2mvaf1EventsEnv', 'protocol0'],
    [ 'initS1EventsEnv', 'protocol1'],
    [ 'initS1Obs1EventsEnv', 'protocol1'],
    [ 'initS1aObs4-2EventsEnv', 'protocol1'],
    [ 'initS1aensfmEventsEnv', 'protocol1'],
    [ 'initS1alocsf1EventsEnv', 'protocol1'],
    [ 'initS1amvaf1EventsEnv', 'protocol1'],
    [ 'initS1amvaf1xEventsEnv', 'protocol1'],
    [ 'initS1locsf1EventsEnv', 'protocol1'],
    [ 'initS2ensf0EventsEnv', 'protocol1'],
    [ 'initS2ensf1EventsEnv', 'protocol1'],
    [ 'initS2locsf0xEventsEnv', 'protocol1'],
    [ 'initS2locsf1EventsEnv', 'protocol1'],
    [ 'initS2mvaf1EventsEnv', 'protocol1'],
    [ 'initS1EventsEnv', 'protocol2'],
    [ 'initS1Obs1EventsEnv', 'protocol2'],
    [ 'initS1aObs4-2EventsEnv', 'protocol2'],
    [ 'initS1aensfmEventsEnv', 'protocol2'],
    [ 'initS1alocsf1EventsEnv', 'protocol2'],
    [ 'initS1amvaf1EventsEnv', 'protocol2'],
    [ 'initS1amvaf1xEventsEnv', 'protocol2'],
    [ 'initS1locsf1EventsEnv', 'protocol2'],
    [ 'initS2ensf0EventsEnv', 'protocol2'],
    [ 'initS2ensf1EventsEnv', 'protocol2'],
    [ 'initS2locsf0xEventsEnv', 'protocol2'],
    [ 'initS2locsf1EventsEnv', 'protocol2'],
    [ 'initS2mvaf1EventsEnv', 'protocol2'],
    [ 'initS1EventsEnv', 'protocol3'],
    [ 'initS1Obs1EventsEnv', 'protocol3'],
    [ 'initS1aObs4-2EventsEnv', 'protocol3'],
    [ 'initS1aensfmEventsEnv', 'protocol3'],
    [ 'initS1alocsf1EventsEnv', 'protocol3'],
    [ 'initS1amvaf1EventsEnv', 'protocol3'],
    [ 'initS1amvaf1xEventsEnv', 'protocol3'],
    [ 'initS1locsf1EventsEnv', 'protocol3'],
    [ 'initS2ensf1EventsEnv', 'protocol3'],
    [ 'initS2locsf0xEventsEnv', 'protocol3'],
    [ 'initS2locsf1EventsEnv', 'protocol3'],
    [ 'initS2mvaf1EventsEnv', 'protocol3'],
    [ 'initS1aObs4-2EventsBot', 'protocol0'],
    [ 'initS1aensfmEventsBot', 'protocol0'],
    [ 'initS1alocsf1EventsBot', 'protocol0'],
    [ 'initS1amvaf1EventsBot', 'protocol0'],
    [ 'initS1amvaf1xEventsBot', 'protocol0'],
    [ 'initS2ensf0EventsBot', 'protocol0'],
    [ 'initS2ensf1EventsBot', 'protocol0'],
    [ 'initS2locsf0xEventsBot', 'protocol0'],
    [ 'initS2locsf1EventsBot', 'protocol0'],
    [ 'initS2mvaf1EventsBot', 'protocol0'],
    [ 'initS1EventsBot', 'protocol1'],
    [ 'initS1Obs1EventsBot', 'protocol1'],
    [ 'initS1aObs4-2EventsBot', 'protocol1'],
    [ 'initS1aensfmEventsBot', 'protocol1'],
    [ 'initS1alocsf1EventsBot', 'protocol1'],
    [ 'initS1amvaf1EventsBot', 'protocol1'],
    [ 'initS1amvaf1xEventsBot', 'protocol1'],
    [ 'initS1locsf1EventsBot', 'protocol1'],
    [ 'initS2ensf0EventsBot', 'protocol1'],
    [ 'initS2ensf1EventsBot', 'protocol1'],
    [ 'initS2locsf0xEventsBot', 'protocol1'],
    [ 'initS2locsf1EventsBot', 'protocol1'],
    [ 'initS2mvaf1EventsBot', 'protocol1'],
    [ 'initS1EventsBot', 'protocol2'],
    [ 'initS1Obs1EventsBot', 'protocol2'],
    [ 'initS1aObs4-2EventsBot', 'protocol2'],
    [ 'initS1aensfmEventsBot', 'protocol2'],
    [ 'initS1alocsf1EventsBot', 'protocol2'],
    [ 'initS1amvaf1EventsBot', 'protocol2'],
    [ 'initS1amvaf1xEventsBot', 'protocol2'],
    [ 'initS1locsf1EventsBot', 'protocol2'],
    [ 'initS2ensf0EventsBot', 'protocol2'],
    [ 'initS2ensf1EventsBot', 'protocol2'],
    [ 'initS2locsf0xEventsBot', 'protocol2'],
    [ 'initS2locsf1EventsBot', 'protocol2'],
    [ 'initS2mvaf1EventsBot', 'protocol2'],
    [ 'initS1EventsBot', 'protocol3'],
    [ 'initS1Obs1EventsBot', 'protocol3'],
    [ 'initS1aObs4-2EventsBot', 'protocol3'],
    [ 'initS1aensfmEventsBot', 'protocol3'],
    [ 'initS1alocsf1EventsBot', 'protocol3'],
    [ 'initS1amvaf1EventsBot', 'protocol3'],
    [ 'initS1amvaf1xEventsBot', 'protocol3'],
    [ 'initS1locsf1EventsBot', 'protocol3'],
    [ 'initS2ensf1EventsBot', 'protocol3'],
    [ 'initS2locsf0xEventsBot', 'protocol3'],
    [ 'initS2locsf1EventsBot', 'protocol3'],
    [ 'initS2mvaf1EventsBot', 'protocol3'],
]

for (log, protocol) in args:
    print(log, protocol)
    retcode = subprocess.call([deviate, '-u', f'logs/{log}.txt', f'logs/{protocol}.txt'])
    print(f'retcode = {retcode}')
    retcode = subprocess.call([deviate, '-i', f'logs/{log}.txt', f'logs/{protocol}.txt'])
    print(f'retcode = {retcode}')
    retcode = subprocess.call([deviate, '-f', f'logs/{log}.txt', f'logs/{protocol}.txt'])
    print(f'retcode = {retcode}')
