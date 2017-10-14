library(stringr)
#fileIn is the input file, which contains the raw data.
fileIn<-file("/Users/yangkui/Desktop/2017_08_30_stream.txt",open = "r")

#fileOut is the output file, which contains the data after parsing.
#it contains d
fileOut<-file("/Users/yangkui/Desktop/out_30.csv",open = "w")

while(TRUE){
  lineOfFile=readLines(fileIn,n=1)
  if(length(lineOfFile)==0){
    break
  }else{
  text_start<-20
  text_end<-regexpr("<", lineOfFile)
  text=substr(lineOfFile,text_start,text_end-1)
  
  date_index<-regexpr("Aug ", lineOfFile)
  date_start<-date_index[1]
  date_end<-date_start+23
  date<-substr(lineOfFile,date_start,date_end)
  final_data<-data.frame(text,date)
  
  write.table(final_data,file = fileOut,sep = ",",append = TRUE,row.names = FALSE,col.names = FALSE)
  #write.table(final_data,file = fileOut,append = TRUE)
  
  }
}
close(fileIn)
close(fileOut)
