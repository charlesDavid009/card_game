from django import forms

class Iterationsforms(forms.Form):
    iteration = forms.IntegerField(required = True)

    def clean_test_value(self):
        data = self.cleaned_data.get('iteration')
        if 1 > data or data > 10000:
            raise forms.ValidationError('Iteration can not be less than 1 or greater than 10000')

        