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
    setwd("/Users/yangkui/Desktop/tweets/")
  
    print(fileName)
    #read tweet into dataframe
    tweets_raw = read.csv(fileName,sep = "|", stringsAsFactors = FALSE,header = FALSE,na.strings = c("","NA"))
    tweets=na.omit(tweets_raw)
    colnames(tweets)<-c("tweet","time")
    tweets<-tweets[order(tweets[,2]),]
  
  #function for clean tweet, remove unrelated symbols.
  cleanTweet = function(tweets) {
    replace_reg = "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"
    unnest_reg = "([^A-Za-z_\\d#@']|'(?![A-Za-z_\\d#@]))"
    
    tweets = tweets %>% 
      mutate(text = str_replace_all(tweet, replace_reg, ""))
    
    tweets$tweet = tweets$text #update tweet cols after cleaning it.
    tweets<-tweets[,1:2] #drop unnecessory cols.
    
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
      mutate(text=gsub("\\W*\\b\\w\\b\\W*", " ", tweet))
    tweets$tweet = tweets$text
    tweets<-tweets[,1:2]
    #remove space
    tweets<- tweets %>% 
      mutate(text=str_replace_all(tweet, "[[:blank:]{1,}]", " "))
    tweets$tweet = tweets$text
    tweets<-tweets[,1:2]
    
    return(tweets)
  }
  
  #clean tweets
  tweets = cleanTweet(tweets)
  
  extract_noun<-function(tweet){
      annotated_str<-annotateString(tweet)
      tok_str<-getToken(annotated_str)
      tok_df<-data.frame(tok_str$lemma,tok_str$POS)
      noun_df<-tok_df %>% filter((tok_str.POS=="NN")| (tok_str.POS=="NNS"))
      tweet_noun<-as.character(paste(noun_df$tok_str.lemma,sep = " ", collapse = " "))
      return(tweet_noun)
  }

  #extract noun from string
  tweets$noun<-unlist(lapply(tweets[,1], extract_noun))
 
  tweets$noun<-unlist(tweets$noun)
  
  tweets<-tweets[,2:3]
  
  #remove NA
  #tweets$noun[tweets$noun==""]<-"NA"
  #tweets1 <- tweets[-which(tweets$noun == "NA"), ]

  split_into_time_block = function(x){
    if (grepl("[Aug|Sep]\\s+\\d{2}\\s+0[0|1|2|3|4|5|6|7|8|9]|[Aug|Sep]\\s+\\d{2}\\s+1[0|1]",x)){
      label<-1
    } else {
      label<-2
    }
    return(label)
  }
  tweets$label<-unlist(lapply(tweets$time,split_into_time_block))
  
  setwd("/Users/yangkui/Desktop/out/")
  
  date_v<-str_extract(fileName,"\\d{2}_\\d{2}")
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
