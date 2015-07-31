from django.shortcuts import render

def homepage(request):
    """Strona główna"""
    return render(request, 'pages/homepage.html')

def gui(request):
    """O interfejsie graficznym"""
    return render(request, 'pages/gui.html')
