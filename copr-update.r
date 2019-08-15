#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " [--all | pkg1 ...]")

cran <- available.packages()
pkgs <- get_copr_list(args)
pkgs <- pkgs[need_update(pkgs, cran)]
pkgs <- with_deps(pkgs, cran)
pkgs <- pkgs[need_update(pkgs, cran)]

if (length(pkgs))
  system2("./copr-add.r", paste(pkgs, collapse=" "))
