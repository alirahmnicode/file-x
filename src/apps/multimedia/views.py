from django.shortcuts import render
from .models import File

# Create your views here.
def f(request):
    a = File.objects.all()
    for f in a:
        print(f.file.url)