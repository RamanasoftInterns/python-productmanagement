from django.urls import path, include
from .import views
urlpatterns = [
    path('table/', views.pdf_table, name="pdf_convert"),
    path('pdf_view/', views.render_pdf_view, name="pdf_view"),
]
