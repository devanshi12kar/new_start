from django.shortcuts import render


# Create your views here.

#def showsubs(request):
    #return render(request, 'subscribe.html', {})


#def save_subscribe(request):
    #if request.method == 'POST':
        #print(request)
    #return True

def showimg(request):
    return render(request, 'image.html', {})


