#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " pkg1 [pkg2 ...]")

pkgs <- with_deps(args, reverse=TRUE)
pkgs <- pkgs[pkgs %in% get_copr_list()]
if (!length(pkgs)) quit(status=0)
pkgs <- paste0(getOption("copr.prefix"), pkgs)

message("Removing ", length(pkgs), " packages")

for (pkg in pkgs) {
  del_pkg_scm(pkg)
  unlink(paste0(getOption("copr.subdir"), "/", pkg, ".spec"))
}
