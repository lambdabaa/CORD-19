#!/usr/bin/env bash

cd ./docs
ls | xargs cat > ../corpus.txt
cd ..
du -h corpus.txt
subword-nmt learn-bpe -s 10000 < corpus.txt > encoding.txt
cat encoding.txt
mkdir -p ./bpe
mkdir -p ./vec
mkdir -p ./docvec
