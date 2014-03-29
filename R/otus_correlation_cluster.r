library(gplots)

otus = read.csv('../preprocessed/otus.csv', row.name=1)

cor_otus <- as.dist(1-cor(t(otus)))
h_cluster <- hclust(cor_otus)

X11()
#png("myplot.png")
plot(h_cluster)

savePlot("out.jpg", type="jpeg")
#dev.off()




message("Press Return To Continue")
invisible(readLines("stdin", n=1))

groups = cutree(h_cluster, k=10)
x<-cbind(otus, groups)


for (i in 1:10) {
    df = subset(x, groups==i)
    print(row.names(df))
    print("----------")
    df$groups <- NULL
    if (nrow(df) > 1) {
        tmp_cor <- as.dist(1-cor(t(df)))
        tmp_cluster <- hclust(tmp_cor)
        plot(tmp_cluster)

        savePlot(paste(i, ".jpg", sep=""), type="jpeg")

        message("Press Return To Continue")
        invisible(readLines("stdin", n=1))
    }
}

#for testing
#sort(cor(t(otus))[,'OTU_53'])
