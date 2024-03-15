from django.shortcuts import render 
def index(request):
     return render(request, 'bookmodule/index.html') # rendring a template
