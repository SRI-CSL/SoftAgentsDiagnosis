#!/bin/bash

#---------------------------------------
echo initS1
./run_dev_task.sh initS1EventsEnv.txt protocol_initS1.txt configuration.cfg initS1Devs.txt

#---------------------------------------
echo initS1locsf1
./run_dev_task.sh initS1locsf1EventsEnv.txt protocol_initS1.txt configuration.cfg initS1locsf1Devs.txt

#---------------------------------------
echo initS1Obs1
./run_dev_task.sh initS1Obs1EventsEnv.txt protocol_initS1.txt configuration.cfg initS1Obs1Devs.txt

#---------------------------------------
echo initS1a
./run_dev_task.sh initS1aEventsEnv.txt protocol_initS1a.txt configuration.cfg initS1aDevs.txt

#---------------------------------------
echo initS1alocsf1x
./run_dev_task.sh initS1alocsf1xEventsEnv.txt protocol_initS1a.txt configuration.cfg initS1alocsf1xDevs.txt

#---------------------------------------
echo initS1aObs4-2
./run_dev_task.sh initS1aObs4-2EventsEnv.txt protocol_initS1a.txt configuration.cfg initS1aObs4-2Devs.txt

#---------------------------------------
echo initS1aensfm1
./run_dev_task.sh initS1aensfm1EventsEnv.txt protocol_initS1a.txt configuration.cfg initS1aensfm1Devs.txt

#---------------------------------------
echo initS1amvaf1
./run_dev_task.sh initS1amvaf1EventsEnv.txt protocol_initS1a.txt configuration.cfg initS1amvaf1Devs.txt

#---------------------------------------
echo initS1amvaf1x
./run_dev_task.sh initS1amvaf1xEventsEnv.txt protocol_initS1a.txt configuration.cfg initS1amvaf1xDevs.txt

#---------------------------------------
echo initS2
./run_dev_task.sh initS2EventsEnv.txt protocol_initS2.txt configuration.cfg initS2Devs.txt

#---------------------------------------
echo initS2ensf0
./run_dev_task.sh initS2ensf0EventsEnv.txt protocol_initS2.txt configuration.cfg initS2ensf0Devs.txt

#---------------------------------------
echo initS2ensf1
./run_dev_task.sh initS2ensf1EventsEnv.txt protocol_initS2.txt configuration.cfg initS2ensf1Devs.txt

#---------------------------------------
echo initS2locsf0x
./run_dev_task.sh initS2locsf0xEventsEnv.txt protocol_initS2.txt configuration.cfg initS2locsf0xDevs.txt

#---------------------------------------
echo initS2locsf1
./run_dev_task.sh initS2locsf1EventsEnv.txt protocol_initS2.txt configuration.cfg initS2locsf1Devs.txt

#---------------------------------------
echo initS2mvaf1
./run_dev_task.sh initS2mvaf1EventsEnv.txt protocol_initS2.txt configuration.cfg initS2mvaf1Devs.txt

#----------------------------------------
