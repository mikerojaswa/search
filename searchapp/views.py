from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("SEARCH INDEX")
# Create your views here.
