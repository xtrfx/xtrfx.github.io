#!/usr/bin/env bash

stamp=$(date +"%Y-%m-%d")
text=$1

filename="$stamp-$text.md"
touch ./$filename
