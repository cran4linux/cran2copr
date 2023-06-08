script_name <- function()
  strsplit(grep("--file=", commandArgs(FALSE), value=TRUE), "=")[[1]][2]

script_call <- function(...)
  if (system2(...)) q("no", status = 1, runLast = FALSE)

get_args <- function(...) {
  args <- commandArgs(TRUE)
  if (!length(args) || "-h" %in% args)
    stop(...)
  args
}

copr_call <- function(...) {
  copr.cmd <- getOption("copr.cmd")
  if (Sys.which(copr.cmd) == "")
    stop("command '", copr.cmd, "' not found", call.=FALSE)
  args <- paste(..., collapse=" ")
  out <- suppressWarnings(system2(copr.cmd, args, stdout=TRUE, stderr=TRUE))
  if (!is.null(attr(out, "status")))
    stop(paste(out, collapse="\n"), "\n", paste(copr.cmd, args), "' failed", call.=FALSE)
  out
}

copr_version <- function() {
  vstr <- strsplit(copr_call("--version"), " ")[[1]]
  package_version(vstr[length(vstr)])
}

check_copr <- function() {
  if (copr_version() < "1.90")
    stop("version >= 1.90 required")

  tryCatch(invisible(copr_call("whoami")), error=function(e)
    stop("file '~/.config/copr' not found or outdated", call.=FALSE))
}

list_pkgs <- function() {
  tryCatch({
    copr_call("list-package-names", getOption("copr.repo"))
  }, error = function(e) {
    # workaround until https://pagure.io/copr/copr/issue/2071 is fixed
    warning(e)
    pkgs <- copr_call("monitor", getOption("copr.repo"),
                      "--output-format=text-row", "--fields=name")
    unique(pkgs)
  })
}

watch_builds <- function(ids) {
  if (!length(ids)) return(logical(0))

  out <- try(copr_call("watch-build", paste(ids, collapse=" ")), silent=TRUE)
  if (class(out) == "try-error") out <- strsplit(out, "\n")[[1]]
  sapply(ids, function(i) {
    build <- paste0(".* Build ", i, ": ")
    status <- grep(paste0(build, "(succeeded|failed)"), out, value=TRUE)
    ifelse(sub(build, "", status) == "failed", TRUE, FALSE)
  })
}

delete_builds <- function(ids) {
  copr_call("delete-build", paste(ids, collapse=" "))
}

do.call.retry <- function(what, args, ..., n=3, wait=60, skip=TRUE) {
  repeat {
    out <- try(do.call(what, args, ...), silent=TRUE)
    errored <- inherits(out, "try-error")
    n <- n - 1
    if (n == 0 || !errored)
      break
    message("  Retrying in ", wait, " seconds (", n, " retries left)...")
    Sys.sleep(wait)
  }
  if (errored) {
    if (skip) return(NA)
    stop(out, call.=FALSE)
  }
  out
}

.build <- function(x, type=c("spec", "repo"), id, chroots) {
  type <- match.arg(type)
  pkg <- sub("\\.spec", "", basename(x))
  args <- c(
    if (type == "spec") "build" else "build-package",
    "--nowait", getOption("copr.bflags"),
    if (!is.null(id)) paste0("--", names(id), "-build-id ", id),
    if (!is.null(chroots)) paste("-r", chroots, collapse=" "),
    getOption("copr.repo"), paste0(if (type == "repo") "--name ", x)
  )
  out <- do.call.retry(copr_call, as.list(args))
  out <- grep("Created builds", out, value=TRUE)
  out <- as.numeric(strsplit(out, ": ")[[1]][2])
  message("  Build ", out, " for ", pkg, " created from ", type)
  out
}

build_spec <- function(specs, after=NULL, chroots=getOption("copr.chroots")) {
  out <- .build(specs[1], "spec", c(after=after[1]), chroots)
  if (length(specs) == 1) return(out)
  c(out, sapply(specs[-1], .build, "spec", c(with=out), chroots))
}

build_pkg <- function(pkgs, after=NULL, chroots=getOption("copr.chroots")) {
  out <- .build(pkgs[1], "repo", c(after=after[1]), chroots)
  if (length(pkgs) == 1) return(out)
  c(out, sapply(pkgs[-1], .build, "repo", c(with=out), chroots))
}

add_pkg_scm <- function(pkg) {
  out <- copr_call(
    "add-package-scm", getOption("copr.repo"), "--name", pkg,
    "--clone-url", getOption("copr.clone.url"),
    "--subdir", getOption("copr.subdir"), "--spec", paste0(pkg, ".spec"))
  message("  New package ", pkg, " added")
}

