from django.shortcuts import render, render_to_response
from .forms import UploadFileForm
from django.template import RequestContext

# Create your views here.

def upload_file(request):
	if request.method == 'POST':
		
		a = request.FILES['file']
		for line in a.readlines():
			print (line)
		return render(request, 'index.html', {})
	else:
		form = UploadFileForm()
		return render(request, 'index.html', {'form': form})
	