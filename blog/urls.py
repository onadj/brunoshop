from django.urls import path
from .views import AddBlogView, CreateBlogView, DeleteBlogView

urlpatterns = [
    path('', AddBlogView.as_view(), name='bloghome'),
    path('addnew/', CreateBlogView.as_view(), name='addnewblog'),
    path('remove/<int:pk>/', DeleteBlogView.as_view(), name='deleteblog'),
]
