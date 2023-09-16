from django.shortcuts import render, redirect
from .models import PrepositionModel
from .forms import PrepositionModelForm


def preposition_upload(request):
    if request.method == 'POST':
        form = PrepositionModelForm(request.POST, request.FILES)
        PrepositionModel.objects.create(
            text=request.POST.get('text'),
            file=request.FILES.get('file')
        )
    else:
        form = PrepositionModelForm()

    return render(request, 'preposition/preposition_list.html', {'form': form})
