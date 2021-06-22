#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()
options(copr.bflags="--background")
options(copr.chroots="fedora-rawhide-x86_64")

args <- get_args("Usage: ", script_name(), " [--all | pkg1 ...]")

pkgs <- get_copr_list(args)
blist <- get_build_list(pkgs)
n <- length(unlist(blist))
ids <- NULL

for (pkgs in blist) {
  message("Building ", length(pkgs), " packages of ", n, " remaining...")

  pkgs <- paste0(getOption("copr.subdir"), "/", getOption("copr.prefix"), pkgs, ".spec")
  ids <- build_spec(pkgs, ids)

  n <- n - length(pkgs)
}
