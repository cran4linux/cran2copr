#' Enable/Disable Copr Package Manager
#'
#' Functions to enable or disable the integration of \code{\link{install_copr}}
#' into \code{\link{install.packages}}. When enabled, packages are installed
#' transparently from Copr if available, and from CRAN if not.
#'
#' @export
enable <- function() {
  expr <- quote(if (!is.null(repos)) pkgs <- CoprManager::install_copr(pkgs))
  trace(utils::install.packages, expr, print=FALSE)
  invisible()
}

#' @name enable
#' @export
disable <- function() {
  untrace(utils::install.packages)
  invisible()
}
