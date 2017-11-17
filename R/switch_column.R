
library(stringr)

library(stringr)

process_files<-function(fileName){
  #set working directory
  setwd("/Users/yangkui/Desktop/nouns_irma/")
  print(fileName)
  #read tweet into dataframe
  tweets_raw<- read.csv(fileName,sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
 
 tweets<-data.frame(tweets_raw$V2,tweets_raw$V1)
  
 setwd("/Users/yangkui/Desktop/switch_irma//")
 write.table(tweets,file = fileName,sep = "|",append = TRUE,row.names = FALSE,col.names = FALSE)
 
  return(0)
}
setwd("/Users/yangkui/Desktop/nouns_irma/")
processJob<-lapply(dir(),process_files)