delete_pkg_scm <- function(pkg) {
  out <- copr_call("delete-package", getOption("copr.repo"), "--name", pkg)
  message("  Package ", pkg, " removed")
}

available_packages <- function(...) {
  cran <- available.packages()
  cran[!duplicated(cran[, "Package"]), ]
}

with_deps <- function(pkgs, cran=available_packages(), reverse=FALSE) {
  if (!length(pkgs)) return(list())

  base <- rownames(installed.packages(priority="base"))
  excl <- unlist(sapply(dir(pattern="excl-.*\\.txt"), readLines))
  if (!is.null(excl))
    excl <- sapply(strsplit(excl, " "), head, 1)
  pkgs <- setdiff(pkgs, base)

  if (!reverse) {
    avail <- pkgs %in% cran[,"Package"]
    if (any(!avail))
      warning("ignoring ", length(pkgs[!avail]), " packages ",
              "(reason: not on CRAN): ",
              paste(pkgs[!avail], collapse=", "), call.=FALSE)
    pkgs <- pkgs[avail]

    avail <- !pkgs %in% excl
    if (any(!avail))
      warning("ignoring ", length(pkgs[!avail]), " packages ",
              "(reason: exclusions): ",
              paste(pkgs[!avail], collapse=", "), call.=FALSE)
    pkgs <- pkgs[avail]
  }

  deps <- tools::package_dependencies(pkgs, db=cran, recursive=TRUE, reverse=reverse)

  avail <- sapply(deps, function(i) all(setdiff(i, base) %in% cran[,"Package"]))
  if (any(!avail))
    warning("ignoring ", length(names(avail)[!avail]), " packages ",
            "(reason: dependencies not on CRAN): ",
            paste(names(avail)[!avail], collapse=", "), call.=FALSE)
  deps <- deps[avail]

  if (!reverse) {
    avail <- sapply(deps, function(i) all(!setdiff(i, base) %in% excl))
    if (any(!avail))
      warning("ignoring ", length(names(avail)[!avail]), " packages ",
              "(reason: dependencies are exclusions): ",
              paste(names(avail)[!avail], collapse=", "), call.=FALSE)
    deps <- deps[avail]
  }

  setdiff(unique(c(names(deps), unlist(deps))), base)
}

get_build_list <- function(pkgs, cran=available_packages()) {
  base <- rownames(installed.packages(priority="base"))
  pkgs <- lapply(tools::package_dependencies(pkgs, db=cran), setdiff, base)
  pkgs <- lapply(Filter(Negate(is.null), pkgs), intersect, names(pkgs))

  build <- list()
  while (length(pkgs)) {
    x <- names(Filter(function(i) all(i %in% unlist(build)), pkgs))
    build[[length(build)+1]] <- x
    pkgs <- pkgs[!names(pkgs) %in% x]
  }

  build
}

get_copr_list <- function(subset) {
  pkgs <- grep(getOption("copr.prefix"), list_pkgs(), value=TRUE)
  pkgs <- sub(getOption("copr.prefix"), "", pkgs)
  if (missing(subset) || "--all" %in% subset)
    return(pkgs)
  avail <- subset %in% pkgs
  if (any(!avail))
    warning("ignoring ", paste(subset[!avail], collapse=", "), call.=FALSE)
  intersect(pkgs, subset)
}

get_spec_version <- function(spec) {
  if (!file.exists(spec)) return("0.0")
  pattern <- "^\\%global packver[[:space:]]*"
  sver <- grep(pattern, readLines(spec), value=TRUE)
  sub(pattern, "", sver)
}

need_update <- function(pkgs, cran=available_packages()) {
  indb <- cran[cran[,"Package"] %in% pkgs, "Version"]
  if (length(indb) != length(pkgs))
    stop("cannot update packages removed from CRAN")
  nver <- package_version(indb[rank(pkgs)])

  spec <- paste0(getOption("copr.subdir"), "/", getOption("copr.prefix"), pkgs, ".spec")
  over <- package_version(sapply(spec, get_spec_version))

  over < nver
}

.fix_version <- function(deps, cran=available_packages()) {
  # fix 2-component versions declared as 3-component
  two_comp <- grep("^[0-9]+.[0-9]+$", cran[,"Version"], value=TRUE)
  two_comp <- deps$pkg %in% names(two_comp)
  deps[two_comp,]$ver <- sub("([0-9]+.[0-9]+).[0-9]+", "\\1", deps[two_comp,]$ver)

  deps
}

