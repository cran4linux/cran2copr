#!/bin/bash

set -e

SPEC=$1
PKGNAME=$(echo $(basename ${SPEC%.*}) | sed -e "s/^R-CRAN-//")
VERSION=$(rpm --specfile $SPEC --qf "%{version}\n" | tail -n1)
SRCFILE=${PKGNAME}_${VERSION}.tar.gz
RESULTS=results_${PKGNAME}
MOCKCMD="mock -r mock.cfg --resultdir $RESULTS"

spectool -g $SPEC
rm -rf $RESULTS
$MOCKCMD --buildsrpm --spec $SPEC --sources $SRCFILE
$MOCKCMD --rebuild $RESULTS/*.src.rpm
