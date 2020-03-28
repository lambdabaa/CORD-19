#!/usr/bin/env python3.7

import gensim
import json
import os
import sys

def load_dataset():
    examples = []
    for idx, doc in enumerate(os.listdir('./bpe')):
        with open('./bpe/%s' % doc, 'r') as f:
            words = f.read().split()
            example = gensim.models.doc2vec.TaggedDocument(words, [doc])
            examples.append(example)
        sys.stdout.write('\rLoading text document %d...' % idx)
    print()
    return examples

def make_predictions(model):
    for idx, doc in enumerate(os.listdir('./bpe')):
        with open('./bpe/%s' % doc, 'r') as f:
            words = f.read().split()
        result = model.infer_vector(words)
        with open('./docvec/%s' % doc.split('/')[-1].replace('.bpe.txt', '.json'), 'w') as f:
            f.write(json.dumps(list(map(str, list(result)))))   
        sys.stdout.write('\rEmbedding text document %d...' % idx)

def main():
    train = load_dataset()
    model = gensim.models.doc2vec.Doc2Vec(vector_size=100, min_count=2, epochs=20)
    print('Discovering corpus vocabulary...')
    model.build_vocab(train)
    print('Building doc2vec model...')
    model.train(train, total_examples=model.corpus_count, epochs=model.epochs)
    model.save('./doc2vec.model')
    #model = gensim.models.doc2vec.Doc2Vec.load('./doc2vec.model')
    make_predictions(model)

if __name__ == '__main__':
    main()
