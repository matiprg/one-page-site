from django.urls import path
from pages.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name='pages'
urlpatterns=[

    #path('pages',pages_view,name='index'),
    path('ourteam',ourteam_view,name='ourteam'),
    path('testimonial',testimonial_view,name='testimonial'),
    path('fourpage',fourpage_view,name='fourpage'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)