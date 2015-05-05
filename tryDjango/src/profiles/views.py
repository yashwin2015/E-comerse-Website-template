from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	context = locals()
	template = 'home.html'
	return render(request, template, context)

def about(request):
	context = locals()
	template = 'about.html'
	return render(request, template, context)

@login_required
def profile(request):
	user= request.user
	contet = {'user': user}
	context = locals()
	template = 'profile.html'
	return render(request, template, context)