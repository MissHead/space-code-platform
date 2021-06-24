from django.conf.urls import url
from space_travel import views


urlpatterns = [
    url(r'^health$', views.health_check),
    url(r'^pilot$', views.pilot_controller),
    url(r'^pilot/(?P<_id>[0-9]+)$', views.pilot_handle),
    url(r'^resource$', views.resource_controller),
    url(r'^resource/(?P<_id>[0-9]+)$', views.resource_handle),
    url(r'^contract$', views.contract_controller),
    url(r'^contract/(?P<_id>[0-9]+)$', views.contract_handle),
    url(r'^ship$', views.ship_controller),
    url(r'^ship/(?P<_id>[0-9]+)$', views.ship_handle),
    url(r'^planet$', views.planet_controller),
    url(r'^planet/(?P<_id>[0-9]+)$', views.planet_handle),
    url(r'^travel$', views.travel_controller),
    url(r'^travel/(?P<_id>[0-9]+)$', views.travel_handle)
]
