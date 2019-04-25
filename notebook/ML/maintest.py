import nltk
import pickle
import argparse
from collections import Counter
from pycocotools.coco import COCO
import easydict

import time
import json
#import voc
import vocabulary


args = easydict.EasyDict({
        'caption_path': 'D:/dev/django-upload-example/mysite/core/data/annotations/captions_train2014.json',
        'vocab_path': 'D:/dev/django-upload-example/mysite/core/data/vocab.pkl',
        'threshold': 4
})



vocab = vocabulary.Vocabulary.build_vocab(json=args.caption_path, threshold=args.threshold)
#vocab = voc.Vocabulary.build_vocab(json=args.caption_path, threshold=args.threshold)

vocab_path = args.vocab_path

with open(vocab_path, 'wb') as f:
    pickle.dump(vocab, f)

print("Total vocabulary size: {}".format(len(vocab)))
print("Saved the vocabulary wrapper to '{}'".format(vocab_path))
