from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:contact_id>', views.seeContact, name='view_contact'),

]

from .api import views as api_views

urlpatterns += [
    path('api/contacts/', api_views.ContactListCreateAPIView.as_view(), name='api_contacts'),
    path('api/contacts/<int:pk>/', api_views.ContactRetrieveAPIView.as_view(), name='api_contact_detail'),
]
