from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# from django.contrib.messages import constants as messages
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable1': 'Dhanraj is great',
        'variable2': 'Dhanraj is awesome',
    }
    messages.success(request, "This is a test message.")
    # return HttpResponse("this is homepage")
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse("this is about page")
    return render(request, 'about.html', )

def service(request):
    # return HttpResponse("this is service page")
    return render(request, 'services.html', )

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "Your message has been sent!")
        # print(name, email, phone, desc)
        
    return render(request, 'contact.html', )

# from django.shortcuts import render

# def home(request):
#     return render(request, 'index.html')


# from django.shortcuts import render
# from home.models import Contact

# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         desc = request.POST.get("desc")

#         contact = Contact(
#             name=name,
#             email=email,
#             phone=phone,
#             desc=desc
#         )
#         contact.save()

#     return render(request, "contact.html")