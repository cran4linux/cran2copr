#! /bin/sh
set -ex

VERSION=$1
LABEL=$2
IMAGE=$(echo $IMAGE | tr '[A-Z]' '[a-z]')

echo "$TOKEN" | docker login $REGISTRY -u $USER --password-stdin
docker build . --pull --build-arg VERSION=$VERSION -t $REGISTRY/$IMAGE:$LABEL
docker push $REGISTRY/$IMAGE:$LABEL
