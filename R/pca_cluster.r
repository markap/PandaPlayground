library(gplots)

otus = read.csv('../preprocessed/otus.csv', row.name=1)

X11()


outs_3 = t(otus[,c("X1.3", "X2.3", "X3.3", "X4.3", "X5.3", "X6.3", "X7.3", "X8.3", "X9.3")])

outs_3 = outs_3[,c("OTU_56", "OTU_87", "OTU_24", "OTU_137", "OTU_76", "OTU_91", "OTU_16", "OTU_3", "OTU_21")]


df <- as.data.frame(scale(outs_3))
#df$OTU_38 <- NULL
#df$OTU_440 <- NULL
pca_data = prcomp(df)

biplot(pca_data)


message("Press Return To Continue")
invisible(readLines("stdin", n=1))
