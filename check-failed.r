source("config.r")
source("common.r")
check_copr()

chroots <- get_chroots()
df.mon <- get_monitor()

df.fail <- subset_failed(df.mon[, c("Package", chroots[1:2])])
ids <- sapply(strsplit(df.fail[, chroots[1]], " "), "[", 1)
url <- get_url_build(ids, df.fail$Package, chroots[1])

# sapply(url, browseURL)
