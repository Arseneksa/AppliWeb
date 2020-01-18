
from django import forms
from .models import *

class InscriptionForm(forms.ModelForm):
    
    email = forms.EmailField( widget= forms.EmailInput(
            attrs = {
                'placeholder':'Votre Email',
            }
        ))
    username = forms.CharField( widget= forms.TextInput(
            attrs = {
                'class':'form-control single-input',
                'placeholder':'Nom Utilisateur',
            }
        ))
    password = forms.CharField( widget= forms.PasswordInput(
            attrs = {
                'class':'form-control single-input',
                'placeholder':'Mot de passe',
            }
        ))
    password_repeat = forms.CharField( widget= forms.PasswordInput(
            attrs = {
                'placeholder':'Confirmez mot de passe',
            }
        ))
    specialite =forms.CharField( widget= forms.TextInput(
            attrs = {
                'placeholder':'Spécialité',
            }
        ))
    telephone = forms.CharField( widget= forms.NumberInput(
            attrs = {
                'placeholder':'N° de téléphone',
            }
        ))
    class  Meta:
        model = Utilisateur
        fields = ('email','username', 'mot de passe', 'spécialité', 'téléphone')
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control single-input'
            
class ConnexionForm(forms.Form):
     username = forms.CharField( widget= forms.TextInput(
            attrs = {
                'class':'form-control single-input',
                'placeholder':'Nom Utilisateur',
            }
        ))
    
     password = forms.CharField( widget= forms.PasswordInput(
            attrs = {
                'class':'form-control single-input',
                'placeholder':'Mot de passe',
            }
        ))
        
class SearchForm(forms.Form):
        
    motcle = forms.CharField( widget= forms.TextInput(
            attrs = {
                'placeholder':'Mots clés (ex: ingenieur; developpeur, stage ...)',
                'requiered':'false',
            }
        ))
    localite = forms.CharField(widget= forms.TextInput(
		attrs = {
			'placeholder':'Localité',
            'requiered':'false',
		}
        
    ))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
class ChangePassForm(forms.Form):
    oldPassword = forms.CharField( widget= forms.PasswordInput(
            attrs = {
                'class':'col-sm-2 control-label',
                'placeholder':'Ancien Mot de passe',
            }
        ))
    newPassword = forms.CharField( widget= forms.PasswordInput(
            attrs = {
                'class':'col-sm-2 control-label',
                'placeholder':'Nouveau Mot de passe',
            }
        ))
class AddCompetenceForm(forms.Form):
    Competence = forms.CharField( widget= forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Compétence',
            }
    ))
class AddLocalisationForm(forms.Form):
    localisation = forms.CharField( widget= forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Localisation',
            }
    ))

class AddDiplomeForm(forms.Form):
    diplome = forms.CharField( widget= forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Diplome le plus récent',
            }
    ))

class ContactForm(forms.Form):
    nom = forms.CharField( widget= forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Entrez votre nom',
            }
    ))
    
    email = forms.EmailField( widget= forms.EmailInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Votre Email',
            }
        ))
        
    objet = forms.CharField( widget= forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Entrez l\' objet du mail',
            }
    ))
    
    message = forms.CharField( widget= forms.Textarea(
            attrs = {
                'class':'form-control',
                'placeholder':'Message',
            }
    ))