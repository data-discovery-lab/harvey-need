# Topic Modeling
---
This is a simple method on creating Topic Model plots using **topicmodels** library in R.

## Text Format

Simple .txt files with line separated data entries.

**Example TXT Format:**
```
how do you ask guy what you   
are without sounding weird or desperate need boy help pls null 
teezyrex go put some clothes on https co hhgw koplj null 
cbs powerful and moving show of  unity during peace march and rally in  charlottesville  ripheatherheyer  cbsla  https co ncxke  oyf null 
nyc nyanimalrescue nycscr rdr nyc amsterdogrescue lganimalrescue lipitstop getabull heartrescueinc https co ci ch null
```

## Compiling

Compile *topic_model_demo.R* using RStudio with text files located in the **text/** folder. Be sure to change file location in **line 9**.

## Output

RStudio will output a graph with *k* topics. The value of *k* can be change in **line 28**.