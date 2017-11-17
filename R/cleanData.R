library(wordcloud2)
library(SnowballC)
library(stringr)
library(ggplot2)
library(tidytext)
library(dplyr)
library(stringr)
library(stringr)
#fileIn is the input file, which contains the raw data.

fileIn<-file("/Users/yangkui/Desktop/newdata/2017_08_17_stream.txt",open = "r")
#fileOut is the output file, which contains the data after parsing.
#it contains d
fileOut<-file("/Users/yangkui/Desktop/08_17out.csv",open = "w")

while(TRUE){
  lineOfFile=readLines(fileIn,n=1)
  if(length(lineOfFile)==0){
      break
  }else{
      #extract text of a tweet
      text_start<-20
      text_end<-regexpr("<", lineOfFile)
      text<-substr(lineOfFile,text_start,text_end-1)
      text <- tolower(text)
      if (!grepl("harvey|hurricane|flood", text)){
        next
      }else{
        #extract date
        date_index<-regexpr("Aug 17", lineOfFile)
        date_start<-date_index[1]
        date_end<-date_start+23
      
        date<-substr(lineOfFile,date_start,date_end)
        final_data<-data.frame(text,date)
        tweets<-final_data
        colnames(tweets)<-c("tweet","time")
        #remove double quote (") and |
        tweets<- tweets %>% 
          mutate(tweet1=gsub('"|\\|', " ", tweet))
      
        tweets$tweet <- tweets$tweet1
        tweets<-tweets[,1:2]
        
        write.table(tweets,file = fileOut,sep = "<->",append = TRUE,row.names = FALSE,col.names = FALSE)
        #write.table(final_data,file = fileOut,append = TRUE)
      }
  }
}
close(fileIn)
close(fileOut)

