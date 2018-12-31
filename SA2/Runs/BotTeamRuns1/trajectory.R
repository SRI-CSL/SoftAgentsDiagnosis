rm(list = ls())
#options(warn=-1)

library(ggplot2)
library(ggrepel)
library(dplyr, warn.conflicts = FALSE)
library(tidyr)

#df<-data.frame(bot=c(0,1,0),
#               x=c(3,4,3),
#               y=c(4,5,4),
#               t=c("9","9","10c"))
#df<-read.csv("~/data.csv", header=T)
#df
args <- commandArgs(TRUE)
#df<-read.csv("~/data_trajectory.csv", header=T)
df<-read.csv(args[1], header=T)
#df

df2 <- unique(df) %>% unite(xy, c(x,y), sep=',', remove=F) %>% group_by(bot, xy) %>% mutate(times = paste(t,collapse=',')) %>% ungroup %>% select(bot,x,y,times) %>% distinct
#print(tbl_df(df2), n=80)

ggplot(data=df2, aes(x=x,y=y))+
  #xlim(0,6)+
  #ylim(-0.1,5)+
  coord_cartesian(xlim = c(0,6), ylim = c(-0.1,5))+
  labs(title="Bot Trajectory", x="x", y="y")+
  #geom_text_repel(aes(color=bot, label=t), segment.size = 0.1, point.padding = 0.01, size=2)+
  geom_text(data=df2 %>% filter(bot==0) %>% mutate(y=y+0.1), aes(color=bot, label=times), size=2)+
  geom_text(data=df2 %>% filter(bot==1) %>% mutate(y=y-0.1), aes(color=bot, label=times), size=2)+
  geom_text(data=df2 %>% filter(bot==2) %>% mutate(y=y-0.2), color="red", aes(color=bot, label=times), size=2)+
  geom_text(data=df2 %>% filter(bot==3) %>% mutate(y=y-0.2), color="purple", aes(color=bot, label=times), size=2)+
  geom_point()+
  #scale_x_continuous(breaks = round(seq(min(df2$x),max(df2$x),by=1)))+
  #scale_y_continuous(breaks = round(seq(min(df2$y),max(df2$y),by=1)))+
  scale_x_continuous(breaks = round(seq(0,6,by=1)))+
  scale_y_continuous(breaks = round(seq(0,5,by=1)))+
  theme(legend.position = "none", panel.grid.minor.x = element_blank(), panel.grid.minor.y = element_blank())
