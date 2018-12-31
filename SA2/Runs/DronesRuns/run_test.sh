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
