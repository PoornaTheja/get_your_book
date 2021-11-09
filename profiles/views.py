from django.shortcuts import render
from orders.models import order

# Create your views here.
def order_view(request):
    qs = order.objects.all()
    qs1 = qs.filter(r_status = "Placed")    
    qs2 = qs.filter(r_status = "Using")    
    qs3 = qs.filter(r_status = "Returned")

    # print(qs1, qs2, qs3)

    return render(request, "profiles/profile.html", {"qs1":qs1, "qs2":qs2, "qs3":qs3})