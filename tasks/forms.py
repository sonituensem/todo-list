from django import forms

from tasks.models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "is_done", "tags")
        widgets = {
            "content": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter task",
                }
            ),
            "deadline": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M",
            ),
            "is_done": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                }
            ),
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["deadline"].input_formats = ["%Y-%m-%dT%H:%M"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter tag name",
                }
            ),
        }
