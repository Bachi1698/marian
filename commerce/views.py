from django.shortcuts import render

# Create your views here.
def rooms(request):
    datas = {

    }
    return render(request,'pages/rooms.html',datas)
