from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'judging/index.html')

def poster(request):
    return render(request, 'judging/poster.html')

def oral(request):
    return render(request, 'judging/oral.html')