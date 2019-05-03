from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

import subprocess
from subprocess import Popen, PIPE

import torch
import matplotlib.pyplot as plt
import numpy as np
import argparse
import pickle
import os
from torchvision import transforms


from .model import EncoderCNN, DecoderRNN
from PIL import Image
import easydict
import sys

import nltk
import pickle
import argparse
from collections import Counter
from pycocotools.coco import COCO
import easydict
import time
import json, datetime
from . import voc
from .models import Data, Member
from django.http import HttpResponse
from api.views import insertView

#from .build_vocab import Vocabulary
sys.modules["voc"] = voc
#sys.modules['Vocabulary'] = Vocabulary
#import pickleversion
#from django.views.decorators.csrf import csrf_exempt

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_image(image_path, transform=None):
    # console.log('########### image path ################# -- ',image_path)
    image = Image.open(image_path)
    image = image.resize([224, 224], Image.LANCZOS)
    if transform is not None:
        image = transform(image).unsqueeze(0)

    return image

def main(args):
    # Image preprocessing
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406),
                             (0.229, 0.224, 0.225))])
    print('main 호출')
    # Load vocabulary wrapper
    print("파일정보:", args["vocab_path"])

    # aa = Vocabulary()
    # print("Vocabulary:", aa)



    with open(args.vocab_path, "rb") as f:
    #vocab = pickle.load(open('D:/dev/django-upload-example/mysite/core/data/vocab.pkl','r', encoding="latin1"))
        #print("파일열기:", f)
        # import pickletools
        # pickletools.dis(f)

        vocab=pickle.load(f)
        #vocab = pickle.load(f)
            #vocab = f.readlines()
            #print(vocab)

    # print('pickle 열기')
    # Build models
    encoder = EncoderCNN(args.embed_size).eval()  # eval mode (batchnorm uses moving mean/variance)
    decoder = DecoderRNN(args.embed_size, args.hidden_size, len(vocab), args.num_layers)
    encoder = encoder.to(device)
    decoder = decoder.to(device)

    # Load the trained model parameters
    encoder.load_state_dict(torch.load(args.encoder_path))
    decoder.load_state_dict(torch.load(args.decoder_path))

    # Prepare an image
    image = load_image(args.image, transform)
    print('load_image_image....')
    image_tensor = image.to(device)
    # print('loadimage image tensor',image_tensor)

    # Generate an caption from the image
    feature = encoder(image_tensor)
    # print('image_tensor encoder feartures',feature)
    sampled_ids = decoder.sample(feature)
    sampled_ids = sampled_ids[0].cpu().numpy()          # (1, max_seq_length) -> (max_seq_length)

    # Convert word_ids to words
    sampled_caption = []
    # print(sampled_caption)
    # print('sampled_ids:', sampled_ids)
    sentence = []
    for word_id in sampled_ids:
        word = vocab.idx2word[word_id]
        # print(word)
        sampled_caption.append(word)
        if word == '<end>':
            break
            # sentence.append(' '.join(sampled_caption[1:-1]))
    # print("원본: ", sampled_caption)
    # print("가공: ", sampled_caption[1:-1])
    sentence.append(' '.join(sampled_caption[1:-1]))
    print(sentence)

    #Print out the image and the generated caption
    return sentence

@csrf_exempt 
def upload(request):
    try:
        if request.META['HTTP_USER_AGENT'] == 'ANDROID':
            print('\n\n######### ANDROID #########\n\n')
            pass
        elif request.session['user'] is None:
            return redirect('home')
    except KeyError:
        return redirect('home')


    # context = {}
    if request.method == 'POST':
        if request.META['HTTP_USER_AGENT'] == 'ANDROID':
            # print('\n############ ANDROID META ############   ')
            # print(request.META)
            id = request.META['HTTP_ID']
            service_type = request.META['HTTP_SERVICE_TYPE']
            publish = request.META['HTTP_PUBLISH']
            print('\n#### ANDROID ID ####   ',  id)
            print('\n#### ANDROID SERVICE_TYPE ####   ', service_type)
            print('\n### ANDROID PUBLISH ####   ', publish)
        else :
            id = request.session['user']['id']
            service_type = request.session['user']['service_type']
            publish = request.POST.get('publish')

        uploaded_file = request.FILES['image']
        extension = os.path.splitext(str(request.FILES['image']))[1]
        rename = id + '_' + str(time.strftime("%Y%m%d%H%M%S")) + extension
        fs = FileSystemStorage()
        fs.save(rename, uploaded_file)
        # context['uploaded_file'] = rename

        args = easydict.EasyDict({
                            #'image': sys.argv[1],
            'image': uploaded_file,
            'encoder_path': 'ML/models/encoder-5-1000.ckpt', # MYTEST + '/models/encoder-5-1000.ckpt'
            'decoder_path': 'ML/models/decoder-5-1000.ckpt', # MYTEST + '/models/decoder-5-1000.ckpt
            'vocab_path' : 'ML/data/vocab.pkl', #MYTEST + '/data/vocab.pkl'
            'embed_size' : 256,
            'hidden_size' : 512,
            'num_layers' : 1
            })

        sentence = main(args) #문장출력

        params = { 'id': id, 'service_type': service_type, 'publish': publish, 'rename': rename, 'sentence': sentence}

        return insertView(request, params)
        
    return render(request, 'ML/upload.html')