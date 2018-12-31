#!/bin/bash

#---------------------------------------
echo initS1
maude -no-banner -no-wrap < initS1.maude > initS1.txt

maude -no-banner -no-wrap < initS1Events.maude > initS1Events.txt
./run_loctreat.sh initS1Events.txt initS1EventsEnv.txt initS1EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1_trajectory.pdf

maude -no-banner -no-wrap < initS1EventsX.maude > initS1EventsX.txt
./run_energy.sh initS1EventsX.txt initS1EventsXEnv.txt initS1EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1_energy.pdf

maude -no-banner -no-wrap < initS1EDevsL.maude > initS1EDevs.txt

#---------------------------------------
echo initS1locsf1
maude -no-banner -no-wrap < initS1locsf1.maude > initS1locsf1.txt

maude -no-banner -no-wrap < initS1locsf1Events.maude > initS1locsf1Events.txt
./run_loctreat.sh initS1locsf1Events.txt initS1locsf1EventsEnv.txt initS1locsf1EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1locsf1_trajectory.pdf

maude -no-banner -no-wrap < initS1locsf1EventsX.maude > initS1locsf1EventsX.txt
./run_energy.sh initS1locsf1EventsX.txt initS1locsf1EventsXEnv.txt initS1locsf1EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1locsf1_energy.pdf

maude -no-banner -no-wrap < initS1locsf1EDevsL.maude > initS1locsf1EDevs.txt

#---------------------------------------
echo initS1Obs1
maude -no-banner -no-wrap < initS1Obs1.maude > initS1Obs1.txt

maude -no-banner -no-wrap < initS1Obs1Events.maude > initS1Obs1Events.txt
./run_loctreat.sh initS1Obs1Events.txt initS1Obs1EventsEnv.txt initS1Obs1EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1Obs1_trajectory.pdf

maude -no-banner -no-wrap < initS1Obs1EventsX.maude > initS1Obs1EventsX.txt
./run_energy.sh initS1Obs1EventsX.txt initS1Obs1EventsXEnv.txt initS1Obs1EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1Obs1_energy.pdf

maude -no-banner -no-wrap < initS1Obs1EDevsL.maude > initS1Obs1EDevs.txt

#---------------------------------------
echo initS1a
maude -no-banner -no-wrap < initS1a.maude > initS1a.txt

maude -no-banner -no-wrap < initS1aEvents.maude > initS1aEvents.txt
./run_loctreat.sh initS1aEvents.txt initS1aEventsEnv.txt initS1aEventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1a_trajectory.pdf

maude -no-banner -no-wrap < initS1aEventsX.maude > initS1aEventsX.txt
./run_energy.sh initS1aEventsX.txt initS1aEventsXEnv.txt initS1aEventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1a_energy.pdf

maude -no-banner -no-wrap < initS1aEDevsL.maude > initS1aEDevs.txt

#---------------------------------------
echo initS1alocsf1x
maude -no-banner -no-wrap < initS1alocsf1x.maude > initS1alocsf1x.txt

maude -no-banner -no-wrap < initS1alocsf1xEvents.maude > initS1alocsf1xEvents.txt
./run_loctreat.sh initS1alocsf1xEvents.txt initS1alocsf1xEventsEnv.txt initS1alocsf1xEventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1alocsf1x_trajectory.pdf

maude -no-banner -no-wrap < initS1alocsf1xEventsX.maude > initS1alocsf1xEventsX.txt
./run_energy.sh initS1alocsf1xEventsX.txt initS1alocsf1xEventsXEnv.txt initS1alocsf1xEventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1alocsf1x_energy.pdf

maude -no-banner -no-wrap < initS1alocsf1xEDevsL.maude > initS1alocsf1xEDevs.txt

#---------------------------------------
echo initS1aObs4-2
maude -no-banner -no-wrap < initS1aObs4-2.maude > initS1aObs4-2.txt

