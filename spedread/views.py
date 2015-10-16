from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.template import RequestContext

@login_required
def home(request):
    return render(request, 'index.html', {})

@login_required
def upload_file(request):
	if request.method == 'POST':
		
		a = request.FILES['file']
		for line in a.readlines():
			print (line)
		return render(request, 'index.html', {})
	else:
		form = UploadFileForm()
		return render(request, 'index.html', {})
	