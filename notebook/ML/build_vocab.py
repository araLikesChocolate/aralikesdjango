import nltk
import pickle
import argparse
from collections import Counter
from pycocotools.coco import COCO
import easydict
import time
import json

class Vocabulary(object):
    print('use Vocabulary..................................')
    """Simple vocabulary wrapper."""
    def __init__(self):
        print("Vocabulary3")
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0


    def add_word(self, word):
        if not word in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1

    def __call__(self, word):
        if not word in self.word2idx:
            return self.word2idx['<unk>']
        return self.word2idx[word]

    def __len__(self):
        return len(self.word2idx)

    def __str__(self):
        return self.word2idx



#@staticmethod
def build_vocab(json, threshold):
    """Build a simple vocabulary wrapper."""
    print('build_vocab 사용하기.......................................')
    print("build_vocab")
    coco = COCO(json)
    counter = Counter()
    ids = coco.anns.keys()
    for i, id in enumerate(ids):
        caption = str(coco.anns[id]['caption'])
        tokens = nltk.tokenize.word_tokenize(caption.lower())
        counter.update(tokens)

        if (i+1) % 1000 == 0:
            print("[{}/{}] Tokenized the captions.".format(i+1, len(ids)))

    # If the word frequency is less than 'threshold', then the word is discarded.
    words = [word for word, cnt in counter.items() if cnt >= threshold]

    # Create a vocab wrapper and add some special tokens.
    vocab = Vocabulary()
    vocab.add_word('<pad>')
    vocab.add_word('<start>')
    vocab.add_word('<end>')
    vocab.add_word('<unk>')

    # Add the words to the vocabulary.
    for i, word in enumerate(words):
        vocab.add_word(word)
    return vocab



def main(args):
    print(args)
    vocab = build_vocab(json=args.caption_path, threshold=args.threshold)
    #print(vocab)
    vocab_path = args.vocab_path

    with open(vocab_path, 'wb') as f:
        pickle.dump(vocab, f)

    print("Total vocabulary size: {}".format(len(vocab)))
    print("Saved the vocabulary wrapper to '{}'".format(vocab_path))

if __name__ == '__main__':
    args = easydict.EasyDict({
            'caption_path': 'D:/dev/django-upload-example/mysite/core/data/annotations/captions_train2014.json',
            'vocab_path': 'D:/dev/django-upload-example/mysite/core/data/vocab.pkl',
            'threshold': 4
            })
    main(args)
