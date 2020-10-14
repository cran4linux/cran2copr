#!/bin/bash

PKG=$1
[[ $PKG == R-* ]] || PKG="R-CRAN-$PKG"

DEL=$(copr-cli get-package cran --name $PKG --with-all-builds | jq '.builds[].id' | tail -n+2)
copr-cli delete-build $DEL
