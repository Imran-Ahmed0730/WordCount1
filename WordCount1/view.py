from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render (request, "homepage.html")
def count(request):
    FullText = request.GET["fun"]
    WordList = FullText.split()
    WordDictionary = {}

    for words in WordList:
        if words in WordDictionary:
            WordDictionary[words] += 1
        else:
             WordDictionary[words] = 1

    SortedWords = sorted(WordDictionary.items(), key = operator.itemgetter(1), reverse = False)

    return render(request, "Counting.html",{"Text": FullText, "WordCount" : len(WordList), "Dictionary": SortedWords })
def about (request):
    return render(request, "About.html")
