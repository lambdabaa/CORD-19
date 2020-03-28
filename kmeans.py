#!/usr/bin/env python3.7

from sklearn.cluster import KMeans
import json
import numpy as np
import os
import sys

def main():
    clusters = 10
    dirname = sys.argv[1]
    filenames = []
    X = []
    for idx, filename in enumerate(os.listdir(dirname)):
        filenames.append(filename)
        with open('%s/%s' % (dirname, filename), 'r') as f:
            X.append(np.array(json.load(f)).astype(np.float))
        sys.stderr.write('\rLoaded %d training vectors...' % idx)
    print()
    X = np.array(X)
    print('Fitting %d documents into %d clusters...' % (len(filenames), clusters), file=sys.stderr)
    model = KMeans(n_clusters=clusters, random_state=0)
    result = model.fit_predict(X)
    print('Summary', file=sys.stderr)
    print('=======', file=sys.stderr)
    for idx in range(clusters):
        print('%d: %d' % (idx, len([entry for entry in result if entry == idx])), file=sys.stderr)
    #print('file,cluster')
    #for idx, filename in enumerate(filenames):
    #    print('%s,%d' % (filename, result[idx]))

if __name__ == '__main__':
    main()
