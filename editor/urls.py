from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.dates import ArchiveIndexView
from .models import Document
from django.urls import reverse


urlpatterns = [
    path('',views.welcome,name='editor'),
    path('home/',views.DocumentListView.as_view(),name='editor-home'),#homepage now
    path('document/<int:pk>/',views.DocumentDetailView.as_view(),name = 'document-detail'),
    path('document/new/',views.DocumentCreateView.as_view(),name = 'document-create'),
    path('document/<int:pk>/update',views.DocumentUpdateView.as_view(),name = 'document-update'),
    path('user/<str:username>',views.UserDocumentListView.as_view(),name='user-documents'),
    path('document/<int:pk>/download',views.DocumentDownload.as_view(),name = 'document-download'),
    path('document/<int:pk>/download2/',views.DocumentDownload2,name = 'document-download2'),
    # path('document/<int:pk>/download3/',views.doc_detail2,name = 'document-download2'),
    path('document/<int:pk>/download3/',views.download_document,name = 'document-download3'),


]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)