library(rtweet)
library(dplyr)

tweet <- search_tweets("#vacina", n = 100, 
                          include_rts = FALSE)
tweet<-read_twitter_csv('/home/thiago/Documentos/MATB10-TOPICOS-EM-BANCO-DE-DADOS-NPL/100 tweet/tweet.csv')

rtweet::save_as_csv(tweet,'tweet.csv',prepend_ids = FALSE)
