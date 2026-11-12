from django import forms
from .models import Comment, Subscriber

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Напиши свій коментар...',
                'rows': 4,
            })
        }

    def clean_text(self):
        text = self.cleaned_data["text"].strip()

        if len(text) < 5:
            raise forms.ValidationError(
               "Коментар має містити мінімум 5 символів."
            )

        if len(text) > 500:
            raise forms.ValidationError(
                "Коментар не може перевищувати 500 символів."
            )
        return text

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Введіть ваш email'
            })
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.strip().lower()