from django.forms import ModelForm, BooleanField # Импортируем true-false поле
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля.
    # Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['post_name', 'position', 'category', 'author', 'content']
        # не забываем включить галочку в поля иначе она не будет показываться на странице!