maude -no-banner -no-wrap < initS1aObs4-2Events.maude > initS1aObs4-2Events.txt
./run_loctreat.sh initS1aObs4-2Events.txt initS1aObs4-2EventsEnv.txt initS1aObs4-2EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1aObs4-2_trajectory.pdf

maude -no-banner -no-wrap < initS1aObs4-2EventsX.maude > initS1aObs4-2EventsX.txt
./run_energy.sh initS1aObs4-2EventsX.txt initS1aObs4-2EventsXEnv.txt initS1aObs4-2EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1aObs4-2_energy.pdf

maude -no-banner -no-wrap < initS1aObs4-2EDevsL.maude > initS1aObs4-2EDevs.txt

#---------------------------------------
echo initS1aensfm1
maude -no-banner -no-wrap < initS1aensfm1.maude > initS1aensfm1.txt

maude -no-banner -no-wrap < initS1aensfm1Events.maude > initS1aensfm1Events.txt
./run_loctreat.sh initS1aensfm1Events.txt initS1aensfm1EventsEnv.txt initS1aensfm1EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1aensfm1_trajectory.pdf

maude -no-banner -no-wrap < initS1aensfm1EventsX.maude > initS1aensfm1EventsX.txt
./run_energy.sh initS1aensfm1EventsX.txt initS1aensfm1EventsXEnv.txt initS1aensfm1EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1aensfm1_energy.pdf

maude -no-banner -no-wrap < initS1aensfm1EDevsL.maude > initS1aensfm1EDevs.txt

#---------------------------------------
echo initS1amvaf1
maude -no-banner -no-wrap < initS1amvaf1.maude > initS1amvaf1.txt

maude -no-banner -no-wrap < initS1amvaf1Events.maude > initS1amvaf1Events.txt
./run_loctreat.sh initS1amvaf1Events.txt initS1amvaf1EventsEnv.txt initS1amvaf1EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1amvaf1_trajectory.pdf

maude -no-banner -no-wrap < initS1amvaf1EventsX.maude > initS1amvaf1EventsX.txt
./run_energy.sh initS1amvaf1EventsX.txt initS1amvaf1EventsXEnv.txt initS1amvaf1EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1amvaf1_energy.pdf

maude -no-banner -no-wrap < initS1amvaf1EDevsL.maude > initS1amvaf1EDevs.txt

#---------------------------------------
echo initS1amvaf1x
maude -no-banner -no-wrap < initS1amvaf1x.maude > initS1amvaf1x.txt

maude -no-banner -no-wrap < initS1amvaf1xEvents.maude > initS1amvaf1xEvents.txt
./run_loctreat.sh initS1amvaf1xEvents.txt initS1amvaf1xEventsEnv.txt initS1amvaf1xEventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS1amvaf1x_trajectory.pdf

maude -no-banner -no-wrap < initS1amvaf1xEventsX.maude > initS1amvaf1xEventsX.txt
./run_energy.sh initS1amvaf1xEventsX.txt initS1amvaf1xEventsXEnv.txt initS1amvaf1xEventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS1amvaf1x_energy.pdf

maude -no-banner -no-wrap < initS1amvaf1xEDevsL.maude > initS1amvaf1xEDevs.txt

#---------------------------------------
echo initS2
maude -no-banner -no-wrap < initS2.maude > initS2.txt

maude -no-banner -no-wrap < initS2Events.maude > initS2Events.txt
./run_loctreat.sh initS2Events.txt initS2EventsEnv.txt initS2EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS2_trajectory.pdf

maude -no-banner -no-wrap < initS2EventsX.maude > initS2EventsX.txt
./run_energy.sh initS2EventsX.txt initS2EventsXEnv.txt initS2EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS2_energy.pdf

maude -no-banner -no-wrap < initS2EDevsL.maude > initS2EDevs.txt

#---------------------------------------
echo initS2ensf0
maude -no-banner -no-wrap < initS2ensf0.maude > initS2ensf0.txt

maude -no-banner -no-wrap < initS2ensf0Events.maude > initS2ensf0Events.txt
./run_loctreat.sh initS2ensf0Events.txt initS2ensf0EventsEnv.txt initS2ensf0EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS2ensf0_trajectory.pdf

