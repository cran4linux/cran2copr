# cran2copr

[![Daily sync](https://github.com/Enchufa2/cran2copr/actions/workflows/sync.yml/badge.svg)](https://github.com/Enchufa2/cran2copr/actions/workflows/sync.yml)
[![Docker images](https://github.com/Enchufa2/cran2copr/actions/workflows/docker.yml/badge.svg)](https://github.com/Enchufa2/cran2copr/actions/workflows/docker.yml)

Bringing R packages to Fedora (in fact, to any distro) is an Herculean task, especially considering the rate at which [CRAN](https://cran.r-project.org) grows nowadays. This is an attempt to maintain RPM repos for most of CRAN (~15k packages as of Feb. 2020) in an automated way using [Fedora Copr](https://copr.fedorainfracloud.org/), while ensuring compatibility with the packages already in the official repos.

## Support

Currently, only x86_64 chroots for supported (non-EOL) versions of Fedora, including rawhide, are enabled. If you are interested in other chroots (from the supported architectures and distros), please [open an issue on GitHub](https://github.com/Enchufa2/cran2copr/issues) expressing so, but it is unlikely that it will be enabled in the short to medium term due to current storage limitations in the Copr infrastructure.

These repos are automatically synchronized with CRAN every day at 00:00 UTC through a GitHub Action that removes archived packages and builds the most recent updates. If you find any issue with any of the supported packages (see details and limitations below), please [open an issue on GitHub](https://github.com/Enchufa2/cran2copr/issues).

Integration with `install.packages` is handled via `CoprManager` (see installation instructions below). If you experience any related issues, please [open an issue in the `bspm` repository](https://github.com/Enchufa2/bspm/issues), which is the upstream source for `CoprManager`.

## Installation

To enable this Copr repository in your system:

```bash
$ sudo dnf copr enable iucar/cran
$ sudo dnf install R-CoprManager
```

By default, CoprManager is enabled, and you can install or update packages in R as you normally do, e.g.,

```r
install.packages("car")
update.packages(ask=FALSE)
```

In the background, a D-Bus service installs the available packages from this Copr repo, and the remaining ones, from CRAN, all within the same call. On the other hand, `remove.packages` will still remove only packages installed in your user library. If you want to remove system packages, run:

```r
CoprManager::remove_copr("car")
```

If you want to disable the CoprManager, so that `install.packages` only works with CRAN again, then run:

```r
CoprManager::disable()
install.packages("car") # from CRAN to user lib
```

## Details and limitations

This project works with a set of R scripts around the `copr-cli` Python tool, which is rather limited yet.

SPECs are generated from a standard template (see `spec.in`), a list of system requirements (currently manually maintained; see the `TODO` list for a possible replacement), and a handful of fixes for particular cases (because, despite all the good work by the CRAN team, still some bad practices sneak in).

All in all, this procedure must work in an automated way for ~15k packages (as of Feb. 2020), which means that this project needs to relax some packaging guidelines that are otherwise enforced in the official Fedora repos. Particularly,

- Package names, versions and license strings are copied from DESCRIPTION files unmodified.
- Dependencies are probably over-specified in most cases, but this shouldn't be a problem.
- Packages are built as-is, without unbundling any included third-party library.
- To ensure compatibility with the official repos, the `/usr/local` prefix is used for package installation.
- All packages are installed under `/usr/local/lib/R/library` (no distinction for noarch packages, which, following Fedora's guidelines, should be placed under `share/R/library` instead).
- Noarch packages incorrectly flagged as needing compilation are inadvertently built as arch-specific.
- Packages that require (Depends or Imports) Bioconductor packages are excluded (see `excl-no-deps.txt`).
- Packages that require unsupported system requirements are excluded (see `excl-no-sysreqs.txt`).
