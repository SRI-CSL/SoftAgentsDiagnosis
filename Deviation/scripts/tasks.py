#! /usr/bin/env python


import subprocess


deviate = '/usr/local/bin/deviate'

environment_logs = (
    'initS1EventsEnv',
    'initS1Obs1EventsEnv',
    'initS1aObs4-2EventsEnv',
    'initS1aensfmEventsEnv',
    'initS1alocsf1EventsEnv',
    'initS1amvaf1EventsEnv',
    'initS1amvaf1xEventsEnv',
    'initS1locsf1EventsEnv',
    'initS2ensf0EventsEnv',
    'initS2ensf1EventsEnv',
    'initS2locsf0xEventsEnv',
    'initS2locsf1EventsEnv',
    'initS2mvaf1EventsEnv',
)


bot_logs =  (
    'initS1EventsBot',
    'initS1Obs1EventsBot',
    'initS1aObs4-2EventsBot',
    'initS1aensfmEventsBot',
    'initS1alocsf1EventsBot',
    'initS1amvaf1EventsBot',
    'initS1amvaf1xEventsBot',
    'initS1locsf1EventsBot',
    'initS2ensf0EventsBot',
    'initS2ensf1EventsBot',
    'initS2locsf0xEventsBot',
    'initS2locsf1EventsBot',
    'initS2mvaf1EventsBot',
)


protocols = (
    'protocol0',
    'protocol1',
    'protocol2',
    'protocol3',
)


unsatisfiable = ''
unsat_pairs = []
gen_theory = False

count = 0
for protocol in protocols:
    for log in environment_logs:
        print(f"Env: {count} {log} {protocol}")
        logpath = 'logs/{0}.txt'.format(log)
        protocolpath = 'logs/{0}.txt'.format(protocol)
        if gen_theory:
            retcode = subprocess.call([deviate, '-t', 'env{0}.ys'.format(count), logpath, protocolpath])
        else:
            retcode = subprocess.call([deviate, logpath, protocolpath])
        if retcode == 1:
            unsatisfiable += '{0} {1} {2}\n'.format(deviate, logpath, protocolpath)
            unsat_pairs.append((log, protocol))
        count += 1


for protocol in protocols:
    for log in bot_logs:
        print(f"Bot: {count} {log} {protocol}")
        logpath = 'logs/{0}.txt'.format(log)
        protocolpath = 'logs/{0}.txt'.format(protocol)
        if gen_theory:
            retcode = subprocess.call([deviate, '-t', 'bot{0}.ys'.format(count), logpath, protocolpath])
        else:
            retcode = subprocess.call([deviate, logpath, protocolpath])

        if retcode == 1:
            unsatisfiable += '{0} {1} {2}\n'.format(deviate, logpath, protocolpath)
            unsat_pairs.append((log, protocol))
        count +=  1


print(unsatisfiable)
for (log, protocol) in unsat_pairs:
    print(f"[ {log}, {protocol}]")
