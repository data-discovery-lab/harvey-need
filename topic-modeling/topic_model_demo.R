library(tidytext)
library(ggplot2)
library(dplyr)
library(magrittr) #Used for %>%
library(tm)
library(topicmodels)

#Stopword File
stopwords <- read.csv("/home/jstuve/GitProj/harvey-need/topic-modeling/stopwords.csv", header = FALSE)
stopwords <- as.character(stopwords$V1)
stopwords <- c(stopwords, stopwords("english"))

#Read tweet file

a  <-Corpus(DirSource("/home/jstuve/GitProj/harvey-need/topic-modeling/text/"), readerControl = list(language="lat")) #Directory for text file analytics

#Clean the data
a <- tm_map(a, removeNumbers)
a <- tm_map(a, removePunctuation)
a <- tm_map(a, tolower)
a <- tm_map(a, removeWords, stopwords)
a <- tm_map(a, stemDocument, language = "english")
TFM <-DocumentTermMatrix(a)   #Create a matrix for LDA functino
TFM <- removeSparseTerms(TFM, 0.75)  #Reduce the matrix size for term that are below .75


# set a seed so that the output of the model is predictable
ap_lda <- LDA(TFM, k = 3, control = list(seed = 1234))
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