.r_deps <- function(desc, cran=available_packages()) {
  keys <- c("Depends", "Imports", "LinkingTo")
  for (i in keys) if (is.null(desc[[i]]))
    desc[[i]] <- ""

  deps <- gsub("\n", " ", as.matrix(desc)[,keys])
  deps <- gsub("compiler[0-9\\(\\)[:space:]>=.]*,", "", deps)
  deps <- sub("[[:space:]]*,[[:space:]]*$", "", deps)
  deps <- strsplit(deps, "[[:space:]]*,[[:space:]]*")
  deps <- do.call(rbind, lapply(deps, function(i) {
    pkg <- trimws(sub("[[:space:]]*\\(.*\\)$", "", i))
    ver <- mapply(function(x, y) sub(x, "", y), pkg, i)
    ver <- sub("\\((.*)\\)", "\\1", ver)
    ver <- gsub("-", ".", ver)
    data.frame(pkg=pkg, ver=ver, stringsAsFactors=FALSE)
  }))
  if (nrow(deps)) deps$ver <- paste0(" ", trimws(deps$ver))
  deps <- deps[order(deps$ver, decreasing=TRUE),]
  dups <- deps$pkg[duplicated(deps$pkg)]
  for (dup in dups)
    deps$ver[deps$pkg==dup] <- deps$ver[deps$pkg==dup][1]

  .fix_version(deps, cran)
}

.sys_deps <- function(desc) {
  deps <- read.csv("sysreqs.csv", na.strings="", stringsAsFactors=FALSE)
  deps <- deps[deps$pkg == desc$Package,]
  if (!nrow(deps))
    return(character(0))

  x <- character(0)
  if (!is.na(deps$build))
    x <- c(x, paste0("BuildRequires:    ", strsplit(deps$build, " ")[[1]]))
  if (!is.na(deps$run))
    x <- c(x, paste0("Requires:         ", strsplit(deps$run, " ")[[1]]))
  x
}

pkg_deps <- function(desc, cran=available_packages()) {
  x <- .sys_deps(desc)
  deps <- .r_deps(desc, cran)

  if ("rstan" %in% deps$pkg)
    deps <- rbind(deps, c(pkg="rstantools", ver=""))

  rdep <- deps$pkg == "R"
  rver <- deps[rdep, "ver"]
  deps <- deps[!rdep,]
  inbase <- deps$pkg %in% rownames(installed.packages(priority="base"))
  deps$pkg[inbase] <- paste0("R-", deps$pkg[inbase])
  deps$pkg[!inbase] <- paste0(getOption("copr.prefix"), deps$pkg[!inbase])

  x <- c(x, paste0("BuildRequires:    R-devel", rver))
  x <- c(x, paste0("Requires:         R-core", rver))

  if (!isTRUE(cran[cran[,"Package"] == desc$Package, "NeedsCompilation"] == "yes"))
    x <- c(x, "BuildArch:        noarch")

  if (nrow(deps))
    x <- c(x, paste0("BuildRequires:    ", deps$pkg, deps$ver))
  deps <- deps[!grepl("LinkingTo", rownames(deps)),]
  if (nrow(deps))
    x <- c(x, paste0("Requires:         ", deps$pkg, deps$ver))

  x[!duplicated(x)]
}

