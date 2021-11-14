from django.shortcuts import render
from .models import book
from comments.models import comment
from .forms import search_form, review_form
from collections import deque
from profiles.models import user
from orders.models import order
from datetime import datetime
from pytz import timezone

# print("****************")
# print(datetime.now())

# Create your views here.
def book_list_view(request):
    ls = book.objects.all().order_by("-n_read")

    genre_list = deque([])
    for s in list(set((ls.values_list("genre", flat=True)))):
        if ',' in s:
            for e in s.split(','):
                if e not in genre_list:
                    genre_list.append(e)
        elif s not in genre_list:
            genre_list.append(s)

    authors_list = deque([])
    for s in list(set((ls.values_list("authors", flat=True)))):
        if ',' in s:
            for e in s.split(','):
                if e not in authors_list:
                    authors_list.append(e)
        elif s not in authors_list:
            authors_list.append(s)



    if request.POST.get("select_genre") != None:
        new_ls = deque([])
        for b in ls:
            if request.POST.get("select_genre") in b.genre:
                new_ls.append(b)
        ls = new_ls

    if request.POST.get("select_author") != None:
        new_ls = deque([])
        for b in ls:
            if request.POST.get("select_author") in b.authors:
                new_ls.append(b) 
        ls = new_ls


    my_form = search_form(request.POST or None)
    if my_form.is_valid():
        data = my_form.cleaned_data.get("search")
        # print("###################")
        # print(data)

        new_ls = deque([])
        for b in ls:
            if (data.lower() in b.name.lower()) or (data.lower() in b.genre.lower()) or (data.lower() in b.authors.lower()):
                new_ls.append(b)

        ls = new_ls
    
    if len(ls)==0:
        no_b = True
    else:
        no_b = False

    return render(request, "books/book_list.html", 
    {"ls":ls, "no_b":no_b, "genre_list":genre_list, "author_list":authors_list})

def book_main_view(request, *args, **kwrgs):
    books= book.objects.all().order_by('-n_read')[:10]
    context={'ls': books}
    return render(request, 'books/book_main.html', context)

def book_view(request, pk):

    bk = book.objects.filter(book_id = pk).first()  
    cs = comment.objects.filter(book = bk)

    
    if str(bk.cover) == "":
        img_path = "/media/books/noImg.jpg"
    else:
        img_path = "/media/" + str(bk.cover)

    # print("@@@@@@@@@@@@@@@@@@@@")
    # print(request.method)

    u = user.objects.all().filter(username = request.user).first()
    u_id = u.user_id
    b_id = bk.book_id

    # print(u_id, b_id)

    stat = ''
    ord_id = 0

    form = review_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        u = user.objects.filter(username = request.user.username).first()
        obj.user = u
        obj.book = bk
        obj.save()
        form = review_form()
    elif request.method == "POST":
        o = order.objects.create(book = bk, user = u, taken = datetime.now(timezone('Asia/Kolkata')))
        ord_id = o.order_id
        stat = o.r_status
        
    # if request.method == "POST":
    #     o = order.objects.create(book = bk, user = u)
    #     stat = o.r_status

    qs = order.objects.all().filter(book = bk).filter(user = u).exclude(r_status = "returned")
    if len(qs):
        qs = qs.first()
        stat = qs.r_status
        ord_id = qs.order_id

        cur = datetime.now(timezone('Asia/Kolkata'))
        if (cur-(qs.taken)).days > 10:
            stat = ""
            ord_id = 0
            qs.delete()


    return render(request, "books/book.html", 
    {"book":bk, "img_path":img_path, "ord_id":ord_id, "cs":cs, "stat":stat, "pk":pk, "count":len(cs), "form":form})

