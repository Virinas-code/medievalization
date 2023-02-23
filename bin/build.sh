#!/usr/bin/bash

for f in ui/*/css/* ; do
    mkdir -p "$(dirname "public/$f")" && cp "$f" "public/$f"
done

cd ui

tsc