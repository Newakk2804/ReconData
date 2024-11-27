"""ReconData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from ListOfPeople import views

urlpatterns = [
    path(
        "detailIndividual/<int:pk>",
        views.HomeDetailIndividualView.as_view(),
        name="detailIndividual_page",
    ),
    path(
        "detailIndividEnter/<int:pk>",
        views.HomeDetailIndiviEnterView.as_view(),
        name="detailIndividEnter_page",
    ),
    path(
        "detailLegalPerson/<int:pk>",
        views.HomeDetailLegalPersonView.as_view(),
        name="detailLegalPerson_page",
    ),
    path(
        "individEnter-page", views.IndividEnterView.as_view(), name="individEnter_page"
    ),
    path("individual-page", views.IndividualView.as_view(), name="individual_page"),
    path("legalPerson-page", views.LegalPersonView.as_view(), name="legalPerson_page"),
    path("", views.HomeListView.as_view(), name="home"),
    path("edit-page", views.edit_page, name="edit_page"),
    path("editIndividual-page", views.edit_individual_page, name="edit_individual_page"),
    path("editIndividEnter-page", views.edit_individEnter_page, name="edit_individEnter_page"),
    path("editLegalPerson-page", views.edit_legalPerson_page, name="edit_legalPerson_page"),
    path("updateIndividual-page/<int:pk>", views.update_individual_page, name="update_individual_page"),
    path("deleteIndividual-page/<int:pk>", views.delete_individual_page, name="delete_individual_page"),
    path("updateIndividEnter-page/<int:pk>", views.update_individEnter_page, name="update_individEnter_page"),
    path("deleteIndividEnter-page/<int:pk>", views.delete_individEnter_page, name="delete_individEnter_page"),
    path("updateLegalPerson-page/<int:pk>", views.update_legalPerson_page, name="update_legalPerson_page"),
    path("deleteLegalPerson-page/<int:pk>", views.delete_legalPerson_page, name="delete_legalPerson_page"),
]
