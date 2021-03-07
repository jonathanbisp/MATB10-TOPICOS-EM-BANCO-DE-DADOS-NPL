library(rtweet)
library(dplyr)

tweet <- search_tweets("#vacina", n = 100, 
                          include_rts = FALSE)
write_as_csv(tweet,'tweet.csv')

