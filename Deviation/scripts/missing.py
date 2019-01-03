#! /usr/bin/env python


import subprocess


deviate = '/usr/local/bin/deviate'

protocols = [
    'protocol_initS1.txt',
    'protocol_initS1_no_local_order.txt',
]

for p in protocols:
    cmd = [deviate, '-g', './configuration.cfg', '-m', '../SA1/Notes/BotTeamRuns2/initS1Obs1EventsEnv.txt', '../SA1/Notes/BotTeamRuns2/{0}'.format(p)]
    print(cmd)
    subprocess.call(cmd)
    cmd = [deviate, '-g', './configuration.cfg', '-fv', '../SA1/Notes/BotTeamRuns2/initS1Obs1EventsEnv.txt', '../SA1/Notes/BotTeamRuns2/{0}'.format(p)]
    print(cmd)
    subprocess.call(cmd)
