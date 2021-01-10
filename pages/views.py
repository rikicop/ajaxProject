#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect,HttpResponse
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
#from django.views.generic.edit import CreateView
#from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm,SumForm



import pandas as pd
import mimetypes

def contact_form(request):
    #El objeto del modelo contact
    #para despues pasarlo con Contact.objects
    contact=Contact()
    df = pd.DataFrame(list(Contact.objects.all().values()))
    df.to_csv("test_project/media/inv_final.csv",index=False)

    #Este es simplemente formulario
    form = ContactForm()
    result = 0
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            result = name + " : " + email     
            form.save()
            df = pd.DataFrame(list(Contact.objects.all().values()))
            df.to_csv("test_project/media/inv_final.csv",index=False)
            return JsonResponse({"name":name,"email":email,"result":result}, status=200)
           
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "contact.html", {"form": form  })

def edit_contact(request):
    if request.method == "POST":
        #contactos=Contact.objects.all()
        fbuscar = request.POST.get('fbuscar')
        buscar = Contact.objects.filter(name__icontains = fbuscar)
        #context = {'buscar': buscar }
        #context= {'contactos': contactos,'buscar':buscar }
        return render(request,'edit_contact.html',{'buscar' : buscar})

    return render(request,'edit_contact.html')
    
   
    
    

def sum_form(request):
    sform = SumForm()
    result = 0
    if request.method == "POST" and request.is_ajax():
        sform = SumForm(request.POST)
        if sform.is_valid():
            first = sform.cleaned_data['first']
            second = sform.cleaned_data['second']
            result = first + second
            sform.save()
            return JsonResponse({"result":result}, status=200)
            #return render(request, "contact.html", {"result": result})
        else:
            errors = sform.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "sum.html", {"sform": sform  })


def download_file(request):
    # fill these variables with real values
    #fl_path = 'calculadora/media/inv_final.csv'
    fl_path = 'test_project/media/inv_final.csv'
    filename = 'inv_final.csv'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response






# @login_required
# def home(request):
#     return render(request, 'home.html')
#
#
# class SignUpView(CreateView):
#     template_name = 'signup.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         valid = super().form_valid(form)
#         login(self.request, self.object)
#         return valid
#
#
# def validate_username(request):
#     """Check username availability"""
#     username = request.GET.get('username', None)
#     response = {
#         'is_taken': User.objects.filter(username__iexact=username).exists()
#     }
#     return JsonResponse(response)
