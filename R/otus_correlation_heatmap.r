library(gplots)

otus_data <- read.csv('../preprocessed/otus.csv', row.name=1)

cormatrix <- cor(t(otus_data))

X11()
heatmap.2(cormatrix, col=redgreen(50), trace="none")

savePlot('heatmap.jpg', type='jpeg')

message("Press Return To Continue")
invisible(readLines("stdin", n=1))