pkg_exceptions <- function(tpl, pkg, path) {
  # top
  tpl <- c(switch(
    pkg,
    BANOVA=,beam=,Boom=,FastRWeb=,mapdata=,pbdRPC=,pbdPROF=,qtpaint=,RxODE=,
    tth=,wingui=,mixl=,StanHeaders=,mathjaxr=,x13binary="%global debug_package %{nil}",
    tcltk2="%undefine __brp_mangle_shebangs"), tpl)

  # source
  src <- grep("Source0", tpl)
  tpl[src] <- paste0(tpl[src], "\n", switch(
    pkg,
    h2o = paste0(
      "Source1:          https://s3.amazonaws.com/h2o-release/h2o/",
      readLines(file.path(path, "inst/branch.txt")), "/",
      readLines(file.path(path, "inst/buildnum.txt")), "/Rjar/h2o.jar"),
    RcppCGAL = paste0(
      "Source1:          https://github.com/CGAL/cgal/releases/download/v",
      v <- readLines(file.path(path, "inst/VERSION")), "/CGAL-", v, "-library.tar.xz")
  ))

  # setup
  setup <- grep("%setup", tpl)
  tpl[setup] <- paste0(tpl[setup], "\n", switch(
    pkg,
    tcltk2 = paste(
      "sed -i 's@/bin/tclsh8.3@/usr/bin/tclsh@g'",
      "%{packname}/inst/tklibs/ctext3.2/function_finder.tcl"),
    askpass = {
      unlink(dir(file.path(path, "inst"), "^mac.*", full.names=TRUE))
      "rm -f %{packname}/inst/mac*" },
    RUnit = paste(
      "sed -i '/Sexpr/d' %{packname}/man/checkFuncs.Rd\n",
      "sed -i 's/\"runitVirtualClassTest.r\")}/\"runitVirtualClassTest.r\"/g'",
      "%{packname}/man/checkFuncs.Rd"),
    rgeolocate = "echo \"PKG_LIBS += -lrt\" >> %{packname}/src/Makevars.in",
    h2o = "cp %{SOURCE1} %{packname}/inst/java",
    RcppCGAL = "tar xf %{SOURCE1} -C %{packname}/inst */include --strip-components=1",
    nws=,OpenMx=,irace=,configr=,goldi=,RWebLogo=,rSymPy=,ndl=,scrobbler=,
    chromoR=,SoilR=,dynwrap=,RcppRedis=,protViz=,PRISMA=,rgee=paste(
      "find %{packname} -type f -exec",
      "sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python3@g' {} \\;"),
    shinyAce=, googleComputeEngineR =
      "find %{packname}/inst -type f -exec chmod a-x {} \\;",
    TMB = "sed -ie '/onAttach/,+4d' %{packname}/R/zzz.R",
    excerptr = paste(
      "find %{packname}/inst -type f -name *.cl -exec chmod a-x {} \\;\n",
      "find %{packname}/inst -type f -exec",
      "sed -Ei 's@#!( )*(/usr)*/bin/(env )*dash@#!/usr/bin/sh@g' {} \\;"),
    funr = paste(
      "find %{packname}/inst -type f -exec",
      "sed -Ei 's@#!( )*(/usr)/bin/(env )*lr@#!/usr/bin/r@g' {} \\;"),
    getopt = paste(
      "find %{packname} -type f -exec",
      "sed -Ei 's@/path/to/Rscript@/usr/bin/Rscript@g' {} \\;"),
    rhli = "rm -f %{packname}/src/Makevars*",
    spcosa = "sed -i '/Sexpr/d' %{packname}/man/spcosa-package.Rd",
    rgexf = "sed -i '/system.file/d' %{packname}/man/plot.gexf.Rd",
    svSocket = paste(
      "find %{packname} -type f -exec",
      "sed -Ei 's@/bin/tclsh8.4@/bin/tclsh@g' {} \\;"),
    datasailr = "autoreconf -i %{packname}/src/Onigmo",
    uavRmp = paste0(
      "sed -i '1d' %{packname}/inst/python/io_solo_params_community.py\n",
      "find %{packname} -type f -exec ",
      "sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \\;"),
    arrow = "sed -i 's|PKGCONFIG_DIRS=.*|PKGCONFIG_DIRS=-L%{_libdir}|' %{packname}/configure",
    bigmemory = "sed -i 's|-luuid||g' %{packname}/configure"
  ))

  # install
  install <- grep("%install", tpl)
  tpl[install] <- paste0(tpl[install], "\n", switch(
    pkg,
    aws=,biglars=,bsamGP=,deldir=,deSolve=,DRAFT=,DynamicGP=,EDR=,eha=,float=,
    frailtypack=,frontier=,lbfgsb3=,lbfgsb3c=,lsei=,mclust=,mda=,n1qn1=,
    npsp=,robeth=,robustbase=,rootSolve=,sequoia=,subplex=,VGAM=paste(
      "test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R &&",
      "echo \"FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch\" > ~/.R/Makevars"),
    rPython = "export RPYTHON_PYTHON_VERSION=3",
    RcppParallel = paste0(
      "export TBB_INC=%{_includedir}/tbb\n",
      "export TBB_LIB=%{_libdir}"),
    Rmpi=,pbdMPI=,pbdSLAP=,bigGP =
      "%{_openmpi_load}\nexport MPI_LIB_PATH=$MPI_LIB\nexport MPI_TYPE=OPENMPI"
  ))
  install <- grep("CMD INSTALL", tpl)
  tpl[install] <- paste0(tpl[install], switch(
    pkg,
    Rmpi=,pbdMPI=,pbdSLAP=,bigGP = "\n%{_openmpi_unload}",
    udunits2 = "\\\n  --configure-args='--with-udunits2-include=/usr/include/udunits2'"
  ))

  # other
  if (pkg %in% c("adapr", "taber"))
    unlink(file.path(path, "data"))
  if (pkg %in% c("x13binary"))
    dir.create(file.path(path, "src"))

  tpl
}

