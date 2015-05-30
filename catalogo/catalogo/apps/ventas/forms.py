from catalogo.apps.ventas.models import Producto
from django import forms

class add_product_form(forms.ModelForm):
	class Meta:
		model  = Producto

		exclude = {'status',}
		
			