from django.shortcuts import render , redirect
from .models import *
import random , string

def main_view(request):
    urls = Url.objects.all()
    return render(request , 'main_page.html', {'urls':urls})

def url_details(request, id):
    DETAIL = Url.objects.get(id=id)
    return render(request , 'url_detail.html', {'url':DETAIL})
def add_url(request):
    
    if request.method == 'POST':
        new_note = Url(
            long = request.POST.get('long'),
            short = url_shortener()
        )
        new_note.save()
        return render(request,'url_added.html')
    return render(request, 'add_url.html')
    

def r1edirect(request,id):
    goal = Url.objects.get(id = id)
    goal.count+=1
    goal.save()
    print(goal.count)
    return redirect(goal.long)

def url_shortener():
    characters = string.ascii_letters + string.digits  # You can customize this as needed
    random_string = ''.join(random.choice(characters) for _ in range(7))
    return 'WWW.ShortenedByLuka.com'+'/'+random_string
def delete_note(request,id):
    delete = Url.objects.get(id=id)
    delete.delete()
    return render(request, 'deleted.html')