create_spec <- function(pkg, cran=available_packages(), write=TRUE) {
  tarfile <- download.packages(pkg, tempdir(), cran, quiet=TRUE)[,2]
  untar(tarfile, exdir=tempdir())
  path <- file.path(tempdir(), pkg)
  tpl <- readLines(getOption("copr.tpl"))
  tpl <- pkg_exceptions(tpl, pkg, path)

  # fields
  desc <- read.dcf(file.path(path, "DESCRIPTION"))
  desc <- as.data.frame(desc, stringsAsFactors=FALSE)
  cran[cran[,"Package"] == desc$Package, "NeedsCompilation"] <-
    if (dir.exists(file.path(path, "src"))) "yes" else "no"
  deps <- pkg_deps(desc, cran)
  description <- strwrap(desc$Description, 75)
  description <- gsub("%", "%%", description)

  tpl <- sub("\\{\\{prefix\\}\\}", getOption("copr.prefix"), tpl)
  tpl <- sub("\\{\\{packname\\}\\}", pkg, tpl)
  tpl <- sub("\\{\\{packver\\}\\}", desc$Version, tpl)
  tpl <- sub("\\{\\{version\\}\\}", gsub("-", ".", desc$Version), tpl)
  tpl <- sub("\\{\\{summary\\}\\}", gsub("\n", " ", desc$Title), tpl)
  tpl <- sub("\\{\\{license\\}\\}", desc$License, tpl)
  tpl <- sub("\\{\\{dependencies\\}\\}", paste(deps, collapse="\n"), tpl)
  tpl <- sub("\\{\\{description\\}\\}", paste(description, collapse="\n"), tpl)

  # java
  if (any(grepl("BuildRequires:[[:space:]]+R-java-devel", deps))) {
    inst <- grep("R CMD INSTALL", tpl)
    tpl[inst] <- paste0("%{_bindir}/R CMD javareconf -e '", tpl[inst], "'")
  }
  # display
  if (any(grepl("BuildRequires:[[:space:]]+xorg-x11-server-Xvfb", deps))) {
    inst <- grep("R CMD INSTALL", tpl)
    tpl[inst] <- paste("xvfb-run", tpl[inst])
  }

  pkg <- paste0(getOption("copr.prefix"), pkg)
  dest <- paste0(getOption("copr.subdir"), "/", pkg, ".spec")
  if (write) writeLines(tpl, dest)
  list(pkg=pkg, dest=dest, spec=tpl)
}

get_url_copr <- function() paste(
  "https://copr.fedorainfracloud.org/coprs",
  copr_call("whoami"), getOption("copr.repo"), sep="/")

get_url_back <- function() paste(
  "https://copr-be.cloud.fedoraproject.org/results",
  copr_call("whoami"), getOption("copr.repo"), sep="/")

get_url_builds <- function(ids, chroots) {
  stopifnot(is.list(ids))
  pkgs <- ids[[2]]
  ids <- ids[[1]]
  ids <- ifelse(nchar(ids) == 7, paste0(0, ids), ids)
  paste0(get_url_back(), "/", chroots, "/", ids, "-", pkgs)
}

get_chroots <- function() {
  repo <- paste0(copr_call("whoami"), "/", getOption("copr.repo"))
  out <- grep(repo, copr_call("list"), value=TRUE)
  trimws(sapply(strsplit(out, ":"), "[", 1))
}

.read_urls <- function(urls, bytes=NULL) {
  tmp <- tempfile(rep("file", length(urls)))
  file.create(tmp)
  timeout <- getOption("timeout")
  on.exit({
    unlink(tmp)
    options(timeout=timeout)
  })
  options(timeout=3600L)

  headers <- character(0)
  if (!is.null(bytes))
    headers <- c(headers, range=paste0("bytes=0-", bytes-1))
  try(suppressWarnings(
    download.file(urls, tmp, mode="a", headers=headers)), silent=TRUE)
  lapply(tmp, readLines, warn=FALSE)
}

