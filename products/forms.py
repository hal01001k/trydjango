from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Text Here"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "placeholder":"Discription Here",
                                "class":"new-class-name two",
                                "rows":6,
                                "cols":40
                            }
                        )
    )
    price       = forms.DecimalField()

