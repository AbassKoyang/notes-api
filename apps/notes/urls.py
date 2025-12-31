from django.urls import path
from . import views
urlpatterns = [
    path('', views.ListCreateNoteView.as_view(), name='list-create-note'),
    path('<int:pk>/', views.RetrieveNoteView.as_view(), name='retrieve-note'),
    path('<int:pk>/update/', views.UpdateNoteView.as_view(), name='update-note'),
    path('<int:pk>/delete/', views.DeleteNoteView.as_view(), name='delete-note')
]