from django.contrib import admin
from django.urls import path
from june6app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("follow", views.follow, name="follow"),
    path("mentor", views.mentor, name="mentor"),
    path("courses", views.courses, name="courses"),
    path("success", views.success, name="success"),
    path("post", views.show, name="show"),
]

# Serve static and media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
