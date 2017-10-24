library(wordcloud2)
library(SnowballC)
library(stringr)
library(ggplot2)
library(tidytext)
library(dplyr)
library(stringr)
library(coreNLP)
library(rJava)

#set working directory
setwd("/Users/yangkui/Desktop/")

preProcessing = FALSE
#without pre-processing
if (preProcessing == FALSE) {
  tweets_raw = read.csv("/Users/yangkui/Desktop/26out.csv",sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
  tweets=na.omit(tweets_raw)
  colnames(tweets)<-c("tweet","time")
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
colnames(tweets)<-c("tweet","time")
#remove all the non-character.
tweets<- tweets %>% 
  mutate(text=str_replace_all(tweet, "[^[:alpha:]]", " "))
tweets$tweet = tweets$text
tweets<-tweets[,1:2]
#remove sigle character.
tweets<- tweets %>% 
  mutate(text=gsub("\\W*\\b\\w{1,2}\\b\\W*|null", " ", tweet))
tweets$tweet = tweets$text
tweets<-tweets[,1:2]
#remove space
tweets<- tweets %>% 
  mutate(text=str_replace_all(tweet, "[[:blank:]{1,}]", " "))
tweets$tweet = tweets$text
tweets<-tweets[,1:2]
###########################
extract_noun<-function(tweet){
    annotated_str<-annotateString(tweet)
    tok_str<-getToken(annotated_str)
    tok_df<-data.frame(tok_str$lemma,tok_str$POS)
    noun_df<-tok_df %>% filter((tok_str.POS=="NN")| (tok_str.POS=="NNS"))
    tweet_noun<-paste(noun_df$tok_str.lemma,sep = " ", collapse = " ")
    return(tweet_noun)
}
#extract noun from string
tweets$noun<-lapply(tweets[,1], extract_noun)
#remove NA
tweets$noun[tweets$noun==""]<-"NA"
tweets <- tweets[-which(tweets$noun == "NA"), ]

#additionalStopWords=c("en","de","la","lo","null")
#additionalStopWords_df <- data_frame(lexicon="custom", word = additionalStopWords)

#custom_stop_words = stop_words
#custom_stop_words <- bind_rows(custom_stop_words, additionalStopWords_df)

#words = tweets %>%
 # unnest_tokens(word, tweet) %>%
  #anti_join(custom_stop_words, by = c("word" = "word"))  %>%
  #mutate(word = wordStem(word))
