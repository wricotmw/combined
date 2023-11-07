from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Dances
from .forms import DancesForm

# Create your views here.
#def line(request):
#	return render(request, 'e_newline/line.html', {})

def line(request):
    #return HttpResponse("Hello, world. You're at the e_newline index.")
    dances_list = Dances.objects.all().order_by('-id')
    latest_list= dances_list[0:5]


    
    return render(request, 'e_newline/line.html',{'latest_list':latest_list})


def linedances(request):

    beg_list = Dances.objects.filter(level="beg").order_by('name')
    imp_list = Dances.objects.filter(level="imp").order_by('name')
    int_list = Dances.objects.filter(level="int").order_by('name')

    return render(request, 'e_newline/all_dances.html',{'beg_list':beg_list, 'imp_list': imp_list, 'int_list': int_list})    


def search_dance(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        dance_result = Dances.objects.filter(name__contains= searched)
        return render(request, 'e_newline/Search_dance.html',{'searched':searched, 'dance_result':dance_result})

    else:

        return render(request, 'e_newline/Search_dance.html',{})

def ammend_dance(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        dance_result = Dances.objects.filter(name__contains= searched)
        return render(request, 'e_newline/ammend_dance.html',{'searched':searched, 'dance_result':dance_result})

    else:

        return render(request, 'e_newline/ammend_dance.html',{})

def ammendment(request, dances_id):
    
    result = Dances.objects.get(pk=dances_id )

    form = DancesForm(request.POST or None, instance=result)
    
    if form.is_valid():
        form.save()
        return redirect('ammend_dance')




    return render(request, 'e_newline/ammendment.html', { 'result':result, 'form':form})



def video_test(request, id, name):
   
    vid_id= id

    d_name = name
    return render(request, 'e_newline/video_test.html',{'vid_id':vid_id, 'd_name':d_name})

def add_dance(request):

    submitted= False
    if request.method== "POST":
        form = DancesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_dance?submitted=True')
    else:
        form = DancesForm
        if 'submitted' in request.GET:
            submitted=True
        return render(request, 'e_newline/dance_add.html',{'form':form, 'submitted':submitted})

#
# Create your views here.

