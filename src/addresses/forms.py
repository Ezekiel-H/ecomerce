from django import forms
from crispy_forms.helper import FormHelper
from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = [
			# 'billing_profile',
			# 'address_type',
			'address_line_1',
			'address_line_2',
			'city',
			'country',
			'post_code'
		]

		def __init__(self):
			super(ExampleForm, self).__init__
			for visible in self.visible_fields():
				visible.field.widget.attrs['class'] = 'form-control'