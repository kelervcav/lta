from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import ContentType, Permission
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import (
    TypeGroupForm, TypeForm, DeviceForm, LocationForm
)
from .models import (
    TypeGroup, Type, Device, Location
)


# Type Group
class TypeGroupListView(LoginRequiredMixin, ListView):
    model = TypeGroup
    template_name = 'management/typegroup/typegroup_list.html'

    def get_context_data(self, **kwargs):
        context = super(TypeGroupListView, self).get_context_data(**kwargs)
        return context


@login_required
def typegroup_create(request):
    form = TypeGroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('management:typegroup_list')

    template_name = 'management/typegroup/typegroup_create.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def typegroup_edit(request, pk):
    typegroup = get_object_or_404(TypeGroup, id=pk)
    form = TypeGroupForm(request.POST or None, instance=typegroup)
    if form.is_valid():
        form.save()
        return redirect('management:typegroup_list')

    template_name = 'management/typegroup/typegroup_edit.html'
    context = {'form': form}
    return render(request, template_name, context)


# Type
class TypeListView(LoginRequiredMixin, ListView):
    model = Type
    template_name = 'management/type/type_list.html'

    def get_context_data(self, **kwargs):
        context = super(TypeListView, self).get_context_data(**kwargs)
        return context


@login_required
def type_create(request):
    form = TypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('management:type_list')

    template_name = 'management/type/type_create.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def type_edit(request, pk):
    type_id = get_object_or_404(Type, id=pk)
    form = TypeForm(request.POST or None, instance=type_id)
    if form.is_valid():
        form.save()
        return redirect('management:type_list')

    template_name = 'management/type/type_edit.html'
    context = {'form': form}
    return render(request, template_name, context)


# Device
class DeviceListView(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'management/device/device_list.html'

    def get_context_data(self, **kwargs):
        context = super(DeviceListView, self).get_context_data(**kwargs)
        return context


@login_required
def device_create(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('management:device_list')

    template_name = 'management/device/device_create.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def device_edit(request, pk):
    device = get_object_or_404(Device, id=pk)
    form = DeviceForm(request.POST or None, instance=device)
    if form.is_valid():
        form.save()
        return redirect('management:device_list')

    template_name = 'management/device/device_edit.html'
    context = {'form': form}
    return render(request, template_name, context)


# Location
class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'management/location/location_list.html'

    def get_context_data(self, **kwargs):
        context = super(LocationListView, self).get_context_data(**kwargs)
        return context


@login_required
def location_create(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('management:location_list')

    template_name = 'management/location/location_create.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def location_edit(request, pk):
    location = get_object_or_404(Location, id=pk)
    form = LocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('management:location_list')

    template_name = 'management/location/location_edit.html'
    context = {'form': form}
    return render(request, template_name, context)
