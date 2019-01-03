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
]


for (log, protocol) in args:
    print(log, protocol)
    retcode = subprocess.call([deviate, '-f', 'logs/{0}.txt'.format(log), 'logs/{0}.txt'.format(protocol)])
    print('retcode = {0}'.format(retcode))
