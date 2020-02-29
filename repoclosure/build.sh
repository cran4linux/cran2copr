#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <tag1> <tag2> ..."
    exit 0
fi

for TAG in $@; do
    podman build --tag iucar/cran/repoclosure:${TAG} --build-arg TAG=${TAG} .
done
