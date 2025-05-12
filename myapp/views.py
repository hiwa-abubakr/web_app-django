from django.shortcuts import render

def home(request):
  context={}
  return render(request,"myapp/home.html",context)

def overview(request):
    return render(request, "myapp/overview.html")

def learning(request):
    return render(request, "myapp/learning.html")