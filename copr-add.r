#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " pkg1 [pkg2 ...]")

cran <- available.packages()
pkgs <- with_deps(args, cran)
pkgs <- pkgs[need_update(pkgs, cran)]
blist <- get_build_list(pkgs, cran)
n <- length(unlist(blist))

for (pkgs in blist) {
  message("Building ", length(pkgs), " packages of ", n, " remaining...")

  tars <- download.packages(pkgs, tempdir(), cran)[,2]
  spec <- mapply(create_spec, pkgs, tars, SIMPLIFY=FALSE)
  pkgs <- paste0(getOption("copr.prefix"), pkgs)
  dest <- paste0(getOption("copr.subdir"), "/", pkgs, ".spec")

  for (i in pkgs[!pkgs %in% list_pkgs()])
    add_pkg_scm(i)
  mapply(writeLines, spec, dest)
  ids <- sapply(dest, build_spec)
  res <- watch_builds(ids)

  if (any(res))
    stop("Some builds failed:\n",
         paste("  Build", ids[res], "for", pkgs[res], "failed", collapse="\n"))

  n <- n - length(pkgs)
}
