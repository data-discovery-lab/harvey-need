library(tidytext)
library(ggplot2)
library(dplyr)
library(magrittr) #Used for %>%
library(tm)
library(topicmodels)

data("AssociatedPress")
a  <-Corpus(DirSource("/home/jstuve/GitProj/harvey-need/topic-modeling/text/"), readerControl = list(language="lat")) #specifies the exact folder where my text file(s) is for analysis with tm.
summary(a)  #check what went in

a <- tm_map(a, removeNumbers)
a <- tm_map(a, removePunctuation)
a <- tm_map(a, tolower)
a <- tm_map(a, removeWords, stopwords("english")) # this stopword file is at C:\Users\[username]\Documents\R\win-library\2.13\tm\stopwords
a <- tm_map(a, stemDocument, language = "english")
TFM <-DocumentTermMatrix(a) 
TFM <- removeSparseTerms(adtm, 0.75)


# set a seed so that the output of the model is predictable
ap_lda <- LDA(TFM, k = 2, control = list(seed = 1234))
ap_lda
 
ap_topics <- tidy(ap_lda, matrix = "beta")
ap_topics

ap_top_terms <- ap_topics %>%
  group_by(topic) %>%
  top_n(10, beta) %>%
  ungroup() %>%
  arrange(topic, -beta)

ap_top_terms %>%
  mutate(term = reorder(term, beta)) %>%
  ggplot(aes(term, beta, fill = factor(topic))) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~ topic, scales = "free") +
  coord_flip()

