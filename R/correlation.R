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
# 
# process_files<-function(fileName){
# 
#   print(fileName)
#   setwd("/Users/yangkui/Desktop/nouns_harvey/")
#   #read tweet into dataframe
#   tweets<- read.csv(fileName,sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
#   colnames(tweets)<-c("time","tweet")
#   tweets<- tweets %>% 
#     mutate(text= gsub("\\b[[:alpha:]]{1,2}\\b", " ", tweet))
#   tweets$tweet = tweets$text
#   tweets<-tweets[,1:2]
#   
#   tweets<- tweets %>% 
#     mutate(text= gsub("\\b\\s{2,}\\b", " ", tweet))
#   tweets$tweet = tweets$text
#   tweets<-tweets[,1:2]
#   
#   #set working directory
#   setwd("/Users/yangkui/Desktop/")
#   write.table(tweets,file = "/Users/yangkui/Desktop/nouns_total_harvey.csv",sep = "|",append = TRUE,row.names = FALSE,col.names = FALSE)
# 
#   return(0)
# }
# setwd("/Users/yangkui/Desktop/nouns_harvey/")
# processJob<-lapply(dir(),process_files)


  setwd("/Users/yangkui/Desktop/")
  #read tweet into dataframe
  fileName<-"nouns_total_harvey.csv"
  tweets<- read.csv(fileName,sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
  colnames(tweets)<-c("time","tweet")
  
  #prepare for the stopwords
  additionalStopWords<-c("harveyflood","hurricaneharveyrelief","rn","fwfj","aharveymitchellen","aharveymitchell","de","la","lo","null","harvei","harvey","houston","hurricaneharvy","hurricane","flood","hurricane","hurricaneharvey","houstonflood","tx","flooding","hurricaneharvery","hurricaineharvey","harveyrescue","realdonaldtrump","texasflood","pl","people","ppl","texa","storm","trump","day","texan","disaster","prayforhouston","katrina","street","harveystorm","hurricanharvey","lot","texas","don","rt","catastrophic","night","houstonchron","easy","fema","thousand","bc","coast","folk","american","cnn","abc","guy","harveyrelief","houstonflooding","alt","real","mexico","retweet","twitter")
  additionalStopWords_df <- data_frame(lexicon="custom", word = additionalStopWords)
  custom_stop_words <- stop_words
  custom_stop_words <- bind_rows(custom_stop_words, additionalStopWords_df)
  
  tweets1<-tweets %>% 
    mutate(section=row_number() %/% 40) %>%
    unnest_tokens(word, tweet) %>%
    anti_join(custom_stop_words, by = c("word" = "word")) %>%
    filter(!word %in% custom_stop_words$word) 
    # mutate(word = wordStem(word))

  word_pairs <- tweets1 %>%
    pairwise_count(word, section, sort = TRUE)

  word_cors <- tweets1 %>%
    group_by(word) %>%
    filter(n() >= 10) %>%
    pairwise_cor(word, section, sort = TRUE)
  
  set.seed(2016)

word_cors %>%
  filter(correlation >0.5) %>%
  filter(correlation <0.95) %>%
  graph_from_data_frame() %>%
  ggraph(layout = "fr") +
  geom_edge_link(aes(edge_alpha = correlation), show.legend = FALSE) +
  geom_node_point(color = "cyan4", size = 5) +
  geom_node_text(aes(label = name), repel = TRUE) +
  theme_void()
  
edgeColor<-"cyan4"
word_pairs %>%
  graph_from_data_frame() %>%
  ggraph(layout = "fr") +
  geom_edge_link(aes(edge_alpha = n, edge_width = n), edge_colour = edgeColor) +
  geom_node_point(size = 4) +
  geom_node_text(aes(label = name), repel = TRUE, 
                 point.padding = unit(0.2, "lines"),size=6)+
  theme_void()+
  theme(legend.text=element_text(size=16))
  
  
  