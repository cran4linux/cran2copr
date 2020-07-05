utils::globalVariables(c("BUS_NAME", "OPATH", "IFACE"))

dbus_call <- function(cmd, pkgs) {
  source(system.file("service/dbus-paths", package="CoprManager"))

  args <- c("list", "--no-pager")
  out <- suppressWarnings(system2("busctl", args, stdout=TRUE, stderr=TRUE))
  if (!any(grepl(BUS_NAME, out)))
    stop("CoprManager service not found")

  args <- c("call", "--timeout=1h", BUS_NAME, OPATH, IFACE,
            cmd, "ias", Sys.getpid(), length(pkgs), pkgs)
  out <- suppressWarnings(system2("busctl", args, stdout=TRUE, stderr=TRUE))

  if (!length(out))
    return(out)
  status <- attr(out, "status")
  if (!is.null(status) && status != 0)
    stop(out)
  cat("\n")

  out <- gsub('"', "", out)
  out <- strsplit(out, " ")[[1]][-(1:2)]
  invisible(out)
}

#' Install Binary Packages from Copr
#'
#' Talk to the accompanying D-Bus service to download and install or remove
#'  packages from Copr repositories.
#'
#' @param pkgs character vector of CRAN names of packages.
#'
#' @return Invisibly, a character vector of the names of packages not available.
#'
#' @export
install_copr <- function(pkgs) dbus_call("install", pkgs)

#' @name install_copr
#' @export
remove_copr <- function(pkgs) dbus_call("remove", pkgs)
