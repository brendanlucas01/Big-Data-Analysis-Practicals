require(tidyverse)
require(lubridate)
require(igraph)
require(tidytext)
library(tm)
require(wordcloud)
require(ggplot2)

#retrieving tweets
path <- paste("/home/hdoop/Documents/Exp 11", "/TweetsElonMusk.csv", sep ="")
elontweets <- read.csv(path)
textdata<-elontweets$tweet


twitter_document<- Corpus(VectorSource(textdata))
twitter_document<-tm_map(twitter_document, content_transformer(tolower))
twitter_document<-tm_map(twitter_document,removeNumbers)
twitter_document<-tm_map(twitter_document, removeWords, stopwords("english"))
twitter_document<-tm_map(twitter_document,removePunctuation)
twitter_document<-tm_map(twitter_document,stripWhitespace)


#analysis
data<-TermDocumentMatrix(twitter_document)
m<-as.matrix(data)
v<-sort(rowSums(m),decreasing = T)
d<-data.frame(frequency=v)
d<-data.frame(word=names(v),frequency=v)


#barplot
barplot(d[1:10,]$freq,las=2, names.arg=d[1:10,]$word,
        col="Red", main="Top Ten Most Frequent words",
        ylab="word Frequencies")


#display wordcloud
set.seed(1234)
wordcloud(words=d$word, freq=d$frequency, min.freq = 1, max.words = 80,
          random.order=FALSE, rot.per=0.40, colors=brewer.pal(8,"Dark2"))


