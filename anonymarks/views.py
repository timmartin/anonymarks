import hashlib

import boto3
from boto3.dynamodb.conditions import Key
from django.shortcuts import render

dynamodb = boto3.resource('dynamodb')
bookmarks_table = dynamodb.Table('bookmarks')

def home(request):
    context = {}
    return render(request, 'index.html', context)

def show(request):
    context = {}

    hash_obj = hashlib.sha1()
    hash_obj.update(request.POST['passphrase'])

    bookmarks = bookmarks_table.query(
        KeyConditionExpression=Key('hash').eq(hash_obj.hexdigest())
    )

    context['bookmarks'] = {item['name'] : item['url']
                            for item in bookmarks}
    context['hash'] = hash_obj.hexdigest()

    return render(request, 'show.html', context)

def store(request):
    context = {}

    bookmarks_table.put_item(
        Item={
            'hash' : request.POST['hash'],
            'name' : request.POST['name'],
            'url' : request.POST['url']
        }
    )

    bookmarks = bookmarks_table.query(
        KeyConditionExpression=Key('hash').eq(request.POST['hash'])
    )

    context['bookmarks'] = {item['name'] : item['url']
                            for item in bookmarks}
    context['hash'] = request.POST['hash']
    return render(request, 'show.html', context)

def delete(request):
    context = {}

    bookmarks_table.delete_item(hash=request.POST['hash'],
                                name=request.POST['name'])

    bookmarks = bookmarks_table.query(
        KeyConditionExpression=Key('hash').eq(request.POST['hash'])
    )

    context['bookmarks'] = {item['name'] : item['url']
                            for item in bookmarks}
    context['hash'] = request.POST['hash']
    return render(request, 'show.html', context)