get_monitor <- function() {
  out <- copr_call("monitor", "--output-format=text-row", getOption("copr.repo"))
  out <- read.delim(textConnection(out),
                    col.names=c("Package", "chroot", "id", "status", "version"))
  out$status <- with(out, paste(id, status, version))
  out$id <- out$version <- NULL
  out <- reshape(out, idvar="Package", timevar="chroot", direction="wide")
  out <- out[, sort(colnames(out))]
  colnames(out) <- sub("status.", "", colnames(out))
  merge(out, data.frame(Package=setdiff(list_pkgs(), out$Package)), all=TRUE)
}

get_builds <- function() {
  stopifnot(requireNamespace("XML", quietly=TRUE))
  url <- paste(get_url_copr(), "builds", sep="/")
  XML::readHTMLTable(.read_urls(url)[[1]])[[1]]
}

get_batch <- function(id) {
  stopifnot(requireNamespace("XML", quietly=TRUE))
  url <- paste("https://copr.fedorainfracloud.org/batches/detail", id, sep="/")
  XML::readHTMLTable(.read_urls(url)[[1]])[[1]]
}

subset_failed <- function(x, chroots=seq_len(ncol(x)-1), nobuild=FALSE) {
  x.chrt <- x[, 2:ncol(x), drop=FALSE]
  x.fail <- x.chrt[, chroots, drop=FALSE]
  x.succ <- x.chrt[, setdiff(names(x.chrt), names(x.fail)), drop=FALSE]
  x.fail <- if (nobuild)
    apply(x.fail, 2, function(x) !grepl("succeeded|forked", x))
  else apply(x.fail, 2, function(x) grepl("failed", x))
  x.succ <- apply(x.succ, 2, function(x) grepl("succeeded|forked", x))
  subset(x, apply(cbind(x.fail, x.succ), 1, all))
}

subset_forked <- function(x, chroots=seq_len(ncol(x)-1), nobuild=FALSE) {
  x.fork <- x[, 2:ncol(x), drop=FALSE][, chroots, drop=FALSE]
  x.fork <- apply(x.fork, 2, function(x) grepl("forked", x))
  subset(x, apply(x.fork, 1, all))
}

subset_vmismatch <- function(x, chroots=seq_len(ncol(x)-1), cran=available_packages()) {
  n <- ncol(x); chroots <- chroots

  cran <- as.data.frame(cran)[, c("Package", "Version")]
  cran$Package <- paste0("R-CRAN-", cran$Package)
  cran$Version <- gsub("-", ".", cran$Version)
  x <- merge(x, cran, all.x=TRUE)

  x.mism <- x[, 2:n, drop=FALSE][, chroots, drop=FALSE]
  x.mism <- apply(x.mism, 2, function(x) {
    ver <- sapply(strsplit(x, "[[:space:]]+"), "[", 3)
    sapply(strsplit(ver, "-"), "[", 1)
  })
  x.mism <- cbind(x.mism, Version=x$Version)
  x.mism <- apply(x.mism, 1, function(x) {
    !all(sapply(seq_along(x)[-1], function(i) x[1] == x[i]), na.rm=TRUE)
  })
  subset(x, x.mism)
}

have_build_msg <- function(ids, chroots, msg, bytes=NULL) {
  urls <- paste0(get_url_builds(ids, chroots), "/builder-live.log.gz")
  contents <- .read_urls(urls, bytes=bytes)
  grepl(msg, contents)
}

.repo <- function() paste0(
  "'copr:copr.fedorainfracloud.org:",
  copr_call("whoami"), ":", getOption("copr.repo"), "'")

list_available <- function(releasever) {
  args <- c(
    "list", "--available",
    if (!missing(releasever)) paste("--releasever", releasever),
    "--repo", .repo(), "R-CRAN-*"
  )
  out <- system2("dnf", args, stdout=TRUE)[-(1:2)]
  out <- sapply(strsplit(out, " "), "[", 1)
  out <- sub("^R-CRAN-", "", out)
  out <- sub("\\.src$|\\.noarch$|\\.x86_64$", "", out)
  out <- sub("-debuginfo$|-debugsource$", "", out)
  out[!duplicated(out)]
}

run_repoclosure <- function(releasever) {
  args <- c(
    "repoclosure",
    if (!missing(releasever)) paste("--releasever", releasever),
    "--check", .repo()
  )
  system2("dnf", args)
}
