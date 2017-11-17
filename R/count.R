 setwd("/Users/yangkui/Desktop/R/")
library(wordcloud2)
library(SnowballC)
library(stringr)
library(ggplot2)
library(tidytext)
library(dplyr)
library(stringr)

process_files<-function(fileName){
  #set working directory
  setwd("/Users/yangkui/Desktop/Input_hurricane/needs_harvey/")
  print(fileName)
  #read tweet into dataframe
  tweets_raw = read.csv(fileName,sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
  tweets=na.omit(tweets_raw)
  colnames(tweets)<-c("tweet","time")
  tweets<-tweets[order(tweets[,2]),]
  
  #function for clean tweet, remove unrelated symbols.
  # cleanTweet = function(tweets) {
  #   replace_reg = "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"
  #   unnest_reg = "([^A-Za-z_\\d#@']|'(?![A-Za-z_\\d#@]))"
  #   
  #   tweets = tweets %>% 
  #     mutate(text = str_replace_all(tweet, replace_reg, ""))
  #   
  #   tweets$tweet = tweets$text #update tweet cols after cleaning it.
  #   tweets<-tweets[,1:2] #drop unnecessory cols.
  #   
  #   #remove the duplicated one.
  #   tweets<-data.frame(unique(tweets[,1:2]))
  #   colnames(tweets)<-c("tweet","time")
  #   #remove all the non-character.
  #   tweets<- tweets %>% 
  #     mutate(text=str_replace_all(tweet, "[^[:alpha:]]", " "))
  #   tweets$tweet = tweets$text
  #   tweets<-tweets[,1:2]
  #   #remove sigle character.
  #   tweets<- tweets %>% 
  #     mutate(text=gsub("\\W*\\b\\w\\b\\W*", " ", tweet))
  #   tweets$tweet = tweets$text
  #   tweets<-tweets[,1:2]
  #   #remove space
  #   tweets<- tweets %>% 
  #     mutate(text=str_replace_all(tweet, "[[:blank:]{1,}]", " "))
  #   tweets$tweet = tweets$text
  #   tweets<-tweets[,1:2]
  #   
  #   return(tweets)
  # }
  # 
  # tweets = cleanTweet(tweets)
  ##########################
  
  split_into_time_block = function(x){
    if (grepl("[Aug|Sep]\\s+\\d{2}\\s+0[0|1|2|3]",x)){
      label<-1
    } else if (grepl("[Aug|Sep]\\s+\\d{2}\\s+0[4|5|6|7]",x)){
      label<-2
    } else if (grepl("[Aug|Sep]\\s+\\d{2}\\s+0[8|9]|Aug\\s+\\d{2}\\s+1[0|1]:",x)) {
      label<-3
    } else if (grepl("[Aug|Sep]\\s+\\d{2}\\s+1[2|3|4|5]:",x)) {
      label<-4
    } else if (grepl("[Aug|Sep]\\s+\\d{2}\\s+1[6|7|8|9]:",x)) {
      label<-5
    }else {
      label<-6
    }
    return(label)
  }
  tweets$label<-unlist(lapply(tweets$time,split_into_time_block))
  
  date_v<-str_extract(fileName,"\\d{2}_\\d{2}")
  for (i in 1:6){
    count_df<-data.frame(period=paste(date_v,i,sep = "_"),count=sum(tweets$label==i),rate=sum(tweets$label==i)/(4*3600))
    write.table(count_df,file = "/Users/yangkui/Desktop/Input_hurricane/count_needs_harvey.csv",sep = "|",append = TRUE,row.names = FALSE,col.names = FALSE)
    print(count_df)
  }
  #close(fileOut)
  return(0)
}
setwd("/Users/yangkui/Desktop/Input_hurricane/needs_harvey/")
processJob<-lapply(dir(),process_files)


