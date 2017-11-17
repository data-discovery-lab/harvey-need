library(wordcloud2)
library(SnowballC)
library(stringr)
library(ggplot2)
library(tidytext)
library(dplyr)
library(stringr)

#set working directory
setwd("/home/long/TTU-SOURCES/harvey-need")

preProcessing = FALSE
#without pre-processing
if (preProcessing == FALSE) {
  tweets_raw = read.csv("data/global-need/2017_08_17_stream.txt",sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
  tweets=na.omit(tweets_raw)
  colnames(tweets)<-c("time","tweet")
  sortedData<-tweets[order(tweets[,2]),]
  tweets=sortedData
}

cleanTweet = function(tweets) {
  replace_reg = "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"
  unnest_reg = "([^A-Za-z_\\d#@']|'(?![A-Za-z_\\d#@]))"
  
  tweets = tweets %>% 
    mutate(text = str_replace_all(tweet, replace_reg, ""))
  
  tweets$tweet = tweets$text
  #tweets$text = NULL
  tweets<-tweets[,1:2]
  
  return(tweets)
}

tweets = cleanTweet(tweets)
##########################
#remove the duplicated one.
tweets<-data.frame(unique(tweets[,1:2]))
colnames(tweets)<-c("time","tweet")
#remove all the non-character.
tweets<- tweets %>% 
  mutate(text=str_replace_all(tweet, "[^[:alpha:]]", " "))
tweets$tweet = tweets$text
tweets<-tweets[,1:2]
#remove sigle character.
tweets<- tweets %>% 
  mutate(text=gsub("\\W*\\b\\w\\b\\W*", " ", tweet))
tweets$tweet = tweets$text
tweets<-tweets[,1:2]
#remove space
tweets<- tweets %>% 
  mutate(text=str_replace_all(tweet, "[[:blank:]{1,}]", " "))
tweets$tweet = tweets$text
tweets<-tweets[,1:2]
###########################

additionalStopWords=c("en","de","la","lo","null", "tx", "harvei", "harvey", "hurricane", "storm", "nyc", "hurricaneharvey", "texas",
                      "texa", "hurricanharvey", "hurricaineharvey", "houston", "hurricaneharvery", "houstonflood", "houstonstrong", "harveyflood", 
                      "harveyrelief", "harveyrescue", "news", "lol", "gonna", "don", "dad", "flood", "flooding", "flooded")
additionalStopWords_df <- data_frame(lexicon="custom", word = additionalStopWords)

custom_stop_words = stop_words
custom_stop_words <- bind_rows(custom_stop_words, additionalStopWords_df)

words = tweets %>%
  unnest_tokens(word, tweet) %>%
  anti_join(custom_stop_words, by = c("word" = "word")) 
 # mutate(word = wordStem(word))

wordFreq=count(words, word, sort = TRUE) 
colnames(wordFreq) = c("word", "freq")

wordFreq = wordFreq %>%
  filter(freq >=100) %>%
  mutate(word = reorder(word, freq))


fillColor = ifelse(preProcessing, "darkred", "cyan4")

graphics.off()

ggplot(data = wordFreq, aes(word, freq)) +
  geom_col(fill = fillColor) +
  coord_flip() +
  labs(x = "Word \n", y = "\n Count", title = "Frequent words in text") +
  geom_text(aes(label = freq), hjust = 1.2, colour = "white", fontface = "bold", size=10) +
  theme(plot.title = element_text(size = 24, hjust = 0.5),
        axis.title.x = element_text(face = "bold", colour = "black", size = 24),
        axis.title.y = element_text(face = "bold", colour = "black", size = 24),
        text=element_text(size=24))