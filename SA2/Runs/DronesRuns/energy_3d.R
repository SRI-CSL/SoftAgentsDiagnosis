rm(list = ls())

library(ggplot2)
library(ggrepel)
library(dplyr)
library(tidyr)

args <- commandArgs(TRUE)
#df<-read.csv("~/data_energy.csv", header=T)
df<-read.csv(args[1], header=T)
df

df2 <- df # %>% unite(xy, c(x,y), sep=',', remove=F) %>% group_by(bot, xy) %>% mutate(times = paste(t,collapse=',')) %>% ungroup %>% select(bot,x,y,times) %>% distinct
#print(tbl_df(df2), n=80)

ggplot(data=df2, aes(x=t,y=energy))+
  #xlim(0,70)+
  #ylim(0,100)+
  coord_fixed(ratio=1)+
  labs(title="Bot Energy", x="time", y="energy")+
  #geom_text_repel(aes(color=bot, label=t), segment.size = 0.1, point.padding = 0.01, size=2)+
  #geom_text(data=df2 %>% filter(bot==0) %>% mutate(y=y+0.1), aes(color=bot, label=times), size=2)+
  #geom_text(data=df2 %>% filter(bot==1) %>% mutate(y=y-0.1), aes(color=bot, label=times), size=2)+
  geom_line(aes(color=bot))+
  geom_point(aes(color=bot))+
  facet_grid(. ~ bot)+
  scale_x_continuous(breaks = round(seq(0,70,by=10)))+
  #scale_y_continuous(breaks = round(seq(0,max(df2$energy),by=5)))+
  scale_y_continuous(breaks = round(seq(0,100,by=5)))+
  theme(legend.position = "none", panel.grid.minor.x = element_blank(), panel.grid.minor.y = element_blank())
 
  #scale_x_continuous(breaks = round(seq(min(df2$x),max(df2$x),by=1)))+
  #scale_y_continuous(breaks = round(seq(min(df2$y),max(df2$y),by=1)))+
  #theme(legend.position = "none", panel.grid.minor.x = element_blank(), panel.grid.minor.y = element_blank())

dev.copy(png,'myplot.png')
dev.off()