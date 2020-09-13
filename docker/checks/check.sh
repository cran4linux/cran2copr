#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <tag>"
    exit 0
fi

podman run --rm iucar/cran/repoclosure:$1
