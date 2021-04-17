import json
import os

import boto3
from django.http import HttpResponse
from django.shortcuts import render

from core.models import CreativeLabeling, Creative


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def player(request, labeling_id):
    confidence = 85

    labeling = CreativeLabeling.objects.get(id=labeling_id)

    labeling_data = json.loads(labeling.labeling_data)

    labels = [x for x in labeling_data['Labels'] if x['Label']['Confidence'] > confidence]
    for x in labels:

        total_sec = x['Timestamp'] / 100
        minutes = int(total_sec // 60)
        seconds = int(total_sec % 60)
        x['human_time'] = "{}:{}".format(minutes, seconds)

    # context = {'labeling': labeling, 'labels': labels, 'video_url': labeling.creative.file.url}
    context = {'labeling': labeling, 'labels': labels, 'video_url': 'https://creative-tags.s3.eu-central-1.amazonaws.com/BigBuckBunny.mp4'}
    return render(request, 'core/player.tpl.html', context=context)


def creative_detail(request, creative_id):
    bucket = 'creative-tags-out-labeled'

    creative = Creative.objects.get(id=creative_id)


    session = boto3.Session()
    s3_connection = boto3.resource('s3')

    client = session.client('s3')

    bucket = s3_connection.Bucket(bucket)
    filename = os.path.basename(creative.file.name)

    imgs = []
    for key in bucket.objects.filter(Prefix='labeled-out_' + filename):
        # url = key.generate_url(expires_in=300)
        url = client.generate_presigned_url('get_object',
                                      Params={'Bucket': bucket.name, 'Key': key.key},
                                      ExpiresIn=300)
        imgs.append(url)

    context = {'creative': creative, 'video_url': 'https://creative-tags.s3.eu-central-1.amazonaws.com/BigBuckBunny.mp4', 'imgs': imgs}

    return render(request, 'core/creative.tpl.html', context=context)
