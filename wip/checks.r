source("config.r")
source("common.r")
check_copr()

chroots <- get_chroots()
df.mon <- get_monitor()

# check version mismatches
df.mism <- subset_vmism(df.mon, tail(chroots, 1))
pkgs.mism <- sub("R-CRAN-", "", df.mism$Package)
system2("./copr-rebuild-repo.r", paste(pkgs.mism, collapse=" "))

# check failed and non-built
df.fail <- subset_failed(df.mon[, c(1,5)])
df.fail <- subset_failed(df.mon, tail(chroots, 1))
pkgs.fail <- sub("R-CRAN-", "", df.fail$Package)
system2("./copr-rebuild-repo.r", paste(pkgs.fail, collapse=" "))

# inspect failed builds and packages
ids <- sapply(strsplit(df.fail[, chroots[i]], " "), "[", 1)
url <- get_url_builds(list(ids, df.fail$Package), chroots[i])
sapply(paste0(url, "/builder-live.log.gz"), browseURL)
sapply(paste(get_url_copr(), "package", df.fail$Package, sep="/"), browseURL)

# check forked
df.fork <- subset_forked(df.mon, chroots=2)
pkgs <- sub("R-CRAN-", "", df.fork$Package)
system2("./copr-rebuild.r", paste(pkgs, collapse=" "))

# search for packages in rawhide built against v3.6.3
ids <- sapply(strsplit(df.mon[, chroots[i]], " "), head, 1)
ids <- list(ids[1:10], df.mon$Package[1:10])
r4 <- have_build_msg(ids, chroots[i], "f33_R_4", 1000)
sum(!r4)
df.mon[which(!r4), c("Package", chroots[i])]
