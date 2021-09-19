#! /bin/sh
set -ex

VERSION=$1
LABEL=$2

echo "$TOKEN" | docker login $REGISTRY -u $USER --password-stdin
docker build . --pull --build-arg VERSION=$VERSION -t $REGISTRY/$USER/$IMAGE:$LABEL
docker push $REGISTRY/$USER/$IMAGE:$LABEL
