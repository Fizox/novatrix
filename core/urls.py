from django.urls import path

from .views import about, contact, home, pricing, services

urlpatterns = [
	path("", home, name="home"),
	path("services/", services, name="services"),
	path("pricing/", pricing, name="pricing"),
	path("about/", about, name="about"),
	path("contact/", contact, name="contact"),
]
