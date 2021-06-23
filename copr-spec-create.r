#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " [--all | pkg1 ...]")

pkgs <- get_copr_list(args)
cran <- available_packages()

message("Recreating spec of ", length(pkgs), " packages")

for (pkg in pkgs) {
  message("Processing ", pkg, "...")
  invisible(create_spec(pkg, cran))
}
