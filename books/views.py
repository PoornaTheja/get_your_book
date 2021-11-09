from django.shortcuts import render
from .models import book
from .forms import search_form, filter_form
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


    # filt_form = filter_form(request.POST or None)
    # print("*******************")
    # print(request.POST.get("select_genre") or request.POST.get("select_author"))
    # if filt_form.is_valid():
    #     gen = filt_form.cleaned_data.get("select_genre")
    #     aut = filt_form.cleaned_data.get("select_author")
    #     print("-------------------")
    #     print(gen, aut)

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
    
    if len(ls)==0:
        no_b = True
    else:
        no_b = False

    return render(request, "books/book_list.html", 
    {"ls":ls, "no_b":no_b, "genre_list":genre_list, "author_list":authors_list})

def book_view(request, pk):
    bk = book.objects.filter(book_id = pk).first()
    img_path = "/media/" + str(bk.cover)[2:-1] + "/"

    return render(request, "books/book.html", {"book":bk, "img_path":img_path})