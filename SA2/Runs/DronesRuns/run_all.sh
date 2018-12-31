#---------------------------------------
#--- initS1
maude -no-banner -no-wrap < initS1.maude > initS1.txt 
maude -no-banner -no-wrap < initS1Events.maude > initS1Events.txt 
maude -no-banner -no-wrap < initS1EventsX.maude > initS1EventsX.txt 
./run_loctarget.sh initS1Events.txt initS1EventsEnv.txt initS1EventsBot.txt data_trajectory.csv
./run_energy.sh initS1EventsX.txt initS1EventsXEnv.txt initS1EventsXBot.txt data_energy.csv
Rscript --vanilla trajectory_3d.R  data_trajectory.csv
mv Rplots.pdf drone_initS1_trajectory.pdf
Rscript --vanilla energy_3d.R  data_energy.csv
mv Rplots.pdf drone_initS1_energy.pdf
#---------------------------------------
#--- initS1locsf
maude -no-banner -no-wrap < initS1locsf.maude > initS1locsf.txt 
maude -no-banner -no-wrap < initS1locsfEvents.maude > initS1locsfEvents.txt 
maude -no-banner -no-wrap < initS1locsfEventsX.maude > initS1locsfEventsX.txt 
./run_loctarget.sh initS1locsfEvents.txt initS1locsfEventsEnv.txt initS1locsfEventsBot.txt data_trajectory.csv
./run_energy.sh initS1locsfEventsX.txt initS1locsfEventsXEnv.txt initS1locsfEventsXBot.txt data_energy.csv
Rscript --vanilla trajectory_3d.R  data_trajectory.csv
mv Rplots.pdf drone_initS1locsf_trajectory.pdf
Rscript --vanilla energy_3d.R  data_energy.csv
mv Rplots.pdf drone_initS1locsf_energy.pdf
#---------------------------------------
#--- initS1locsf2
maude -no-banner -no-wrap < initS1locsf2.maude > initS1locsf2.txt 
maude -no-banner -no-wrap < initS1locsf2Events.maude > initS1locsf2Events.txt 
maude -no-banner -no-wrap < initS1locsf2EventsX.maude > initS1locsf2EventsX.txt 
./run_loctarget.sh initS1locsf2Events.txt initS1locsf2EventsEnv.txt initS1locsf2EventsBot.txt data_trajectory.csv
./run_energy.sh initS1locsf2EventsX.txt initS1locsf2EventsXEnv.txt initS1locsf2EventsXBot.txt data_energy.csv
Rscript --vanilla trajectory_3d.R  data_trajectory.csv
mv Rplots.pdf drone_initS1locsf2_trajectory.pdf
Rscript --vanilla energy_3d.R  data_energy.csv
mv Rplots.pdf drone_initS1locsf2_energy.pdf
#---------------------------------------
#--- initS1locsf3
maude -no-banner -no-wrap < initS1locsf3.maude > initS1locsf3.txt 
maude -no-banner -no-wrap < initS1locsf3Events.maude > initS1locsf3Events.txt 
maude -no-banner -no-wrap < initS1locsf3EventsX.maude > initS1locsf3EventsX.txt 
./run_loctarget.sh initS1locsf3Events.txt initS1locsf3EventsEnv.txt initS1locsf3EventsBot.txt data_trajectory.csv
./run_energy.sh initS1locsf3EventsX.txt initS1locsf3EventsXEnv.txt initS1locsf3EventsXBot.txt data_energy.csv
Rscript --vanilla trajectory_3d.R  data_trajectory.csv
mv Rplots.pdf drone_initS1locsf3_trajectory.pdf
Rscript --vanilla energy_3d.R  data_energy.csv
mv Rplots.pdf drone_initS1locsf3_energy.pdf
#---------------------------------------
#--- initS1gotoaf
maude -no-banner -no-wrap < initS1gotoaf.maude > initS1gotoaf.txt 
maude -no-banner -no-wrap < initS1gotoafEvents.maude > initS1gotoafEvents.txt 
maude -no-banner -no-wrap < initS1gotoafEventsX.maude > initS1gotoafEventsX.txt 
./run_loctarget.sh initS1gotoafEvents.txt initS1gotoafEventsEnv.txt initS1gotoafEventsBot.txt data_trajectory.csv
./run_energy.sh initS1gotoafEventsX.txt initS1gotoafEventsXEnv.txt initS1gotoafEventsXBot.txt data_energy.csv
Rscript --vanilla trajectory_3d.R  data_trajectory.csv
mv Rplots.pdf drone_initS1gotoaf_trajectory.pdf
Rscript --vanilla energy_3d.R  data_energy.csv
mv Rplots.pdf drone_initS1gotoaf_energy.pdf
#---------------------------------------
#--- initS1gotoaf2
maude -no-banner -no-wrap < initS1gotoaf2.maude > initS1gotoaf2.txt 
maude -no-banner -no-wrap < initS1gotoaf2Events.maude > initS1gotoaf2Events.txt 
maude -no-banner -no-wrap < initS1gotoaf2EventsX.maude > initS1gotoaf2EventsX.txt 
./run_loctarget.sh initS1gotoaf2Events.txt initS1gotoaf2EventsEnv.txt initS1gotoaf2EventsBot.txt data_trajectory.csv
./run_energy.sh initS1gotoaf2EventsX.txt initS1gotoaf2EventsXEnv.txt initS1gotoaf2EventsXBot.txt data_energy.csv
Rscript --vanilla trajectory_3d.R  data_trajectory.csv
mv Rplots.pdf drone_initS1gotoaf2_trajectory.pdf
Rscript --vanilla energy_3d.R  data_energy.csv
mv Rplots.pdf drone_initS1gotoaf2_energy.pdf
#---------------------------------------
#--- initS1gotoaf3
maude -no-banner -no-wrap < initS1gotoaf3.maude > initS1gotoaf3.txt 
maude -no-banner -no-wrap < initS1gotoaf3Events.maude > initS1gotoaf3Events.txt 
maude -no-banner -no-wrap < initS1gotoaf3EventsX.maude > initS1gotoaf3EventsX.txt 
./run_loctarget.sh initS1gotoaf3Events.txt initS1gotoaf3EventsEnv.txt initS1gotoaf3EventsBot.txt data_trajectory.csv
./run_energy.sh initS1gotoaf3EventsX.txt initS1gotoaf3EventsXEnv.txt initS1gotoaf3EventsXBot.txt data_energy.csv
Rscript --vanilla trajectory_3d.R  data_trajectory.csv
mv Rplots.pdf drone_initS1gotoaf3_trajectory.pdf
Rscript --vanilla energy_3d.R  data_energy.csv
mv Rplots.pdf drone_initS1gotoaf3_energy.pdf
#----------------------------------------
rm tmp
rm data_trajectory.csv 
rm data_energy.csv
