options(
  copr.cmd       = "copr-cli",
  copr.repo      = "cran",
  copr.clone.url = "https://github.com/Enchufa2/cran2copr",
  copr.subdir    = "specs",
  copr.prefix    = "R-CRAN-",
  copr.tpl       = "specfile.tpl",
  copr.bflags    = "--background",
  repos          = "https://cloud.r-project.org",
  error          = NULL,
  available_packages_filters = c("R_version", "OS_type", "license/FOSS")
)
