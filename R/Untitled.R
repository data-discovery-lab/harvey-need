library(stringr)

fileIn<-file("/Users/yangkui/Desktop/2017_08_26_stream_sample.txt",open = "r")
fileOut<-file("/Users/yangkui/Desktop/out.csv",open = "w")
lineOfFile=readLines(fileIn,n=1)

while(str_count(string=lineOfFile,pattern = "[:alnum:]")!=0){
  
  text_start<-20
  text_end<-regexpr("<", lineOfFile)
  text=substr(lineOfFile,text_start,text_end-1)
  
  date_index<-regexpr("Aug ", lineOfFile)
  date_start<-date_index[1]
  date_end<-date_start+23
  date<-substr(lineOfFile,date_start,date_end)
  final_data<-c(text,date)
  
  write.table(final_data,file = fileOut,append = TRUE)
  
  lineOfFile=readLines(fileIn,n=1)   #Read another line
}
close(fileIn)
close(fileOut)

