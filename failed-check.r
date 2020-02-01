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

subset_failed <- function(x, chroots=seq_len(ncol(df)-1)) {
  x.chrt <- x[, 2:ncol(x), drop=FALSE]
  x.fail <- x.chrt[, chroots, drop=FALSE]
  x.succ <- x.chrt[, setdiff(names(x.chrt), names(x.fail)), drop=FALSE]
  x.fail <- apply(x.fail, 2, function(x) grepl("failed", x))
  x.succ <- apply(x.succ, 2, function(x) grepl("succeeded|forked", x))
  subset(x, apply(cbind(x.fail, x.succ), 1, all))
}

df.3 <- subset_failed(df, 3)
fails <- sapply(strsplit(df.3[,4], " "), "[", 1)

pkg_list <- character(0)
for (i in seq_along(fails)) {
  message("Package ", i, "/", length(fails))
  URL <- paste0(URL.BACK, "/fedora-rawhide-x86_64/0", fails[i], "-", df.3[i, 1])
  res <- httr::GET(URL)
  if (res$status_code == 200) {
    res <- httr::GET(paste0(URL, "/builder-live.log.gz"))
    content <- strsplit(httr::content(res), "\n")[[1]]
    #pkgs <- grep("No matching package to install", content, value=TRUE)
    #pkg_list <- c(pkg_list, sapply(strsplit(pkgs, "'"), "[", 2))
    if (any(grepl("Error: Rank mismatch", content)))
      pkg_list <- c(pkg_list, df.3[i, 1])
  }
}
pkgs <- sapply(strsplit(unlist(pkg_list), " "), "[", 1)
pkgs <- pkgs[!duplicated(pkgs)]
