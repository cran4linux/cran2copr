script_name <- function()
  strsplit(grep("--file=", commandArgs(FALSE), value=TRUE), "=")[[1]][2]

get_args <- function(...) {
  args <- commandArgs(TRUE)
  if (!length(args) || "-h" %in% args) {
    message(...)
    quit(status=1)
  }
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

check_copr <- function() {
  tryCatch(invisible(copr_call("whoami")), error=function(e)
    stop("file '~/.config/copr' not found or outdated", call.=FALSE))
}

list_pkgs <- function() {
  copr_call("list-package-names", getOption("copr.repo"))
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

build_spec <- function(spec) {
  pkg <- sub("\\.spec", "", basename(spec))
  out <- copr_call("build", "--nowait", getOption("copr.repo"), spec)
  out <- grep("Created builds", out, value=TRUE)
  out <- as.numeric(strsplit(out, ": ")[[1]][2])
  message("  Build ", out, " for ", pkg, " created from SPEC")
  out
}

build_pkg <- function(pkg, chroots) {
  chroots <- if (missing(chroots)) "" else paste("-r", chroots, collapse=" ")
  out <- copr_call("build-package", "--nowait",
                   getOption("copr.repo"), "--name", pkg, chroots)
  out <- grep("Created builds", out, value=TRUE)
  out <- as.numeric(strsplit(out, ": ")[[1]][2])
  message("  Build ", out, " for ", pkg, " created from repo")
  out
}

add_pkg_scm <- function(pkg) {
  out <- copr_call(
    "add-package-scm", getOption("copr.repo"), "--name", pkg,
    "--clone-url", getOption("copr.clone.url"),
    "--subdir", getOption("copr.subdir"), "--spec", paste0(pkg, ".spec"))
  message("  New package ", pkg, " added")
}

del_pkg_scm <- function(pkg) {
  out <- copr_call("delete-package", getOption("copr.repo"), "--name", pkg)
  message("  Package ", pkg, " removed")
}

with_deps <- function(pkgs, cran=available.packages(), reverse=FALSE) {
  if (!length(pkgs)) return(list())

  base <- rownames(installed.packages(priority="high"))
  excl <- unlist(sapply(dir(pattern="excl-.*\\.txt"), readLines))
  pkgs <- setdiff(pkgs, base)

  avail <- pkgs %in% cran[,"Package"]
  if (any(!avail))
    warning("ignoring ", paste(pkgs[!avail], collapse=", "),
            " because they are not on CRAN", call.=FALSE)
  pkgs <- pkgs[avail]

  avail <- !pkgs %in% excl
  if (any(!avail))
    warning("ignoring ", paste(pkgs[!avail], collapse=", "),
            " because they are exclusions", call.=FALSE)
  pkgs <- pkgs[avail]

  deps <- tools::package_dependencies(pkgs, db=cran, recursive=TRUE, reverse=reverse)

  avail <- sapply(deps, function(i) all(setdiff(i, base) %in% cran[,"Package"]))
  if (any(!avail))
    warning("ignoring ", paste(names(avail)[!avail], collapse=", "),
            " because one or more dependencies are not on CRAN", call.=FALSE)
  deps <- deps[avail]

  if (!reverse) {
    avail <- sapply(deps, function(i) all(!setdiff(i, base) %in% excl))
    if (any(!avail))
      warning("ignoring ", paste(names(avail)[!avail], collapse=", "),
              " because one or more dependencies are exclusions", call.=FALSE)
    deps <- deps[avail]
  }

  setdiff(unique(c(names(deps), unlist(deps))), base)
}

get_build_list <- function(pkgs, cran=available.packages()) {
  base <- rownames(installed.packages(priority="high"))
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

need_update <- function(pkgs, cran=available.packages()) {
  indb <- cran[cran[,"Package"] %in% pkgs, "Version"]
  if (length(indb) != length(pkgs))
    stop("cannot update packages removed from CRAN")
  nver <- package_version(indb[rank(pkgs)])

  spec <- paste0(getOption("copr.subdir"), "/", getOption("copr.prefix"), pkgs, ".spec")
  over <- package_version(sapply(spec, get_spec_version))

  over < nver
}

pkg_files <- function(pkg, path) {
  topdir <- "^DESCRIPTION$|^NAMESPACE$|^LICEN(S|C)E$|^NEWS|^R$|^data$|demo|exec"
  nodocs <- "DESCRIPTION|INDEX|NAMESPACE|/R$|libs|data|include|LICEN"
  license <- "LICEN"

  instignore <- file.path(path, ".Rinstignore")
  if (file.exists(instignore)) {
    instignore <- suppressWarnings(readLines(instignore))
    instignore <- setdiff(sub("^inst/", "", instignore), "")
    unlink(unlist(sapply(instignore, function(i)
      dir(file.path(path, "inst"), i, full.names=TRUE))), recursive=TRUE)
  }

  files <- grep(topdir, dir(path), value=TRUE)
  files <- c(files, dir(file.path(path, "inst")))

  if (length(dir(file.path(path, "man"))))
    files <- c(files, "INDEX")
  if (file.exists(file.path(path, "src")))
    files <- c(files, "libs")

  # exceptions
  files <- c(files, switch(
    pkg, stringi=,dparser="include", readr="rcon", maps=,mapdata="mapdata",
    littler=,processx=,ps=,zip=,phylocomr=,arulesSequences=,brotli=,cepreader="bin",
    RcppParallel=,StanHeaders=,RInside=,Boom="lib", rscala="dependencies",
    pbdZMQ="etc", antiword=c("bin", "share"), TMB="Matrix-version", icd="COPYING",
    Rttf2pt1="exec", FastRWeb=c("Rcgi", "cgi-bin")))

  files <- paste0("%{rlibdir}/%{packname}/", files)
  files[!grepl(nodocs, files)] <- paste("%doc", files[!grepl(nodocs, files)])
  files[grep(license, files)] <- paste("%license", files[grep(license, files)])

  files
}

.r_deps <- function(desc) {
  keys <- c("Depends", "Imports", "LinkingTo")
  for (i in keys) if (is.null(desc[[i]]))
    desc[[i]] <- ""

  deps <- gsub("\n", " ", as.matrix(desc)[,keys])
  deps <- gsub("compiler,*", "", deps)
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
  deps
}

.sys_deps <- function(desc) {
  deps <- read.csv("sysreqs.csv", na.strings="", stringsAsFactors=FALSE)
  deps <- deps[deps$pkg == desc$Package,]
  if (!nrow(deps))
    return(character(0))

  x <- character(0)
  if (!is.na(deps$build))
    x <- c(x, paste0("BuildRequires:    ", strsplit(deps$build, ", ")[[1]]))
  if (!is.na(deps$run))
    x <- c(x, paste0("Requires:         ", strsplit(deps$run, ", ")[[1]]))
  x
}

pkg_deps <- function(desc) {
  x <- .sys_deps(desc)
  deps <- .r_deps(desc)

  rdep <- deps$pkg == "R"
  rver <- deps[rdep, "ver"]
  deps <- deps[!rdep,]
  inbase <- deps$pkg %in% rownames(installed.packages(priority="high"))
  deps$pkg[inbase] <- paste0("R-", deps$pkg[inbase])
  deps$pkg[!inbase] <- paste0(getOption("copr.prefix"), deps$pkg[!inbase])

  x <- c(x, paste0("BuildRequires:    R-devel", rver))
  x <- c(x, paste0("Requires:         R-core", rver))

  old_nc <- c(
    "proj4", "pdist", "FMStable", "mlbench", "allelic", "apple", "nnls", "mlmmm",
    "fracdiff", "flashClust", "biglars", "fpow", "mcclust", "brainwaver", "EL",
    "emoa", "genepi", "EMC", "clusteval", "cgh", "lassoshooting", "ftnonpar",
    "IndependenceTests", "imputeMDR", "hier.part", "factorQR", "dblcens", "ifa",
    "datamap", "condmixt", "emdist", "exactLoglinTest", "darts", "coxrobust",
    "ezglm", "fugeR", "GWASExactHW", "HybridMC", "identity", "ieeeround",
    "JASPAR", "Kendall", "LogitNet", "endogMNP", "dpglasso")
  if (!isTRUE(desc$NeedsCompilation == "yes") && !desc$Package %in% old_nc)
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
    StanHeaders=,reshape=,SIBER=,bestglm=,pbdRPC=,AGHmatrix=,anacor=,aspect=,
    analogueExtra=,oai=,mapdata=,CARRoT=,Boom=,beam=,BANOVA=,deisotoper=,cfa=,
    BNPdensity=,bcgam=,jmdl=,brglm2=,FastRWeb=,HDDesign=,mQTL=,MHTmult=,dfped=,
    intRegGOF=,idmTPreg=,fxtract=,doubcens=,IGG=,ITRLearn=,ITRSelect=,lcc=,
    esmprep=,MBSP=,MOLHD=,isotone="%global debug_package %{nil}",
    tcltk2="%undefine __brp_mangle_shebangs"), tpl)

  # source
  src <- grep("Source0", tpl)
  tpl[src] <- paste0(tpl[src], "\n", switch(
    pkg,
    h2o = paste0(
      "Source1:          https://s3.amazonaws.com/h2o-release/h2o/",
      readLines(file.path(path, "inst/branch.txt")), "/",
      readLines(file.path(path, "inst/buildnum.txt")), "/Rjar/h2o.jar"),
    rscala = paste0(
      "Source1:          https://downloads.lightbend.com/scala/2.12.8/scala-2.12.8.tgz\n",
      "Source2:          https://github.com/sbt/sbt/releases/download/v1.2.8/sbt-1.2.8.tgz")
  ))

  # setup
  setup <- grep("%setup", tpl)
  tpl[setup] <- paste0(
    tpl[setup], switch(
      pkg,
      rscala = " -a 1 -a 2"
    ), "\n", switch(
      pkg,
      rscala = paste(
        "mkdir %{packname}/inst/dependencies",
        "mv scala* %{packname}/inst/dependencies/scala",
        "mv sbt* %{packname}/inst/dependencies/sbt", sep="\n"),
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
      nws=, OpenMx=, irace=, configr=, goldi= paste(
        "find %{packname}/inst -type f -exec",
        "sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \\;"),
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
        "sed -Ei 's@/path/to/Rscript@/usr/bin/Rscript@g' {} \\;")
    )
  )

  # install
  install <- grep("%install", tpl)
  tpl[install] <- paste0(tpl[install], "\n", switch(
    pkg,
    rPython = "export RPYTHON_PYTHON_VERSION=3",
    Rmpi = "%{_openmpi_load}"
  ))
  install <- grep("CMD INSTALL", tpl)
  tpl[install] <- paste0(tpl[install], switch(
    pkg,
    udunits2 = "\\\n  --configure-args='--with-udunits2-include=/usr/include/udunits2'"
  ))

  # other
  if (pkg %in% c("rtweet", "gunit", "ggasym", "facerec")) system(paste(
    "sed -i 's/magrittr (>= 1.5.0)/magrittr (>= 1.5)/g'", file.path(path, "DESCRIPTION")))
  if (pkg %in% "abstractr") system(paste(
    "sed -i 's/gridExtra (>= 2.3.0)/gridExtra (>= 2.3)/g'", file.path(path, "DESCRIPTION")))
  if (pkg %in% "cNORM") system(paste(
    "sed -i 's/leaps (>= 3.0.0)/leaps (>= 3.0)/g'", file.path(path, "DESCRIPTION")))
  if (pkg %in% "imgrec") system(paste(
    "sed -i 's/jsonlite (>= 1.6.0)/jsonlite (>= 1.6)/g'", file.path(path, "DESCRIPTION")))
  if (pkg %in% "facerec") system(paste(
    "sed -i 's/jsonlite (>= 1.5.0)/jsonlite (>= 1.5)/g'", file.path(path, "DESCRIPTION")))
  if (pkg %in% c("imgrec", "facerec")) system(paste(
    "sed -i 's/knitr (>= 1.2.0)/knitr (>= 1.2)/g'", file.path(path, "DESCRIPTION")))
  if (pkg %in% "adapr")
    unlink(file.path(path, "data"))

  tpl
}

