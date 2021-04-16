from django.shortcuts import render,redirect
from .models import Song,AudioType,AudioBook,Podcast
from .forms import SongForm,AudioTypeForm,AudioBookForm,PodcastForm
from django.views.generic import TemplateView
from django.contrib import messages
# Create your views here.

# For audio selection to create
class AudioTypeCreate(TemplateView):
    model = AudioType
    form_class = AudioTypeForm
    template_name = "audiotypes/audiotype.html"
    context = {}

    def get(self,request,*args,**kwargs):
        self.context["form"] = self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        types = request.POST.get('audiotype')
        if form.is_valid():
            form.save()
            #Redirects according to the audio selection
            if types == '1':
                return redirect('songcreate')
            elif types == '2':
                return redirect('audiocreate')
            elif types == '3':
                return redirect('podcastcreate')
            else:
                print('None')
            return render(request,self.template_name,self.context)

# For audio selection to edit
class AudioTypeEdit(TemplateView):
    model = AudioType
    form_class = AudioTypeForm
    template_name = "audiotypes/audiotype.html"
    context = {}

    def get(self,request,*args,**kwargs):
        self.context["form"] = self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        types = request.POST.get('audiotype')
        if form.is_valid():
            form.save()
            #Redirects according to the audio selection
            if types == '1':
                return redirect('songeditlist')
            elif types == '2':
                return redirect('audioeditlist')
            elif types == '3':
                return redirect('podcasteditlist')
            else:
                print('None')
            return render(request,self.template_name,self.context)

# for audio selection to list
class AudioTypeList(TemplateView):
    model = AudioType
    form_class = AudioTypeForm
    template_name = "audiotypes/audiotype.html"
    context = {}

    def get(self,request,*args,**kwargs):
        self.context["form"] = self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        types = request.POST.get('audiotype')
        if form.is_valid():
            form.save()
            #Redirects according to the audio selection
            if types == '1':
                return redirect('songlist')
            elif types == '2':
                return redirect('audiolist')
            elif types == '3':
                return redirect('podcastlist')
            else:
                print('None')
            return render(request,self.template_name,self.context)

# For Audio selection to delete
class AudioTypeDelete(TemplateView):
    model = AudioType
    form_class = AudioTypeForm
    template_name = "audiotypes/audiotype.html"
    context = {}

    def get(self,request,*args,**kwargs):
        self.context["form"] = self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        types = request.POST.get('audiotype')
        if form.is_valid():
            form.save()
            #Redirects according to the audio selection
            if types == '1':
                return redirect('songdeletelist')
            elif types == '2':
                return redirect('audiodeletelist') 
            elif types == '3':
                return redirect('podcastdeletelist')
            else:
                print('None')
            return render(request,self.template_name,self.context)

# For song create single item
class SongCreateView(TemplateView):
    model = Song
    form_class = SongForm
    template_name = "audiotypes/song_create.html"
    context = {}

    def get(self,request,*args,**kwargs):
        self.context["form"] = self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        self.context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, 'Song created successfully.')
            return redirect('typecreate')
        else:
            messages.error(request, 'Invalid Details please check the form and submit.')
            return render(request,self.template_name,self.context) 

# For song edit single item 
class SongEditView(TemplateView):
    model = Song
    form_class = SongForm
    template_name = "audiotypes/song_edit.html"
    context = {}

    def get(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs)
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs,data=request.POST)
        self.context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, 'Song  edited successfully.')
            return redirect('typeedit')
        else:
            messages.error(request, 'Invalid Details please check the form and submit.')
            return render(request,self.template_name,self.context)

# For Song delete single item
class SongDeleteView(TemplateView):
    model = Song
    form_class = SongForm
    template_name = "audiotypes/song_delete.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = self.form_class(instance=qs)
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect('typedelete')

# For Song Detailed view Single
class SongDetailView(TemplateView):
    model = Song
    form_class = SongForm
    template_name = "audiotypes/song_detail.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        id = kwargs.get("pk")
        obj = self.model.objects.get(id=id)
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For Song Detail listing
class SongListView(TemplateView):
    model = Song
    form_class = SongForm
    template_name = "audiotypes/song_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For song Edit listing
class SongEditListView(TemplateView):
    model = Song
    form_class = SongForm
    template_name = "audiotypes/songedit_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For Song Delete listing
