from django.shortcuts import render

def showMain(request):

    
    return render(request, 'main.html')

def showCatalog(request):


    return render(request, 'catalog.html')

def showFeedback(request):


    return render(request, 'feedback.html')

def showAboutus(request):


    return render(request, 'aboutus.html')