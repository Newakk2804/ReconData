from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import IndividualBd, IndividEnter, LegalPerson
from .forms import IndividualForm, IndividEnterForm, LegalPersonForm
from django.urls import reverse


class HomeListView(ListView):
    model = IndividualBd
    template_name = "index.html"
    context_object_name = "list_peopleBd"


class IndividEnterView(ListView):
    model = IndividEnter
    template_name = "individEnter_page.html"
    context_object_name = "list_individEnter"


class IndividualView(ListView):
    model = IndividualBd
    template_name = "individual_page.html"
    context_object_name = "list_individual"


class LegalPersonView(ListView):
    model = LegalPerson
    template_name = "legalPerson_page.html"
    context_object_name = "list_legalPerson"


class HomeDetailIndividualView(DetailView):
    model = IndividualBd
    template_name = "detailIndividual.html"
    context_object_name = "get_individual"


class HomeDetailIndiviEnterView(DetailView):
    model = IndividEnter
    template_name = "detailIndividEnter.html"
    context_object_name = "get_individEnter"


class HomeDetailLegalPersonView(DetailView):
    model = LegalPerson
    template_name = "detailLegalPerson.html"
    context_object_name = "get_legalPerson"


def edit_individual_page(request):
    if request.method == "POST":
        form = IndividualForm(request.POST)
        if form.is_valid():
            form.save()
    template = "edit_individual_page.html"
    context = {
        "list_people": IndividualBd.objects.all().order_by("id"),
        "form": IndividualForm(),
    }
    return render(request, template, context)


def edit_individEnter_page(request):
    if request.method == "POST":
        form = IndividEnterForm(request.POST)
        if form.is_valid():
            form.save()
    template = "edit_individEnter_page.html"
    context = {
        "list_individEnter": IndividEnter.objects.all().order_by("id"),
        "form": IndividEnterForm(),
    }
    return render(request, template, context)


def edit_legalPerson_page(request):
    if request.method == "POST":
        form = LegalPersonForm(request.POST)
        if form.is_valid():
            form.save()
    template = "edit_legalPerson_page.html"
    context = {
        "list_legalPerson": LegalPerson.objects.all().order_by("id"),
        "form": LegalPersonForm(),
    }
    return render(request, template, context)


def edit_page(request):
    if request.method == "POST":
        form = IndividualForm(request.POST)
        if form.is_valid():
            form.save()

    template = "edit_page.html"
    context = {
        "list_people": IndividualBd.objects.all().order_by("id"),
        "form": IndividualForm(),
    }

    return render(request, template, context)


def update_individual_page(request, pk):
    get_people = IndividualBd.objects.get(pk=pk)
    if request.method == "POST":
        form = IndividualForm(request.POST, instance=get_people)
        if form.is_valid():
            form.save()
    template = "edit_individual_page.html"
    context = {
        "get_people": get_people,
        "update": True,
        "form": IndividualForm(instance=get_people),
    }
    return render(request, template, context)


def update_individEnter_page(request, pk):
    get_individEnter = IndividEnter.objects.get(pk=pk)
    if request.method == "POST":
        form = IndividEnterForm(request.POST, instance=get_individEnter)
        if form.is_valid():
            form.save()
    template = "edit_individEnter_page.html"
    context = {
        "get_individEnter": get_individEnter,
        "update": True,
        "form": IndividEnterForm(instance=get_individEnter),
    }
    return render(request, template, context)


def update_legalPerson_page(request, pk):
    get_legalPerson = LegalPerson.objects.get(pk=pk)
    if request.method == "POST":
        form = LegalPersonForm(request.POST, instance=get_legalPerson)
        if form.is_valid():
            form.save()
    template = "edit_legalPerson_page.html"
    context = {
        "get_legalPerson": get_legalPerson,
        "update": True,
        "form": LegalPersonForm(instance=get_legalPerson),
    }
    return render(request, template, context)


def delete_individual_page(request, pk):
    get_people = IndividualBd.objects.get(pk=pk)
    get_people.delete()
    return redirect(reverse("edit_individual_page"))


def delete_individEnter_page(request, pk):
    get_individEnter = IndividEnter.objects.get(pk=pk)
    get_individEnter.delete()
    return redirect(reverse("edit_individEnter_page"))


def delete_legalPerson_page(request, pk):
    get_legalPerson = LegalPerson.objects.get(pk=pk)
    get_legalPerson.delete()
    return redirect(reverse("edit_legalPerson_page"))
