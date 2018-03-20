from django import forms
from django.forms import ModelForm
from .models import (
    TypeGroup, Type, Device, Location
)


class TypeGroupForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5'}))

    class Meta:
        model = TypeGroup
        fields = [
            'name',
            'description'
        ]


class TypeForm(ModelForm):
    typegroup = forms.ModelChoiceField(
        queryset=TypeGroup.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5'}))

    class Meta:
        model = Type
        fields = [
            'typegroup',
            'name',
            'description'
        ]


class DeviceForm(ModelForm):
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5'}))

    class Meta:
        model = Device
        fields = [
            'type',
            'name',
            'description'
        ]


class LocationForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5'}))

    class Meta:
        model = Location
        fields = [
            'name',
            'description'
        ]
