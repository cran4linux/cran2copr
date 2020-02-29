#!/usr/bin/env Rscript

# createrepo runs for every delete action
# better to not use this for now...

source("config.r")
source("common.r")
check_copr()

df.mon <- get_monitor()
latest <- unique(unname(sapply(strsplit(unlist(df.mon[,-1]), " "), "[", 1)))

df.builds <- get_builds()
df.rm <- subset(df.builds, !`Build ID` %in% latest)

for (i in seq_len(nrow(df.rm))) {
  copr_call("delete-build", df.rm[i, 1])
  message("  Build ", df.rm[i, 1], " for package ", df.rm[i, 2],
          " removed (", i, "/", nrow(df.rm), ")")
}
