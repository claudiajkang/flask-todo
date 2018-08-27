#!/usr/bin/env bash

PROJ=FLASK-TODO
# https://stackoverflow.com/questions/2264428/how-to-convert-a-string-to-lower-case-in-bash
BUILD_PROJ=$(echo "${PROJ}" | tr '[:upper:]' '[:lower:]')

PROJ_PATH=$(pwd)
DOCKERFILE_PATH=${PROJ_PATH}/dockers/Dockerfile

docker build --tag ${BUILD_PROJ} \
--build-arg proj=${PROJ} \
-f ${DOCKERFILE_PATH} \
${PROJ_PATH}

docker run --name ${PROJ} \
-p 5555:5555 \
-d ${BUILD_PROJ}
