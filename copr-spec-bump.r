#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " [--all | pkg1 ...]")

pkgs <- get_copr_list(args)
pkgs <- paste0(getOption("copr.prefix"), pkgs)
pkgs <- paste0(getOption("copr.subdir"), "/", pkgs, ".spec")

message("Bumping release of ", length(pkgs), " packages")

for (pkg in pkgs) {
  spec <- readLines(pkg)
  pattern <- "^(Release:[[:space:]]+)([0-9]+)(%\\{\\?dist\\})"
  release <- as.numeric(sub(pattern, "\\2", spec[grep(pattern, spec)]))
  spec <- sub(pattern, paste0("\\1", release+1, "\\3"), spec)
  writeLines(spec, pkg)
}