create_spec <- function(pkg, tarfile) {
  untar(tarfile, exdir=tempdir())
  path <- file.path(tempdir(), pkg)
  tpl <- readLines(getOption("copr.tpl"))
  tpl <- pkg_exceptions(tpl, pkg, path)

  # fields
  desc <- read.dcf(file.path(path, "DESCRIPTION"))
  desc <- as.data.frame(desc, stringsAsFactors=FALSE)
  deps <- pkg_deps(desc)
  description <- strwrap(desc$Description, 75)
  files <- pkg_files(pkg, path)

  tpl <- sub("\\{\\{prefix\\}\\}", getOption("copr.prefix"), tpl)
  tpl <- sub("\\{\\{packname\\}\\}", pkg, tpl)
  tpl <- sub("\\{\\{packver\\}\\}", desc$Version, tpl)
  tpl <- sub("\\{\\{version\\}\\}", gsub("-", ".", desc$Version), tpl)
  tpl <- sub("\\{\\{summary\\}\\}", gsub("\n", "", desc$Title), tpl)
  tpl <- sub("\\{\\{license\\}\\}", desc$License, tpl)
  tpl <- sub("\\{\\{dependencies\\}\\}", paste(deps, collapse="\n"), tpl)
  tpl <- sub("\\{\\{description\\}\\}", paste(description, collapse="\n"), tpl)
  tpl <- sub("\\{\\{files\\}\\}", paste(files, collapse="\n"), tpl)

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

  tpl
}
