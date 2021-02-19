from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.products, name="index"),
<<<<<<< HEAD
    path("category/<int:pk>/", mainapp.products, name="category"),
=======
    path("<int:pk>/", mainapp.products, name="category"),
>>>>>>> 3f1c69c0bcb100de897fe6af20939e0fd64d0777
]