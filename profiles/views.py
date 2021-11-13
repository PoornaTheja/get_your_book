from django.shortcuts import render
from orders.models import order
from .forms import register_form
from .models import user
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your views here.
def order_view(request):
    qs = order.objects.all()
    qs1 = qs.filter(r_status = "Placed")    
    qs2 = qs.filter(r_status = "Using")    
    qs3 = qs.filter(r_status = "Returned")

    no_use, no_ret = 1, 1
    if len(qs2):
        no_use = 0
    if len(qs3):
        no_ret = 0

    temp = 50

    # print(qs1, qs2, qs3)
    us = user.objects.all().filter(username = request.user).first()
    # print("^^^^^^^^^^^^^^^^^^")
    # print(type(us))

    return render(request, "profiles/profile.html", 
    {"qs1":qs1, "qs2":qs2, "qs3":qs3, "no_use":no_use, "no_ret":no_ret, "test":temp, "u":us})

# def register_view(request):
#     form = register_form(request.POST or None)
#     if form.is_valid():
#         data = form.cleaned_data
#         user.objects.create(username=data.get("username"), email=data.get("email"), pswd=data.get("pswd"))

#         form.save()
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # UserProfile.objects.create(user=instance)
        # EmailAdress.objects.create(user_id = instance.id, user_email=instance.email)
        # print("*******************")
        # print(instance, instance.username, instance.password)
        # print("!!!!!!!!!!!!!!!!!!!")
        # print(sender)
        # try:
        #     print("$$$$$$", instance.email)
        # except:
        #     print("^^^^^^")

        user.objects.create(username = instance.username, email = instance.email, pswd = instance.password)