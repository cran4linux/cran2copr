#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

df.mon <- get_monitor()
df.mon <- subset(df.mon, grepl(getOption("copr.prefix"), Package))

pkgs.mism <- subset_vmism(df.mon)$Package
pkgs.nobl <- subset_nobuild(df.mon)$Package
pkgs.fail <- subset_failed(df.mon)$Package

pkgs.rebl <- setdiff(c(pkgs.mism, pkgs.nobl), pkgs.fail)
pkgs.rebl <- sub(getOption("copr.prefix"), "", pkgs.rebl)
pkgs.rebl <- with_rebuild_deps(pkgs.rebl)

if (length(pkgs.rebl))
  script_call("./copr-rebuild-repo.r", paste(pkgs.rebl, collapse=" "))
