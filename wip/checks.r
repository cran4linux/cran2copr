source("config.r")
source("common.r")
check_copr()
#options(copr.bflags="--background")

chroots <- get_chroots()
df.mon <- get_monitor()

i <- 3
df.fail <- subset_failed(df.mon[, c("Package", chroots[i])])
df.fail.common <- subset_failed(df.mon[, c("Package", chroots[2:3])])
no.common <- !df.fail$Package %in% df.fail.common$Package
pkgs <- sub("R-CRAN-", "", df.fail$Package[no.common])
blist <- get_build_list(pkgs)
for (i in seq_along(blist)) {
  n <- formatC(i, width=2, format="d", flag="0")
  writeLines(blist[[i]], paste0("f33-rebuild-", n, ".txt"))
}

ids <- sapply(strsplit(df.fail[, chroots[i]], " "), "[", 1)
url <- get_url_builds(list(ids, df.fail$Package), chroots[i])
# sapply(paste0(url, "/builder-live.log.gz"), browseURL)
# create_spec("pexm")
# sapply(df.fail$Package, build_pkg, chroots[i])
pkgs <- unlist(get_build_list(sub("R-CRAN-", "", df.fail$Package)))
sapply(paste0("R-CRAN-", pkgs), build_pkg, chroots[i])

# search for packages in rawhide built against v3.6.3
ids <- sapply(strsplit(df.mon[, chroots[i]], " "), head, 1)
ids <- list(ids[1:10], df.mon$Package[1:10])
r4 <- have_build_msg(ids, chroots[i], "f33_R_4", 1000)
sum(!r4)
df.mon[which(!r4), c("Package", chroots[i])]

# check version mismatches
df.mism <- subset_vmismatch(df.mon)
pkgs <- sub("R-CRAN-", "", df.mism$Package)
blist <- get_build_list(pkgs)
for (i in seq_along(blist)) {
  n <- formatC(i, width=2, format="d", flag="0")
  writeLines(blist[[i]], paste0("fall-rebuild-", n, ".txt"))
}
