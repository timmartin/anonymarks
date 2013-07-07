import os
import hashlib

from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

from boto.dynamodb2.table import Table

bookmarks_table = Table('bookmarks')

def home(request):
    context = {}
    return render(request, 'index.html', context)

def show(request):
    context = {}

    hash_obj = hashlib.sha1()
    hash_obj.update(request.POST['passphrase'])

    bookmarks = bookmarks_table.query(hash__eq=hash_obj.hexdigest())

    context['bookmarks'] = {item['name'] : item['url']
                            for item in bookmarks}
    context['hash'] = hash_obj.hexdigest()

    context.update(csrf(request))
    return render(request, 'show.html', context)

def store(request):
    bookmarks_table.put_item(data={
            'hash' : request.POST['hash'],
            'name' : request.POST['name'],
            'url' : request.POST['url']})

    return HttpResponseRedirect('/')
