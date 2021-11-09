from django.shortcuts import render
from .models import book
from comments.models import comment
from .forms import search_form
from collections import deque

# Create your views here.
def book_list_view(request):
    ls = book.objects.all()

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
            if data.lower() in b.name.lower():
                new_ls.append(b)

        ls = new_ls

    ls = ls.order_by("n_read")
    
    if len(ls)==0:
        no_b = True
    else:
        no_b = False

    return render(request, "books/book_list.html", 
    {"ls":ls, "no_b":no_b, "genre_list":genre_list, "author_list":authors_list})

def book_view(request, pk):

    bk = book.objects.filter(book_id = pk).first()  
    cs = comment.objects.filter(book = bk)
    
    img_path = "/media/" + str(bk.cover) + "/"

    return render(request, "books/book.html", {"book":bk, "img_path":img_path, "cs":cs})