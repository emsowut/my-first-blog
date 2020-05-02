from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]

'''
- post/ means that the URL should begin with the word post followed by a /.
- <int:pk> means that Django expects an integer value and will transfer it to a view as a variable called pk.
- / then we need a / again before finishing the URL.
'''