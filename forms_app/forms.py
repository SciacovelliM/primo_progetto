from django import forms
from .models import Contatto

#class FormContatto(forms.Form):
#    nome= forms.CharField()
#    cognome= forms.CharField()
#    email= forms.EmailField()
#    contenuto= forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Area Testuale! Scrivi!"}))

class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"
        widgets={
            'nome': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'cognome': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'contenuto': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
        }
    
    def clean_contenuto(self):
        dati= self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viola le norme del sito.")
        if len(dati)<20:
            raise ValidationError("Il contenuto inserito è troppo breve")
        return dati