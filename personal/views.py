from django.shortcuts import render

# Create your views here.

def index(request):
	return render (request,'personal/home.html')

#def index(request):
	#return render (request,'personal/index.html')
	
def contact(request):
	return render(request,'personal/basic.html', {'content':['www.google.com','8942121']})
