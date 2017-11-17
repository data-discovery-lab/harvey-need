library(wordcloud2)
library(SnowballC)
library(stringr)
library(ggplot2)
library(tidytext)
library(dplyr)
library(stringr)
library(coreNLP)
library(rJava)

process_files<-function(fileName){
  #set working directory
  setwd("/Users/yangkui/Desktop/output/")
  print(fileName)
  #read tweet into dataframe
  tweets <- read.csv(fileName,sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
  colnames(tweets)<-c("time","tweet")
  tweets<-tweets[order(tweets[,2]),]
  
  
  
  setwd("/Users/yangkui/Desktop/wordFreq/")
  
  date_v<-str_extract(fileName,"\\d{2}_\\d{2}_\\d{1}")
  for (i in 1:2){
    fileOut<-sprintf("%s_%d.csv",date_v,i)
    df<-subset(tweets,label==i)
    df<-df[,1:2]
    print(fileOut)
    write.table(df,file = fileOut,sep = "|",append = TRUE,row.names = FALSE,col.names = FALSE)
  }
  
}

setwd("/Users/yangkui/Desktop/Test/")
processJob<-lapply(dir(),process_files)

# additionalStopWords=c("en","de","la","lo","null")
# additionalStopWords_df <- data_frame(lexicon="custom", word = additionalStopWords)
# 
# custom_stop_words = stop_words
# custom_stop_words <- bind_rows(custom_stop_words, additionalStopWords_df)
# 
# words = tweets %>%
#   unnest_tokens(word, tweet) %>%
#   anti_join(custom_stop_words, by = c("word" = "word"))  %>%
#   mutate(word = wordStem(word))
# 
# wordFreq=count(words, word, sort = TRUE) 
# colnames(wordFreq) = c("word", "freq")
# 
# wordFreq = wordFreq %>%
#   filter(freq >=2) %>%
#   mutate(word = reorder(word, freq))
# 
# fillColor = ifelse(preProcessing, "darkred", "cyan4")
# 
# ggplot(data = wordFreq, aes(word, freq)) + 
#   geom_col(fill = fillColor) + 
#   coord_flip() + 
#   labs(x = "Word \n", y = "\n Count", title = "Frequent words in text") +
#   geom_text(aes(label = freq), hjust = 1.2, colour = "white", fontface = "bold", size=10) + 
#   theme(plot.title = element_text(size = 24, hjust = 0.5), 
#         axis.title.x = element_text(face = "bold", colour = "black", size = 24),
#         axis.title.y = element_text(face = "bold", colour = "black", size = 24),
#         text=element_text(size=24))
