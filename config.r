options(
  copr.cmd         = "copr-cli",
  copr.repo        = "cran",
  copr.clone.url   = "https://github.com/Enchufa2/cran2copr",
  copr.subdir      = "specs",
  copr.prefix      = "R-CRAN-",
  copr.tpl         = "specfile.tpl",
  copr.bflags      = "",
  copr.chroots     = c("fedora-31-x86_64", "fedora-rawhide-x86_64"),
  copr.watch       = FALSE,
  repos            = "https://cran.r-project.org",
  error            = NULL,
  stringsAsFactors = FALSE,
  available_packages_filters = c("OS_type", "license/FOSS")
)
