from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^first/', views.first_loan, name='first_loan'),
    url(r'^search/', views.search, name='search'),
    url(r'^$', views.index, name='index'),
]
