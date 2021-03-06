from django.db import models


from billing.models import BillingProfile

ADDRESS_TYPES = (
	('billing', 'Billing'),
	('shipping','Shipping'),
	)

class Address(models.Model):
	billing_profile 	= models.ForeignKey(BillingProfile)
	address_type 		= models.CharField(max_length=120, choices=ADDRESS_TYPES)
	address_line_1 		= models.CharField(max_length=120)
	address_line_2 		= models.CharField(max_length=120)
	city 				= models.CharField(max_length=120)
	country 			= models.CharField(max_length=120, default='Netherlands')
	post_code 			= models.CharField(max_length=120)

	def __str__(self):
		return str(self.billing_profile)


 
	def get_address(self):
		return "{line1}\n{line2}\n{city}\n{postal}\n{country}".format(
			line1 = self.address_line_1, 
			line2 = self.address_line_2 or "",
			city = self.city,
			postal= self.post_code,
			country = self.country
			)

