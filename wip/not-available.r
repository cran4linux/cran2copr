source("config.r")
source("common.r")
check_copr()

pkgs <- get_copr_list()
avail <- list_available("rawhide")

pkgs[!pkgs %in% avail]
