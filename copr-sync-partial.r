#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()
#options(copr.chroots=c("fedora-rawhide-x86_64"))

df.mon <- get_monitor()
df.mon <- subset(df.mon, grepl(getOption("copr.prefix"), Package))

pkgs.rebl <- subset_partial(df.mon)$Package
pkgs.rebl <- sub(getOption("copr.prefix"), "", pkgs.rebl)
pkgs.rebl <- with_rebuild_deps(pkgs.rebl)

if (length(pkgs.rebl))
  script_call("./copr-rebuild-repo.r", paste(pkgs.rebl, collapse=" "))
