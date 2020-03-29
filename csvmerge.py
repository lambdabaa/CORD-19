#!/usr/bin/env python3.7

import csv
import sys

def csvmerge():
    with open('clusters.csv', 'r') as f:
        clusters = list(csv.reader(f))[1:]
    with open('titles.csv', 'r') as f:
        titles = list(csv.reader(f))[1:]
    docs = {}
    for cluster in clusters:
        docs[cluster[0]] = {'cluster': cluster[1], 'title': ''}
    for title in titles:
        docs[title[0]]['title'] = title[1]
    print('file,title,cluster')
    for filename, doc in docs.items():
        print('%s,%s,%s' % (filename, doc['title'], doc['cluster']))

def write_titles_by_cluster():
    with open('docs.csv', 'r') as f:
        docs = [doc for doc in list(csv.reader(f))[1:] if len(doc) == 3]
        clusters = {doc[2] for doc in docs if doc[2].isdigit()}
        for cluster in clusters:
            with open('./clusters/%s.csv' % cluster, 'w') as f:
                f.write('file,title\n')
                for doc in docs:
                    if len(doc[1]) > 0 and doc[2] == cluster:
                        f.write('%s,%s\n' % (doc[0],doc[1].replace('"', '')))

def main():
    csv.field_size_limit(sys.maxsize)
    #csvmerge()
    write_titles_by_cluster()


if __name__ == '__main__':
    main()
