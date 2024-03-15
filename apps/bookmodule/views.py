from django.shortcuts import render,redirect 
def index(request):
     return render(request, 'bookmodule/index.html') # rendring a template
def books(request):
     u = request.user
     return render(request, 'bookmodule/bookList.html')
     #return redirect('/')
def book(reqest,bId):
     book1 = {'id':123, 'title':'Continous Delivery','auther':'J. Humble'}
     book2 = {'id':567, 'title':'Reserving secrests','auther':'E. Eilam'}
     targetBook = None
     if book1['id'] == bId: targetBook = book1
     if book2['id'] == bId: targetBook = book2
     
     if targetBook == None: 
          return render(reqest,'bookmodule/nf.html', {'id':bId})
     context = {'book':targetBook}
     return render(reqest,'bookmodule/book.html',context)