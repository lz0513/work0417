from django.http import HttpResponse

def index(request):
	print('sss')
	return HttpResponse('index')
