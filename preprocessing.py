#!/usr/bin/env python3.7

import ijson
import json
import os
import subprocess
import sys

def mkdirp(dirname):
    subprocess.call(['mkdir', '-p', dirname])

def extract_text():
    docs = (os.path.join(dirname, filename)
        for dirname, _, filenames in os.walk('./CORD-19-research-challenge')
        for filename in filenames
        if filename.endswith('.json'))
    for idx, doc in enumerate(docs):
        with open(doc, 'r') as f:
            items = ijson.kvitems(f, '')
            sections = (v for k, v in items if k == 'abstract' or k == 'body_text')
            chunks = (chunk['text'] for section in sections for chunk in section)
            text = '\n'.join(chunks)
        dest = './docs/%s' % doc.split('/')[-1].replace('.json', '.txt')
        with open(dest, 'w') as f:
            f.write(text)
        sys.stdout.write('\rWrote %d text documents!' % idx)

def extract_titles():
    docs = (os.path.join(dirname, filename)
        for dirname, _, filenames in os.walk('./CORD-19-research-challenge')
        for filename in filenames
        if filename.endswith('.json'))
    print('file,title')
    for idx, doc in enumerate(docs):
        with open(doc, 'r') as f:
            items = ijson.kvitems(f, '')
            sections = [v for k, v in items if k == 'metadata']
            titles = (section['title'] for section in sections)
            text = '\n'.join(titles)
        print('%s,%s' % (doc.split('/')[-1], text))

def apply_bpe():
    for idx, doc in enumerate(os.listdir('./docs')):
        dest = doc.split('/')[-1].replace('.txt', '.bpe.txt')
        subprocess.call(['subword-nmt apply-bpe -c encoding.txt --input ./docs/%s --output ./bpe/%s' % (doc, dest)], shell=True)
        sys.stdout.write('\rRan BPE on %d text documents!' % (idx + 1))

def main():
    #mkdirp('./docs')
    #extract_text()
    extract_titles()
    #apply_bpe()

if __name__ == '__main__':
    main()
