setwd("C:/Users/ishaan/Documents/drdo")
dat<-read.csv("8byteSimpleExhaustive.csv")
library(ggplot2)
ggplot(aes(x=number,y=time),data=dat)+geom_point(fill=I('black'),color=I('black'),shape=25)+geom_smooth(method='lm',color='blue')+geom_jitter(alpha=1/20)+
  xlab("Key Number out of 256(8 bit)")+ylab("Time taken in seconds for search")
dat<-read.csv("4byteSimpleExhaustive.csv")
ggplot(aes(x=number,y=time),data=dat)+geom_point(fill=I('black'),color=I('black'),shape=25)+geom_smooth(method='lm',color='green')+geom_jitter(alpha=1/20)+
  xlab("Key Number out of 16(4 bit)")+ylab("Time taken in seconds for search")
 