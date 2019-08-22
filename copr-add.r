#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " pkg1 [pkg2 ...]")

copr <- list_pkgs()
cran <- available.packages()
pkgs <- with_deps(args, cran)
pkgs <- pkgs[need_update(pkgs, cran)]
blist <- get_build_list(pkgs, cran)
n <- length(unlist(blist))

for (pkgs in blist) {
  message("Building ", length(pkgs), " packages of ", n, " remaining...")

  ids <- sapply(pkgs, function(pkg) {
    tarf <- download.packages(pkg, tempdir(), cran, quiet=TRUE)
    spec <- create_spec(pkg, tarf[,2])
    pkg <- paste0(getOption("copr.prefix"), pkg)
    dest <- paste0(getOption("copr.subdir"), "/", pkg, ".spec")
    if (!pkg %in% copr) add_pkg_scm(pkg)
    writeLines(spec, dest)
    build_spec(dest)
  })

  message("Waiting for ", length(pkgs), " packages of ", n, " remaining...")

  res <- watch_builds(ids)

  if (any(res))
    stop("Some builds failed:\n",
         paste("  Build", ids[res], "for", pkgs[res], "failed", collapse="\n"))

  n <- n - length(pkgs)
}
