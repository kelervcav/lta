from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import ContentType, Permission
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Review


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/reviews_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        return context
