from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Alert, Comment, Category, Profile
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class AlertListView(ListView):
    model = Alert
    context_object_name = 'alert'
    template_name = 'app/alert_list.html'

class AlertDetailView(DetailView):
    model = Alert
    context_object_name = 'alert'
    template_name = 'app/alert_detail.html'
    def get_success_url(self):
        # Redirect to the detail page of the updated alert
        return reverse_lazy('alert_detail', args=[self.object.pk])

class AlertCreateView(CreateView):
    model = Alert
    fields = ['title', 'message', 'valid_until']  # Use fields from the Alert model
    template_name = 'app/alert_create.html'

    def form_valid(self, form):
        # Assign the logged-in user as the issuer of the alert
        form.instance.issued_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('alert_detail', kwargs={'pk': self.object.pk})

class AlertUpdateView(UpdateView):
    model = Alert
    fields = ['title', 'message', 'valid_until']  # Use fields from the Alert model
    template_name = 'app/alert_update.html'

    def get_success_url(self):
        # Redirect to the detail page of the updated alert
        return reverse_lazy('alert_detail', args=[self.object.pk])

class AlertDeleteView(DeleteView):
    model = Alert
    template_name = 'app/alert_delete.html'
    success_url = reverse_lazy('alert')