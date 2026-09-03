from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def home(request):
    return render(request, 'usuarios/home.html')