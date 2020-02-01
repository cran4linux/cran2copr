source("config.r")
source("common.r")
options(stringsAsFactors=FALSE)

URL.COPR <- paste("https://copr.fedorainfracloud.org/coprs",
                  copr_call("whoami"), getOption("copr.repo"), sep="/")
URL.BACK <- paste("https://copr-be.cloud.fedoraproject.org/results",
                  copr_call("whoami"), getOption("copr.repo"), sep="/")

df <- XML::readHTMLTable(readLines(URL.BACK))[[1]]
chroots <- sort(sub("/$", "", subset(df, grepl("^fedora", Name))$Name))

df <- XML::readHTMLTable(readLines(paste(URL.COPR, "monitor", "detailed", sep="/")))[[1]]
colnames(df) <- c("Package", chroots)
df <- na.omit(df)
latest <- unique(unname(sapply(strsplit(unlist(df[,-1]), " "), "[", 1)))

df.builds <- XML::readHTMLTable(readLines(paste(URL.COPR, "builds", sep="/")))[[1]]
df.rm <- subset(df.builds, !`Build ID` %in% latest)

for (i in seq_len(nrow(df.rm))) {
  copr_call("delete-build", df.rm[i, 1])
  message("  Build ", df.rm[i, 1], " for package ", df.rm[i, 2], " removed (", i, "/", nrow(df.rm), ")")
}
