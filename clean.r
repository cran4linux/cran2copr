source("config.r")
source("common.r")

URL.COPR <- paste("https://copr.fedorainfracloud.org/coprs",
                  copr_call("whoami"), getOption("copr.repo"), sep="/")

html <- xml2::read_html(paste(URL.COPR, "builds", sep="/"))
df <- rvest::html_table(html)[[1]]

df.rm <- df[df$Status == "succeeded",]
df.rm <- df.rm[duplicated(df.rm[,2:3]),]
df.rm <- df.rm[df.rm[,2] %in% unique(df.rm[duplicated(df.rm[,2]), 2]),]

for (i in seq_len(nrow(df.rm))) {
  copr_call("delete-build", df.rm[i, 1])
  message("  Build ", build, " for package ", df.rm[i, 2], " removed (", i, "/", nrow(df.rm), ")")
}
