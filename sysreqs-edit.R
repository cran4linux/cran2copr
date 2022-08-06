cran <- tools::CRAN_package_db()[, c("Package", "NeedsCompilation", "Depends", "Imports")]
cran <- cran[!duplicated(cran$Package), ]
names(cran) <- c("pkg", "nc", "dep", "imp")

deps <- read.csv("sysreqs.csv", na.strings="", stringsAsFactors=FALSE)
deps <- merge(deps, cran, all.x=TRUE)
deps$revised <- as.factor(deps$revised)
deps$nc <- as.factor(deps$nc == "yes")
comment <- deps$comment; deps$comment <- NULL; deps$comment <- comment

deps <- DataEditR::data_edit(
  deps,
  col_edit = FALSE,
  col_options = list(revised = c(TRUE, FALSE), nc = c(TRUE, FALSE)),
  col_names = FALSE,
  col_readonly = c("pkg", "nc", "dep", "imp", "comment"),
  row_edit = FALSE,
  viewer_height = 1080,
  viewer_width = 1920
)

data.table::fwrite(deps[, c(1:4, 8)], "sysreqs.csv")

# cleanup archived
archived <- is.na(deps$comment) & is.na(deps$nc)
sum(archived)
deps <- deps[!archived, ]