maude -no-banner -no-wrap < initS2ensf0EventsX.maude > initS2ensf0EventsX.txt
./run_energy.sh initS2ensf0EventsX.txt initS2ensf0EventsXEnv.txt initS2ensf0EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS2ensf0_energy.pdf

maude -no-banner -no-wrap < initS2ensf0EDevsL.maude > initS2ensf0EDevs.txt

#---------------------------------------
echo initS2ensf1
maude -no-banner -no-wrap < initS2ensf1.maude > initS2ensf1.txt

maude -no-banner -no-wrap < initS2ensf1Events.maude > initS2ensf1Events.txt
./run_loctreat.sh initS2ensf1Events.txt initS2ensf1EventsEnv.txt initS2ensf1EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS2ensf1_trajectory.pdf

maude -no-banner -no-wrap < initS2ensf1EventsX.maude > initS2ensf1EventsX.txt
./run_energy.sh initS2ensf1EventsX.txt initS2ensf1EventsXEnv.txt initS2ensf1EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS2ensf1_energy.pdf

maude -no-banner -no-wrap < initS2ensf1EDevsL.maude > initS2ensf1EDevs.txt

#---------------------------------------
echo initS2locsf0x
maude -no-banner -no-wrap < initS2locsf0x.maude > initS2locsf0x.txt

maude -no-banner -no-wrap < initS2locsf0xEvents.maude > initS2locsf0xEvents.txt
./run_loctreat.sh initS2locsf0xEvents.txt initS2locsf0xEventsEnv.txt initS2locsf0xEventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS2locsf0x_trajectory.pdf

maude -no-banner -no-wrap < initS2locsf0xEventsX.maude > initS2locsf0xEventsX.txt
./run_energy.sh initS2locsf0xEventsX.txt initS2locsf0xEventsXEnv.txt initS2locsf0xEventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS2locsf0x_energy.pdf

maude -no-banner -no-wrap < initS2locsf0xEDevsL.maude > initS2locsf0xEDevs.txt

#---------------------------------------
echo initS2locsf1
maude -no-banner -no-wrap < initS2locsf1.maude > initS2locsf1.txt

maude -no-banner -no-wrap < initS2locsf1Events.maude > initS2locsf1Events.txt
./run_loctreat.sh initS2locsf1Events.txt initS2locsf1EventsEnv.txt initS2locsf1EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS2locsf1_trajectory.pdf

maude -no-banner -no-wrap < initS2locsf1EventsX.maude > initS2locsf1EventsX.txt
./run_energy.sh initS2locsf1EventsX.txt initS2locsf1EventsXEnv.txt initS2locsf1EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS2locsf1_energy.pdf

maude -no-banner -no-wrap < initS2locsf1EDevsL.maude > initS2locsf1EDevs.txt

#---------------------------------------
echo initS2mvaf1
maude -no-banner -no-wrap < initS2mvaf1.maude > initS2mvaf1.txt

maude -no-banner -no-wrap < initS2mvaf1Events.maude > initS2mvaf1Events.txt
./run_loctreat.sh initS2mvaf1Events.txt initS2mvaf1EventsEnv.txt initS2mvaf1EventsBot.txt data_trajectory.csv
Rscript --vanilla trajectory.R  data_trajectory.csv
mv Rplots.pdf botteam_initS2mvaf1_trajectory.pdf

maude -no-banner -no-wrap < initS2mvaf1EventsX.maude > initS2mvaf1EventsX.txt
./run_energy.sh initS2mvaf1EventsX.txt initS2mvaf1EventsXEnv.txt initS2mvaf1EventsXBot.txt data_energy.csv
Rscript --vanilla energy.R  data_energy.csv
mv Rplots.pdf botteam_initS2mvaf1_energy.pdf

maude -no-banner -no-wrap < initS2mvaf1EDevsL.maude > initS2mvaf1EDevs.txt

#----------------------------------------
rm tmp
rm data_trajectory.csv 
rm data_energy.csv
