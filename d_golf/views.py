
from django.shortcuts import render
from .models import Golfer, FiveScores
from .forms import GolferForm, ScoreForm
from django.http import HttpResponseRedirect
from .utils import initial, update
# Create your views here.
def golf(request):
	return render(request, 'd_golf/golf.html', {})

def add_golfer(request):
	submitted = False
	if request.method == 'POST':
		form = GolferForm(request.POST)
		if form.is_valid():
			 
			#g_name= request.POST.get('name')
			
			golfer_data = form.save(commit = True)

			
			x = golfer_data.pk
			initial(x)
			
			return HttpResponseRedirect('/d_golf/add_golfer/?submitted=True')
			
	else:
		form = GolferForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 
			'd_golf/add_golfer.html',
			{'form': form, 'submitted': submitted}
			)

def add_scores(request):
	submitted = False
	if request.method == 'POST':
		form = ScoreForm(request.POST)
		if form.is_valid():
			golfer_id = form.save()

			y = golfer_id.name
			z = golfer_id.score
			x = golfer_id.round_no


			update(y, z, x)

			return HttpResponseRedirect('/d_golf/add_scores/?submitted=True')
	else:
		form = ScoreForm()
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 
		'd_golf/add_scores.html',
		{'form': form, 'submitted': submitted}
		)


