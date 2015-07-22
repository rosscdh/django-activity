# -*- coding: utf-8 -*-
from django.views.generic import ListView

from m1_tools.apps.tools.mixins import LoginRequiredMixin

from .models import Action


class ActivityListView(LoginRequiredMixin,
                       ListView):
    model = Action
    template_name = 'activity/activity_list.html'
    paginate_by = 15
