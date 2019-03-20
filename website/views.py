from django.shortcuts import render
from django.views.generic import View,TemplateView, FormView, ListView, DetailView
from django.core.mail import send_mail
from website import forms
from website.models import Album, AlbumImage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

#Index view
class Index(TemplateView):
    template_name = 'index.html'

#About-us view
class Artista(TemplateView):
    template_name = 'about-us.html'

#AondeComprar view
class Aonde(TemplateView):
    template_name = 'aonde.html'

#Portfolio(albuns) view
def trabalhos(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        albums = paginator.page(paginator.num_pages) # If page is out of range (e.g.  9999), deliver last page of results.

    return render(request, 'portfolio.html', { 'albums': list })

#Fotos dos Albuns view
class AlbumDetail(DetailView):
     model = Album
     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context

#Form contato view
def contato(request):
    form = forms.ContactForm()
    if request.method == 'GET':
        form = forms.ContactForm(request.GET)

        if form.is_valid():
            subject = "Email do site Farfalla!"
            nome = form.cleaned_data['Nome']
            email = form.cleaned_data['Email']
            mensagem = form.cleaned_data['Mensagem']
            send_mail(subject, mensagem, email, ['atelierfarfallapiccola@gmail.com'])
        return render(request, 'contact.html', {'form':form})

    else:
            form = forms.ContactForm()

    return render(request, 'contact.html', {'form':form})

#404
def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)
