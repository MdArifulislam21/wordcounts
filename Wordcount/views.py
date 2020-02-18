from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')


def count(request):
	fulltext = request.GET['fulltext']

	wordlist  = fulltext.split()
	wordcountdict = {}
	for word in wordlist:
		if word in wordcountdict:
			# increase
			wordcountdict[word] +=1
		else:
			#add to the dictionary 
			wordcountdict[word] = 1
	sorted_word = sorted(wordcountdict.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sorted_word }) 

def about(request):
	return render(request, 'about.html')