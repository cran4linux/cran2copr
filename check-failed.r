source("config.r")
source("common.r")
check_copr()

chroots <- get_chroots()
df.mon <- get_monitor()

df.fail <- subset_failed(df.mon[, c("Package", chroots[1:2])])
ids <- sapply(strsplit(df.fail[, chroots[2]], " "), "[", 1)
url <- get_url_build(ids, df.fail$Package, chroots[2])

# sapply(paste0(url, "/builder-live.log.gz"), browseURL)
# pkg <- "rgexf"; writeLines(create_spec(pkg), paste0("specs/R-CRAN-", pkg, ".spec"))
# sapply(df.fail$Package, build_pkg, chroots[2])
