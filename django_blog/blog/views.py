from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')  # Add a basic home template




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm

@login_required
def ProfileView(request):
    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect to profile page after successful update

    return render(request, 'authentication/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
