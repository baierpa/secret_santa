from members.forms import MembersCreationForm
from django.urls import reverse_lazy
from django.views import generic

class MembersView(generic.CreateView):
    form_class = MembersCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
