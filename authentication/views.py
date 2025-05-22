from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.utils import timezone
from formulario.models import TransportForm
from django.db.models import Q
from .forms import EditProfileForm, ChangePasswordForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})

@login_required
def profile(request):
    # Obtener los últimos 5 formularios del usuario
    try:
        recent_forms = TransportForm.objects.filter(
            created_by=request.user
        ).order_by('-created_at')[:5]
    except TransportForm.DoesNotExist:
        recent_forms = None
    
    context = {
        'recent_forms': recent_forms,
    }
    return render(request, 'authentication/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'authentication/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contraseña cambiada exitosamente')
            return redirect('profile')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'authentication/change_password.html', {'form': form})