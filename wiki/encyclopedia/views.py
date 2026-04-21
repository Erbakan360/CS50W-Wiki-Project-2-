from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util
from random import randint

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        if content == None:
            content = "### Page not found"
        content = markdown(content)
        return render(request, "encyclopedia/entry.html", {
            "content": content,
            "entry": title
        })
    else:
        return redirect("edit", title=title)


def search(request):
    query = request.GET.get("q").strip()
    matches = set()
    entries = util.list_entries()
    for entry in entries:
        if query.upper() == entry.upper():
            return redirect("entry", title=entry)
        for i in range (0, len(entry)):
            if entry[i].upper() == query.upper():
                matches.add(entry)
            elif query.upper() in entry.upper():
                matches.add(entry)

    return render(request, "encyclopedia/search.html", {
        "query": query,
        "entries": matches
    })


def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title in util.list_entries():
            error = markdown("### entry already exists")
            return render(request, "encyclopedia/error.html", {"error":error})
        elif content == None or content == "" or title == None or title == "":
            error = markdown("### Fields cannot remain empty")
            return render(request, "encyclopedia/error.html", {"error":error})
        util.save_entry(title, content)
        return redirect("entry", title = title)

        
def random(request):
    titles = util.list_entries()
    random = titles[randint(0, len(titles)-1)]
    return redirect("entry", title=random)

def edit(request, title):
    content = util.get_entry(title)
    if content == None:
        error = "### Entry doesn't exist"
        error = markdown(error)
        return render(request, "encyclopedia/error.html", {"error":error})

    if request.method == "POST":
        content = request.POST.get("content").strip()
        if content == "":
            error = "Fields cannot remain empty"
            return render(request, "encyclopedia/edit.html", {"message": error, "title": title, "content": content})
        
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {'content': content, 'title': title})  