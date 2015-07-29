from django.shortcuts import render

def homepage(request):
    return render(request, 'pages/homepage.html')

def gui(request):
    return render(request, 'pages/gui.html')
