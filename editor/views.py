from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import get_template

from .models import Document
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from PIL import Image
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
import requests
from requests.auth import HTTPBasicAuth
# from filetransfers.api import serve_file
from urllib.request import urlretrieve, urlcleanup
from xhtml2pdf import pisa

from io import BytesIO
from django.core.files import File
from django.template.loader import get_template

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
        # a dict object returned

        form.instance.last_change_details = str(self.request.user) + str(form.instance.date_posted)
        # print("changes made by ",form.instance.last_change_details)
        return super().form_valid(form)

    # def test_func(self):
    #     document = self.get_object()
    #     if self.request.user == document.author:
    #         return True
    #     return False #403 -forbidden


class UserDocumentListView(ListView):
    model = Document
    template_name = 'editor/user_documents.html'
    #<app>/<model>_<viewtype>.html
    context_object_name = 'documents'
    #ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        return Document.download_to_local(self,)

class DocumentDownload(DetailView):
    model = Document
    print(model.author)
    print('-'*30)
    print(model.content)
    print('-'*30)
    print(model.date_posted)

def DocumentDownload2(request,pk):
    requested_doc = Document.objects.get(id = pk)
    requested_doc = get_object_or_404(Document, pk=pk)
    # print(requested_doc.author)
    # print('-'*20)
    # print(requested_doc.content)
    # print('-'*20)
    data = requested_doc.content
    print(type(data))
    # return
    template_name = 'editor/DownloadDocument2.html'
    return render(request,template_name, {'data':data,
                                          'title':'download page'})


#
# def doc_detail2(request,pk):
#     #    return render(request, 'music/AllUsers.html', {'all_users': all_users,})
#     return redirect('doc-detail2', pk=pk)



def download_document(request,pk):
    requested_doc = Document.objects.get(id = pk)

    # requested_doc = get_object_or_404(Document, pk=pk)
    # context = {'data': requested_doc}
    # pdf  = render_to_pdf()
    template_name = 'editor/DownloadDocument3.html'

    # print('-'*30)
    # print("this is the url of requested file : ",request,"id = ",pk)
    # print('-'*30)
    # print("this is the url of requested file --------- : ",request.path)
    # url_to_be_used = "http://localhost:8000"+request.path
    # print("url which should be passed -> :",url_to_be_used)
    # print('-'*40)
    # print(urlretrieve(url_to_be_used))
    # print("\n ----------------- now focus on downloading ----------------- ")
    # try:
    #     name, _ = url_to_be_used
    #     requested_doc.signed_file.save("{timestamp}.pdf".format(timestamp=timezone.now().strftime('%Y-%m-%d%/%H-%M-%S')), File(open(tempname, 'rb')))
    # finally:
    #     urlcleanup()
    try:
        # request.encoding = 'koi8-r'
        print("-trying to render it into pdf-\n")
        pdf = render_to_pdf(template_name,{'data':requested_doc.content,
                                                       'title':'download page3',
                                                       })
    finally:
        urlcleanup()
    print("-pdf rendering successfull-")
    return HttpResponse(pdf,content_type='application/pdf',charset='utf-8')

    # Document.objects.get(id = pk).download_to_local(request)
    # print("did it save ?")
    #
    # f = requested_doc.signed_file
    # print('file : ',f,'type : ',type(f))
    # print("saving")
    # f.open(mode='rb')
    # lines = f.readlines()
    # f.close()
    # print("saved")
    # requested_doc.saved_file.close()
    #
    # return render(request,template_name, {'data':requested_doc.content,
    #                                       'title':'download page3',
    #                                       })
    # http://localhost:8000/document/4/download3/
    #
    # def generate_obj_pdf(instance_id):
    #     obj = YouModel.objects.get(id=instance_id)
    #     context = {'instance': obj}
    #     pdf = render_to_pdf('your/pdf/template.html', context)
    #     filename = "YourPDF_Order{}.pdf" %(obj.slug)
    #     obj.pdf.save(filename, File(BytesIO(pdf.content)))

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    # utf8
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),charset='latin-1', content_type='application/pdf')
    return None