class SongDeleteListView(TemplateView):
    model = Song
    form_class = SongForm
    template_name = "audiotypes/songdelete_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

#######
# For Audiobook create single item
class AudioBookCreateView(TemplateView):
    model = AudioBook
    form_class = AudioBookForm
    template_name = "audiotypes/book_create.html"
    context = {}

    def get(self,request,*args,**kwargs):
        self.context["form"] = self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        self.context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, 'AudioBook created successfully.')
            return redirect('typecreate')
        else:
            messages.error(request, 'Invalid Details please check the form and submit.')
            return render(request,self.template_name,self.context) 

# For AudioBook edit single item 
class AudioBookEditView(TemplateView):
    model = AudioBook
    form_class = AudioBookForm
    template_name = "audiotypes/book_edit.html"
    context = {}

    def get(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs)
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs,data=request.POST)
        self.context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, 'AudioBook  edited successfully.')
            return redirect('typeedit')
        else:
            messages.error(request, 'Invalid Details please check the form and submit.')
            return render(request,self.template_name,self.context)

# For AudioBook delete single item
class AudioBookDeleteView(TemplateView):
    model = AudioBook
    form_class = AudioBookForm
    template_name = "audiotypes/book_delete.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = self.form_class(instance=qs)
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect('typedelete')

# For AudioBook Detailed view Single
class AudioBookDetailView(TemplateView):
    model = AudioBook
    form_class = AudioBookForm
    template_name = "audiotypes/book_detail.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        id = kwargs.get("pk")
        obj = self.model.objects.get(id=id)
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For AudioBook Detail listing
class AudioBookListView(TemplateView):
    model = AudioBook
    form_class = AudioBookForm
    template_name = "audiotypes/book_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For AudioBook Edit listing
class AudioBookEditListView(TemplateView):
    model = AudioBook
    form_class = AudioBookForm
    template_name = "audiotypes/bookedit_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For AudioBook Delete listing
class AudioBookDeleteListView(TemplateView):
    model = AudioBook
    form_class = AudioBookForm
    template_name = "audiotypes/bookdelete_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

########
# For Podcast create single item
class PodcastCreateView(TemplateView):
    model = Podcast
    form_class = PodcastForm
    template_name = "audiotypes/podcast_create.html"
    context = {}

    def get(self,request,*args,**kwargs):
        self.context["form"] = self.form_class
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        self.context['form'] = form
        rem = request.POST.getlist('participants')
        my_string = ','.join(map(str,rem))
        if form.is_valid():
            PodcastCreate = form.save(commit=False)
            PodcastCreate.Podcast_Participants = my_string
            PodcastCreate.save()
            messages.success(request, 'Podcast created successfully.')
            return redirect('typecreate')
        else:
            messages.error(request, 'Invalid Details please check the form and submit.')
            return render(request,self.template_name,self.context) 

# For podcast edit single item 
class PodcastEditView(TemplateView):
    model = Podcast
    form_class = PodcastForm
    template_name = "audiotypes/podcast_edit.html"
    context = {}

    def get(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs)
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs,data=request.POST)
        self.context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, 'Podcast  edited successfully.')
            return redirect('typeedit')
        else:
            messages.error(request, 'Invalid Details please check the form and submit.')
            return render(request,self.template_name,self.context)

# For Podcast delete single item
class PodcastDeleteView(TemplateView):
    model = Podcast
    form_class = PodcastForm
    template_name = "audiotypes/podcast_delete.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = self.form_class(instance=qs)
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect('typedelete')

# For Podcast Detailed view Single
class PodcastDetailView(TemplateView):
    model = Podcast
    form_class = PodcastForm
    template_name = "audiotypes/podcast_detail.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        id = kwargs.get("pk")
        obj = self.model.objects.get(id=id)
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For Podcast Detail listing
class PodcastListView(TemplateView):
    model = Podcast
    form_class = PodcastForm
    template_name = "audiotypes/podcast_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For Podcast Edit listing
class PodcastEditListView(TemplateView):
    model = Podcast
    form_class = PodcastForm
    template_name = "audiotypes/podcastedit_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)

# For Podcast Delete listing
class PodcastDeleteListView(TemplateView):
    model = Podcast
    form_class = PodcastForm
    template_name = "audiotypes/podcastdelete_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        self.context['form'] = obj
        return render(request,self.template_name,self.context)