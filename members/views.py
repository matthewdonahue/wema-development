from django.shortcuts import (
    render,
    redirect,
    HttpResponseRedirect
)
from members.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:home'))
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'members/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'members/profile.html', args)
         
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('members:view_profile'))
        else:
            print(form.errors)
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'members/edit_profile.html', args)

def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('members:view_profile'))
        else:
            return redirect(reverse('members:change_password'))

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'members/change_password.html', args)

        