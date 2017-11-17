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

#set working directory
setwd("/Users/yangkui/Desktop/")

preProcessing = FALSE
tweets_raw = read.csv("/Users/yangkui/Desktop/nouns_harvey/08_27.csv",sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
tweets=na.omit(tweets_raw)
colnames(tweets)<-c("tweet","time")
tweets<-tweets[order(tweets[,2]),]
##########################
#remove the duplicated one.
tweets<-data.frame(unique(tweets[,1:2]))
colnames(tweets)<-c("tweet","time")
#remove all the non-character.
#remove space

###########################
additionalStopWords=c("harveyflood","hurricaneharveyrelief","rn","fwfj","aharveymitchellen","aharveymitchell","de","la","lo","null","harvei","harvey","houston","hurricaneharvy","hurricane","flood","hurricane","hurricaneharvey","houstonflood","tx","flooding","hurricaneharvery","hurricaineharvey","harveyrescue","realdonaldtrump","texasflood","pl","people","ppl","texa","storm","trump","day","texan","disaster","prayforhouston","katrina","street","harveystorm","hurricanharvey","lot","texas","don","rt","catastrophic","night","houstonchron","easy","fema","thousand","bc","coast","folk","american","cnn","abc","guy","harveyrelief","houstonflooding","alt","real","mexico","retweet","twitter")
additionalStopWords_df <- data_frame(word = additionalStopWords,lexicon="custom")
custom_stop_words = stop_words
custom_stop_words <- bind_rows(custom_stop_words, additionalStopWords_df)

words = tweets %>%
  unnest_tokens(word, tweet) %>%
  anti_join(custom_stop_words)  %>%
  mutate(word = wordStem(word))

count(words, word, sort = TRUE) 

#which pair should we count in this case?
#Count the number of times each pair of items appear together within a 
#group defined by "feature." For example, this could count the number 
#of times two words appear within documents).
# word_pairs <- words %>%   
productList<-c("help","water","fruit","batteries","solar charger","pet food", "food","gloves","fan","trash","bags","diapers","Hygiene","first aid","flashligh","repellent","medicine","wipes","tape","bottled water","paper")
filter(word == 'avoid' ) %>% 
  pairwise_count(word, productList, sort = TRUE, upper = FALSE)  %>% 
      filter(n >=3)

set.seed(1234)
edgeColor = ifelse(preProcessing, "darkred", "cyan4")

word_pairs %>%
  graph_from_data_frame() %>%
  ggraph(layout = "fr") +
  geom_edge_link(aes(edge_alpha = n, edge_width = n), edge_colour = edgeColor) +
  geom_node_point(size = 4) +
  geom_node_text(aes(label = name), repel = TRUE, 
                 point.padding = unit(0.2, "lines"),size=6)+
  theme_void()+
  theme(legend.text=element_text(size=16))
