from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page , name='login_page'),
    path('register/', register_page, name='register_page'),
    path('hotels-detail/<uid>/' , hotels_detail , name="hotels_detail"),
    path('check_booking/' , check_booking),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()