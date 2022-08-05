#!/usr/bin/env Rscript

pgsub <- function(x, pattern, replacement, ...) gsub(pattern, replacement, x, ...)
creplace <- function(x, pattern, replacement) replace(x, x==pattern, replacement)

deps <- read.csv("sysreqs.csv", na.strings="", stringsAsFactors=FALSE)
cran <- tools::CRAN_package_db()[, c("Package", "SystemRequirements")]
cran <- cran[!duplicated(cran), ]

cran$SystemRequirements <- cran$SystemRequirements |>
  pgsub("\n", "") |> # newline
  pgsub(" [\\(]*[>= \\.[:digit:]]+[\\)]*", "") |> # versions
  pgsub("C\\+\\+[[:digit:]]+[,;.]*", "") |> # C++xx
  pgsub("GNU [mM]ake[,;]*", "") |>
  pgsub("gfortran[,;]*", "") |>
  pgsub("gcc[,;]*", "") |>
  pgsub("clang[\\+,;]*", "") |>
  trimws() |>
  creplace("", NA)

cran <- x <- na.omit(cran) |>
  merge(deps[, c("pkg", "revised", "comment")], by.x="Package", by.y="pkg", all=TRUE) |>
  transform(revised = is.na(SystemRequirements) | (revised & SystemRequirements == comment)) |>
  transform(comment = SystemRequirements) |>
  transform(SystemRequirements = NULL)

deps <- merge(deps[, 1:3], cran, by.x="pkg", by.y="Package", all=TRUE)
data.table::fwrite(deps, "sysreqs.csv")
