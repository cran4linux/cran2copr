#!/usr/bin/env Rscript

library(furrr)
plan(multicore, workers=4)

options(repos = "https://cloud.r-project.org")

path <- "~/copr/DESC/"
url <- paste0(getOption("repos"), "/web/packages/")
pkgs <- available_packages()[,"Package"]

invisible(future_map(pkgs, function(pkg) {
  download.file(paste0(url, pkg, "/DESCRIPTION"), paste0(path, pkg), quiet=TRUE)
}, .progress=TRUE))
