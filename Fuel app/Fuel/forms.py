from django import forms

from Fuel.models import FuelRequest, User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    car_licence = forms.CharField()
    phone_number = forms.CharField()
    role = forms.ChoiceField(choices=User.Role.choices)


class RequestFuelForm(forms.Form):
    address = forms.CharField(max_length=200)
    amount = forms.IntegerField(max_value=40)


class AssignFuelRequstForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._set_agent_choices()

    def _set_agent_choices(self):
        self.fields['agent'].choices = sorted([
            (agent.id, f"{agent.first_name} {agent.last_name}") for agent in
            User.objects.all().filter(role=User.Role.AGENT, status=User.StatusTypes.AVAILABLE)
        ])

    class Meta:
        model = FuelRequest
        fields = [
            "amount",
            "address",
            "agent",
        ]
        widgets = {
            "amount": forms.NumberInput(attrs={'readonly': 'readonly'}),
            "address": forms.TextInput(attrs={'readonly': 'readonly'}),
        }
