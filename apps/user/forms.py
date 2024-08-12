from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao_silva"
            }
        )
    )
    password=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    
class RegisterForm(forms.Form):
    name=forms.CharField(
        label="Nome completo",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    email=forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao_silva@xpto.com"
            }
        )
    )
    username=forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,        
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao_silva"
            }
        )
    )
    password=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    confirm_password=forms.CharField(
        label="Confirmação de senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite novamente sua senha"
            }
        )
    )
    
    #precisa iniciar com 'clean' - padrão django
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if username:
            username = username.strip() #remove espaços do início e do fim
            
            if ' ' in username:
                raise forms.ValidationError('Não é possível inserir epaços no campo Usuário!')
            else:
                return username