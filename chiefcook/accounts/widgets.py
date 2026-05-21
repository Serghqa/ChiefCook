from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    template_name = "accounts/widgets/avatar_form.html"
    clear_checkbox_label = "Удалить фото"
    initial_text = "Текущее фото"
    input_text = "Изменить"
