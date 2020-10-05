
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    #if we only have one app we can put all the paths here
    #but its better practice to keep them in their app folder

]
