from django import forms
from .models import IndividualBd, IndividEnter, LegalPerson


class IndividualForm(forms.ModelForm):
    class Meta:
        model = IndividualBd
        fields = "__all__"
        widgets = {
            "dateOfBirth": forms.SelectDateWidget(years=range(1940, 2024)),
            "dateIssuedBy": forms.SelectDateWidget(years=range(1940, 2024)),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class IndividEnterForm(forms.ModelForm):
    class Meta:
        model = IndividEnter
        fields = "__all__"
        widgets = {
            "dateOfBirth": forms.SelectDateWidget(years=range(1940, 2024)),
            "dateIssuedBy": forms.SelectDateWidget(years=range(1940, 2024)),
            "dateRegist": forms.SelectDateWidget(years=range(1940, 2024)),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class LegalPersonForm(forms.ModelForm):
    class Meta:
        model = LegalPerson
        fields = "__all__"
        widgets = {
            "dateRegist": forms.SelectDateWidget(years=range(1940, 2024)),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"