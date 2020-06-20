#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

cran <- available.packages()
copr <- get_copr_list()

pkgs.del <- copr[!copr %in% cran[,"Package"]]
pkgs <- with_deps(cran[,"Package"], cran)
pkgs.add <- pkgs[need_update(pkgs, cran)]

if (length(pkgs.del))
  system2("./copr-delete.r", paste(pkgs.del, collapse=" "))
if (length(pkgs.add))
  system2("./copr-add.r", paste(pkgs.add, collapse=" "))
