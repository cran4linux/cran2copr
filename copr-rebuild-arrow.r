#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

cmd.rq <- "dnf --releasever=CHROOT rq libarrow --queryformat '%{version}' -q"
cmd.gs <- "git show HEAD~NREV:specs/R-CRAN-arrow.spec"

chroots <- rev(getOption("copr.chroots"))
versions <- sapply(strsplit(chroots, "-"), "[", 2) |>
  sapply(function(x) system(sub("CHROOT", x, cmd.rq), intern=TRUE))

nrev <- 0
for (i in seq_along(versions)) while (TRUE) {
  remove_patch <- function(x)
    paste(head(unlist(strsplit(x, "[.]")), 2), collapse=".")

  spec <- system(sub("NREV", nrev, cmd.gs), intern=TRUE)
  ver <- strsplit(grep("Version", spec, value=TRUE), " +")[[1]][2]
  cmp <- compareVersion(remove_patch(ver), remove_patch(versions[i]))

  if (cmp > 0) {
    nrev <- nrev + 1
    next
  } else if (cmp == 0) {
    message("Building v", ver, " for libarrow-", versions[i], " in ", chroots[i])
    tmp <- file.path(tempdir(), "R-CRAN-arrow.spec")
    writeLines(spec, tmp)
    build_spec(tmp, chroots=chroots[i])
  }

  break
}
