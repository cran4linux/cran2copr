#!/bin/bash

DEL=$(copr-cli get-package cran --name $1 --with-all-builds | jq '.builds[].id' | tail -n+2)
copr-cli delete-build $DEL

