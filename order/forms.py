from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Hà Nội', 'Hà Nội'),
		('Hải Phòng', 'Hải Phòng'),

	)

	DISCRICT_CHOICES = (
		('Đan Phượng', 'Đan Phượng'),
		('Hoài Đức', 'Hoài Đức'),
	)

	PAYMENT_METHOD_CHOICES = (
		('VNPay', 'VNPay'),
		('Paypal', 'Paypal'),
		('Thẻ ghi nợ','Thẻ ghi nợ')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
