#!/bin/bash

DIR_BASE=$(cd $(dirname ${0}); pwd)
ENV=""

while read LINE
do
  ENV+="${LINE}"
  ENV+=" "
done<${DIR_BASE}/env.conf

echo ${ENV}