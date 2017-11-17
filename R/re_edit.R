library(wordcloud2)
library(SnowballC)
library(stringr)
library(ggplot2)
library(tidytext)
library(dplyr)
library(stringr)

#set working directory
setwd("/Users/yangkui/Desktop/")

preProcessing = FALSE
#without pre-processing
if (preProcessing == FALSE) {
  tweets_raw = read.csv("/Users/yangkui/Desktop/out_sample.csv",sep = "\n", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
  tweets=na.omit(tweets_raw)
  tweets$line<-1:nrow(tweets)
  colnames(tweets)<-c("tweet","line")
  #sortedData<-tweets[order(tweets[,2])]
 # tweets=sortedData
}

cleanTweet = function(tweets) {
  replace_reg = "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"
  unnest_reg = "([^A-Za-z_\\d#@']|'(?![A-Za-z_\\d#@]))"
  
  tweets = tweets %>% 
    mutate(text = str_replace_all(tweet, replace_reg, ""))
  
  tweets$tweet = tweets$text
  #tweets$text = NULL
  tweets<-tweets[,1:2]
  #tweets<-data.frame(tweets)
  
  return(tweets)
}

tweets = cleanTweet(tweets)
tweets<-data.frame(tweets)
##########################
#remove the duplicated one.
tweets<-data.frame(unique(tweets[,1:2]))
colnames(tweets)<-c("tweet","line")
#remove all the non-character.
tweets<- tweets %>% 
  #remove the non-character 
  mutate(text1=str_replace_all(tweet, "[^[:alpha:]]", " ")) %>%
  mutate(text2=gsub("\\W*\\b\\w\\b\\W*", " ", text1)) %>%
  mutate(text3=gsub("\\b.{1,2}\\b", " ", text2)) %>%
  mutate(text4=str_replace_all(text3, "[[:blank:]{2,}]", " ")) %>%
  mutate(text5=str_replace_all(text4,"\\s{2,}"," ")) %>%
  mutate(text6=gsub("[^[:alnum:]///' ]", "", text5))

tweets$tweet = tweets$text6
tweets<-tweets[,1:2]
#########################
additionalStopWords=c("en","de","la","lo","null","cdt","aug")
additionalStopWords_df <- data_frame(lexicon="custom", word = additionalStopWords)

custom_stop_words = stop_words
custom_stop_words <- bind_rows(custom_stop_words, additionalStopWords_df)

words = tweets %>%
  unnest_tokens(word, tweet) %>%
  anti_join(custom_stop_words, by = c("word" = "word"))  %>%
  mutate(word = wordStem(word))

wordFreq=count(words, word, sort = TRUE) 
colnames(wordFreq) = c("word", "freq")

wordFreq = wordFreq %>%
  filter(freq >=2) %>%
  mutate(word = reorder(word, freq))

fillColor = ifelse(preProcessing, "darkred", "cyan4")

ggplot(data = wordFreq, aes(word, freq)) + 
  geom_col(fill = fillColor) + 
  coord_flip() + 
  labs(x = "Word \n", y = "\n Count", title = "Frequent words in text") +
  geom_text(aes(label = freq), hjust = 1.2, colour = "white", fontface = "bold", size=10) + 
  theme(plot.title = element_text(size = 24, hjust = 0.5), 
        axis.title.x = element_text(face = "bold", colour = "black", size = 24),
        axis.title.y = element_text(face = "bold", colour = "black", size = 24),
        text=element_text(size=24))


##  ggplot(data = wordFreq, aes(word, freq), size=14) + 
##  geom_col(fill = fillColor) + 
##  coord_flip() + 
##  labs(x = "Word \n", y = "\n Count", title = "Frequent words in text") +
##  geom_text(aes(label = freq), hjust = 1.2, colour = "white", fontface = "bold") + 
##  theme(plot.title = element_text(size = 18, hjust = 0.5), 
##        axis.title.x = element_text(face = "bold", colour = "black", size = 18),
##        axis.title.y = element_text(face = "bold", colour = "black", size = 18))