from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect, Http404

# registering the users
class RegisterView(View):
    def get(self, request): #this takes in the user request for the first time, so it loads an empty form
        form = UserRegisterForm()
        #form is a context. Variables that we can access indise of our forms
        #by adding context, we can render the form in the template.
        return render(request, "user/register.html", {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST) #takes data from form fields and save it to the database

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('index')
        else:
            return redirect('index')