from django.urls import path
from website.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',index_view),
    path('about',about_view),
    path('contact',contact_view)

    

]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)