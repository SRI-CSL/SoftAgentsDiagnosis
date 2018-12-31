rm(list = ls())

library(ggplot2)
library(ggrepel)
library(dplyr)
library(tidyr)

args <- commandArgs(TRUE)
#df<-read.csv("~/data_trajectory.csv", header=T)
df<-read.csv(args[1], header=T)
df

df2 <- unique(df) %>% unite(xy, c(x,y), sep=',', remove=F) %>% group_by(bot, xy) %>% mutate(times = paste(t,collapse=',')) %>% ungroup %>% select(bot,x,y,times) %>% distinct
print(tbl_df(df2), n=120)

ggplot(data=df2, aes(x=x,y=y))+
  #xlim(0,6)+
  #ylim(-0.1,5)+
  coord_cartesian(xlim = c(0,100), ylim = c(-0.1,100))+
  coord_fixed(ratio=1)+
  labs(title="Bot Trajectory", x="x", y="y")+
  #geom_text_repel(aes(color=bot, label=t), segment.size = 0.1, point.padding = 0.01, size=2)+
  #geom_text(data=df2 %>% filter(bot==0) %>% mutate(y=y+0.5,x=x-0.5), aes(color=bot, label=times), size=2)+
  geom_text_repel(data=df2 %>% filter(bot==0) %>% mutate(y=y-0.2), aes(color=bot, label=times), size=2)+
  #geom_text(data=df2 %>% filter(bot==1) %>% mutate(y=y-0.5,x=x+0.5), aes(color=bot, label=times), size=2)+
  geom_text_repel(data=df2 %>% filter(bot==1) %>% mutate(y=y-0.2), aes(color=bot, label=times), size=2)+
  geom_text(data=df2 %>% filter(bot==2) %>% mutate(y=y+1), color="red", aes(color=bot, label=times), size=2)+
  geom_text(data=df2 %>% filter(bot==3) %>% mutate(y=y+1), color="purple", aes(color=bot, label=times), size=2)+
  geom_point()+
  #scale_x_continuous(breaks = round(seq(min(df2$x),max(df2$x),by=1)))+
  #scale_y_continuous(breaks = round(seq(min(df2$y),max(df2$y),by=1)))+
  scale_x_continuous(breaks = round(seq(0,100,by=10)))+
  scale_y_continuous(breaks = round(seq(0,100,by=10)))+
  theme(legend.position = "none", panel.grid.minor.x = element_blank(), panel.grid.minor.y = element_blank())

dev.copy(png,'myplot.png')
dev.off()