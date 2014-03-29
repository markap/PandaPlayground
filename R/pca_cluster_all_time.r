library(gplots)

otus = read.csv('../preprocessed/otus.csv', row.name=1)

X11()


outs_3 = t(otus)

outs_3 = outs_3[,c("OTU_56", "OTU_87", "OTU_24", "OTU_137", "OTU_76", "OTU_91", "OTU_16", "OTU_3", "OTU_21")]


df <- as.data.frame(scale(outs_3))
#df$OTU_38 <- NULL
#df$OTU_440 <- NULL
pca_data = prcomp(df)

biplot(pca_data)


message("Press Return To Continue")
invisible(readLines("stdin", n=1))
