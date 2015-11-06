# encoding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from django.views.decorators.csrf import *
from models import * 

import json
# Create your views here.

def index(request):
	if request.method == 'GET':
		allbook = Book.objects.all()
		content = {"active": "index", "books": allbook}
		return render_to_response('index.html', content)
"""
新增图书
"""
def addBook(request):
	if request.method == 'GET':
		content = {"active": "addbook"}
		return render_to_response('addbook.html', content)

	else:

		mISBN = request.POST.get('ISBN', '')
		mTitle = request.POST.get('Title', '')
		mAuthor = request.POST.get('Author', '')
		mPublisher = request.POST.get('Publisher', '')
		mPublishDate = request.POST.get('PublishDate', '')
		mPrice = request.POST.get('Price', '')

		if len(Book.objects.filter(ISBN = mISBN)) != 0 :
			data = {"status": 0}
		else :
			newbook = Book(
				ISBN = mISBN,
				Title = mTitle,
				Author = Author.objects.get_or_create(Name = mAuthor)[0],
				Publisher = mPublisher,
				PublishDate = mPublishDate,
				Price = mPrice
				)
			newbook.save()
			data = {"status": 1}

		return HttpResponse(json.dumps(data, ensure_ascii=False))

"""
删除图书
"""		
@csrf_exempt
def deleteBook(request):
	if request.method == 'POST':
		ISBN = request.POST.get('ISBN')
		book = Book.objects.get(ISBN = ISBN)
		book.delete()
		data = {"status": 1}
		return HttpResponse(json.dumps(data, ensure_ascii=False))

"""
更新图书
"""
@csrf_exempt
def updateBook(request, mISBN=-1):
	if request.method == 'GET':
		updatebook = Book.objects.get(ISBN = mISBN)
		content = {"book": updatebook}
		return render_to_response('update.html', content)

	if request.method == 'POST':
		mISBN = request.POST.get('ISBN', '')
		mTitle = request.POST.get('Title', '')
		mAuthor = request.POST.get('Author', '')
		mPublisher = request.POST.get('Publisher', '')
		mPublishDate = request.POST.get('PublishDate', '')
		mPrice = request.POST.get('Price', '')

		newbook = Book(
			ISBN = mISBN,
			Title = mTitle,
			Author = Author.objects.get_or_create(Name = mAuthor)[0],
			Publisher = mPublisher,
			PublishDate = mPublishDate,
			Price = mPrice
			)

		newbook.save()
		data = {"status": 1}

		return HttpResponse(json.dumps(data, ensure_ascii=False))
"""
图书详细信息
"""
def listBook(request, mISBN):
	if request.method == 'GET':
		updatebook = Book.objects.get(ISBN = mISBN)
		content = {"book": updatebook}
		return render_to_response('list.html', content)
		
"""
查询该作者的所有图书
"""
def queryAuthor(request, mAuthorName):
	if request.method == 'GET':
		try:
			searchbook = Book.objects.filter(Author = Author.objects.get(Name = mAuthorName))
			content = {"books": searchbook}
		except:
			content = {"books": ""}
		return render_to_response('search.html', content)
