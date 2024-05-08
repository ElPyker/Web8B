from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    context = {}
    form_class = None

    def get(self, request):
        self.context = {
            "users": User.objects.all()
        }
        return render(request, self.template_name, self.context)