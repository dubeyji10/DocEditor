from django.shortcuts import render,redirect
from .models import Document
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from PIL import Image
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone

# null -- landing page
def welcome(request):
    return render(request,'editor/welcome.html',{'title':'Landing Page'})



def home(request):
    context = {
        'posts':Document.objects.all()
    }
    return render(request,'editor/home_backup.html',context)

class DocumentListView(ListView):
    model = Document
    template_name = 'editor/home_backup.html'
    #<app>/<model>_<viewtype>.html
    context_object_name = 'documents'
    ordering = ['-date_posted']
    paginate_by = 4


class DocumentDetailView(DetailView):
    model = Document

class DocumentCreateView(LoginRequiredMixin,CreateView):
    model = Document
    fields = ['title','content']#remove image

    def form_valid(self,form):
        #setting the author to the logged in
        form.instance.author = self.request.user

        return super().form_valid(form)

class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = Document
    fields = ['title','content']

    def form_valid(self,form):#setting the author to the logged in
        form.instance.last_change_details = str(self.request.user) + " \non : "+ str(form.instance.date_posted)
        return super().form_valid(form)

    # def test_func(self):
    #     document = self.get_object()
    #     if self.request.user == document.author:
    #         return True
    #     return False #403 -forbidden


