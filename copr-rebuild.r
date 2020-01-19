#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " [--all | pkg1 ...]")

pkgs <- get_copr_list(args)
blist <- get_build_list(pkgs)
n <- length(unlist(blist))

for (pkgs in blist) {
  message("Building ", length(pkgs), " packages of ", n, " remaining...")

  pkgs <- paste0(getOption("copr.subdir"), "/", getOption("copr.prefix"), pkgs, ".spec")
  ids <- sapply(pkgs, build_spec)

  message("Waiting for ", length(pkgs), " packages of ", n, " remaining...")

  res <- watch_builds(ids)

  if (any(res))
    stop("Some builds failed:\n",
         paste("  Build", ids[res], "for", pkgs[res], "failed", collapse="\n"))

  n <- n - length(pkgs)
}
