import os
import hashlib

from django.shortcuts import render
from django.core.context_processors import csrf

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

    context['bookmarks'] = {item.name : item.value
                            for item in bookmarks}

    context.update(csrf(request))
    return render(request, 'show.html', context)
