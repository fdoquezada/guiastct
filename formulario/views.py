from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TransportForm
from .forms import TransportFormForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def transport_form_list(request):
    forms = TransportForm.objects.all()
    return render(request, 'formulario/transport_form_list.html', {'forms': forms})

@login_required
def transport_form_create(request):
    if request.method == 'POST':
        form = TransportFormForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulario creado exitosamente')
            return redirect('transport_form_list')
    else:
        form = TransportFormForm()
    return render(request, 'formulario/transport_form_create.html', {'form': form})

@login_required
def transport_form_edit(request, pk):
    form = get_object_or_404(TransportForm, pk=pk)
    if request.method == 'POST':
        form = TransportFormForm(request.POST, request.FILES, instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulario actualizado exitosamente')
            return redirect('transport_form_list')
    else:
        form = TransportFormForm(instance=form)
    return render(request, 'formulario/transport_form_edit.html', {'form': form})

@login_required
def transport_form_delete(request, pk):
    form = get_object_or_404(TransportForm, pk=pk)
    if request.method == 'POST':
        form.delete()
        messages.success(request, 'Formulario eliminado exitosamente')
        return redirect('transport_form_list')
    return render(request, 'formulario/transport_form_delete.html', {'form': form})
