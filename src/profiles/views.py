from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import ContentType, Permission
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from profiles.forms import (
    ProfileCreationForm, EditProfileForm, AdminEditPasswordForm,
    AdminGroupForm,
)
from .utils import unique_id_generator

# Create your views here.
User = get_user_model()


class ProfileListView(LoginRequiredMixin, ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        return context


@login_required
def profile_create(request):
    form = ProfileCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        uid = User.objects.get(id=user.id)
        uid.user_id = unique_id_generator(user.id)
        uid.save()
        return redirect('/u')

    template_name = 'profiles/user_create.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def profile_edit(request, pk):
    user = get_object_or_404(User, id=pk)
    form = EditProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('/u')

    template_name = 'profiles/user_edit.html'
    context = {'form': form, 'id': pk}
    return render(request, template_name, context)


@login_required
def admin_edit_password(request, pk):
    user = get_object_or_404(User, id=pk)
    form = AdminEditPasswordForm(data=request.POST or None, user=user)
    if form.is_valid():
        form.save()
        return redirect('/u')

    template_name = 'profiles/user_admin_edit_password.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def group_create(request):
    form = AdminGroupForm(request.POST or None)
    content_types = ContentType.objects.all()
    permissions = Permission.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/u')

    template_name = 'profiles/group_create.html'
    context = {
        'form': form,
        'content_types': content_types,
        'permissions': permissions
    }
    return render(request, template_name, context)
