from django.shortcuts import render,redirect 
def index(request):
     return render(request, 'bookmodule/index.html') # rendring a template
def names(request):
     u = request.user
     return render(request, 'bookmodule/namesList.html')
     #return redirect('/')