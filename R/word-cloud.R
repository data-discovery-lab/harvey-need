library(wordcloud2)
library(SnowballC)
library(stringr)
library(widyr)
library(ggplot2)
library(igraph)
library(ggraph)
library(wordcloud2)
library(SnowballC)
library(stringr)
library(dplyr)
library(tidytext)
library(ggplot2)
library(igraph)
library(ggraph)

library(tidytext)
setwd("/Users/yangkui/Desktop/")

preProcessing = FALSE
#without pre-processing
if (preProcessing == FALSE) {
  tweets_raw = read.csv("/Users/yangkui/Desktop/nouns_total_harvey.csv",sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
  tweets=na.omit(tweets_raw)
  colnames(tweets)<-c("time","tweet")
  sortedData<-tweets[order(tweets[,2]),]
  tweets=sortedData
}

# cleanTweet = function(tweets) {
#   replace_reg = "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"
#   unnest_reg = "([^A-Za-z_\\d#@']|'(?![A-Za-z_\\d#@]))"
#   
#   tweets = tweets %>% 
#     mutate(text = str_replace_all(tweet, replace_reg, ""))
#   
#   tweets$tweet = tweets$text
#   #tweets$text = NULL
#   tweets<-tweets[,1:2]
#   
#   return(tweets)
# }
# 
# tweets = cleanTweet(tweets)
# 
# ##########################
# #remove the duplicated one.
# tweets<-data.frame(unique(tweets[,1:2]))
# colnames(tweets)<-c("tweet","time")
# #remove all the non-character.
# tweets<- tweets %>% 
#   mutate(text=str_replace_all(tweet, "[^[:alpha:]]", " "))
# tweets$tweet = tweets$text
# tweets<-tweets[,1:2]
# #remove sigle character.
# tweets<- tweets %>% 
#   mutate(text=gsub("\\W*\\b\\w\\b\\W*", " ", tweet))
# tweets$tweet = tweets$text
# tweets<-tweets[,1:2]
# #remove space
# tweets<- tweets %>% 
#   mutate(text=str_replace_all(tweet, "[[:blank:]{1,}]", " "))
# tweets$tweet = tweets$text
# tweets<-tweets[,1:2]
# ###########################

additionalStopWords=c("harveyflood","hurricaneharveyrelief","rn","fwfj","aharveymitchellen","aharveymitchell","de","la","lo","null","harvei","harvey","houston","hurricaneharvy","hurricane","flood","hurricane","hurricaneharvey","houstonflood","tx","flooding","hurricaneharvery","hurricaineharvey","harveyrescue","realdonaldtrump","texasflood","pl","people","ppl","texa","storm","trump","day","texan","disaster","prayforhouston","katrina","street","harveystorm","hurricanharvey","lot","texas","don","rt","catastrophic","night","houstonchron","easy","fema","thousand","bc","coast","folk","american","cnn","abc","guy","harveyrelief","houstonflooding","alt","real","mexico","retweet","twitter")
additionalStopWords_df <- data_frame(word = additionalStopWords,lexicon="custom")
custom_stop_words = stop_words
custom_stop_words <- bind_rows(custom_stop_words, additionalStopWords_df)


words = tweets %>%
  unnest_tokens(word, tweet) %>%
  anti_join(custom_stop_words, by = c("word" = "word"))


#str(words)

## visualize negative flu-shot words
wordFreq = count(words, word, sort = TRUE) %>%
  filter(n >= 10) 

colnames(wordFreq) = c("word", "freq")

wordcloud2(data = wordFreq, size =1,gridSize = 5,fontWeight = 50)

