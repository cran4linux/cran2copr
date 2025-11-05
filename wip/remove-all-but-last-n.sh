#!/bin/bash

PKG="$1"
N="${2:-1}"
[[ $PKG == R-* ]] || PKG="R-CRAN-$PKG"

DEL=$(copr-cli get-package cran --name $PKG --with-all-builds | jq '.builds[].id' | tail -n+$(($N+1)))
copr-cli delete-build $DEL
