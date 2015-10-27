from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.template import RequestContext
from .models import *

@login_required
def home(request):
    return render(request, 'index.html', {})

@login_required
def upload_file(request):
    if request.method == 'POST':
        fullDocument = ''
        a = request.FILES['file']
        count = 0
        
        for line in a.readlines():
            linha = line.strip().decode('utf-8', 'ignore')
            registro = linha.split('|')
            
            if (count==0):
                nomeEmpresa = registro[6]
                Sped.objects.create(nome=nomeEmpresa)
                count=1
            else:
                pass
        
        form = UploadFileForm()
        return render(request, 'file.html', {'form':form})
    else:
        form = UploadFileForm()
        return render(request, 'file.html', {'form':form})
	