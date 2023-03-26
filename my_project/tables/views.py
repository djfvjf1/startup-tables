from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)   
    else:
        form = NameForm()
    return render(request, 'form/form.html', {'form': form})
