options(
  copr.cmd         = "copr-cli",
  copr.repo        = "cran",
  copr.clone.url   = "https://github.com/cran4linux/cran2copr",
  copr.subdir      = "specs",
  copr.prefix      = "R-CRAN-",
  copr.tpl         = "spec.in",
  copr.bflags      = "",
  copr.chroots     = paste("fedora", c(38:39, "rawhide"), "x86_64", sep="-"),
  repos            = "https://cran.r-project.org",
  error            = NULL,
  stringsAsFactors = FALSE,
  available_packages_filters = c("OS_type", "license/FOSS")
)
