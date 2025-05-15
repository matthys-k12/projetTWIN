from django.shortcuts import render, redirect
from .forms import InscriptionForm
from .models import Inscription

def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            inscription = form.save()
            return redirect('confirmation', numero_inscription=inscription.numero_inscription)
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})

def confirmation_view(request, numero_inscription):
    inscription = Inscription.objects.get(numero_inscription=numero_inscription)
    return render(request, 'confirmation.html', {'inscription': inscription})
