#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " pkg1 [pkg2 ...]")

copr <- list_pkgs()
cran <- available_packages()
pkgs <- with_deps(args, cran)
pkgs <- pkgs[need_update(pkgs, cran)]

if (file.exists("DEBUG")) {
  cat(pkgs, sep="\n")
  quit(status=0)
}

blist <- get_build_list(pkgs, cran)
n <- length(unlist(blist))
ids <- NULL

for (pkgs in blist) {
  message("Building ", length(pkgs), " packages of ", n, " remaining...")

  specs <- sapply(pkgs, function(pkg) {
    spec <- create_spec(pkg, cran)
    if (!spec$pkg %in% copr) tryCatch(
      add_pkg_scm(spec$pkg),
      error = function(e) if (!grepl("already exists", e)) stop(e)
    )
    spec$dest
  })
  ids <- build_spec(specs, ids)

  n <- n - length(pkgs)
}
