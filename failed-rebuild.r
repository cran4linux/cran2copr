source("config.r")
source("common.r")
options(stringsAsFactors=FALSE)
options(copr.bflags="")

URL.COPR <- paste("https://copr.fedorainfracloud.org/coprs",
                  copr_call("whoami"), getOption("copr.repo"), sep="/")
URL.BACK <- paste("https://copr-be.cloud.fedoraproject.org/results",
                  copr_call("whoami"), getOption("copr.repo"), sep="/")

df <- XML::readHTMLTable(readLines(URL.BACK))[[1]]
chroots <- sort(sub("/$", "", subset(df, grepl("^fedora", Name))$Name))

df <- XML::readHTMLTable(readLines(paste(URL.COPR, "monitor", "detailed", sep="/")))[[1]]
colnames(df) <- c("Package", chroots)
df <- na.omit(df)

subset_failed <- function(x, chroots=seq_len(ncol(df)-1)) {
  x.chrt <- x[, 2:ncol(x), drop=FALSE]
  x.fail <- x.chrt[, chroots, drop=FALSE]
  x.succ <- x.chrt[, setdiff(names(x.chrt), names(x.fail)), drop=FALSE]
  x.fail <- apply(x.fail, 2, function(x) grepl("failed", x))
  x.succ <- apply(x.succ, 2, function(x) grepl("succeeded|forked", x))
  subset(x, apply(cbind(x.fail, x.succ), 1, all))
}

df.rel <- df[,-ncol(df)]

for (i in list(1, 2, 1:2)) {
  pkgs <- subset_failed(df.rel, i)$Package
  sapply(pkgs, build_pkg, chroots=chroots[i])
}
