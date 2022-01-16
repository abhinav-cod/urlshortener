from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import tinyurls
from .forms import tinyurlsform


# Create your views here.
def index(request):
    template='urlshort/index.html'
    context={}
    context['form']=tinyurlsform()
    if request.method=='GET':
        return render(request,template,context)
    elif request.method=='POST':
        used_form=tinyurlsform(request.POST)
        if used_form.is_valid():
            shortened_object=used_form.save()
            new_url=request.build_absolute_uri('/')+shortened_object.tiny_url
            original_url=shortened_object.original_url

            context['new_url']=new_url
            context['original_url']=original_url

            return render(request,template,context)
        context['error']=used_form.errors
        return render(request,template,context)


def redirect_view(request,tiny_path):
    print(tiny_path)
    try:
        shortener=tinyurls.objects.get(tiny_url=tiny_path)
        print(shortener)
        # tinyurls.objects.filter(tiny_url=tiny_path).update(num_times_followed=num_times_followed+1)
        return HttpResponseRedirect(shortener.original_url)
    except:
        raise Http404('Sorry this link is broken :(')
