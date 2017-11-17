
library(dplyr)
library(stringr)
setwd("/Users/yangkui/Desktop/RA/")
tax_mention<-str_extract_all(str,"[[:punct]]\\s{0,1}\\w{1,}?[effective tax rates|effective tax rate|etr|ETR|]\\s\\w{1,}?[is|are]{0,1}\\s\\w{1,}?]\\d%")
library(readstata13)


sa_sp<-read.dta13("/Users/yangkui/Desktop/RA/sa_sp500.dta.txt")
contents<-sa_sp$body
length(contents)

contents<-data.frame(contents,1:17056)
colnames(contents)<-c("text","lineNumber")

contents<-contents %>% 
  mutate(tax_mention=str_trim(str_extract_all(text, "\\s?(\\w+\\s+){1,}(?:effective tax rate|effective tax rates|ETR|etr)\\s+(?:is|are|will be)\\s{1,}\\w+\\d+%")[[1]]),text)
