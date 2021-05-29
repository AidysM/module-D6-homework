from django_filters import FilterSet, CharFilter  # импортируем filterset, чем-то
                                    # напоминающий знакомые дженерики
from .models import Post, Author, Category


# создаём фильтр
class PostFilter(FilterSet):
    user__author = CharFilter(lookup_expr='icontains')
    category__category = CharFilter(lookup_expr='icontains')
    # Здесь в мета классе надо предоставить модель и указать поля по которым будет
    # фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {
            'post_date': ['gt'], # количество товаров должно быть больше или равно тому,
                                # что указал пользователь
            'post_name': ['icontains'], # мы хотим чтобы нам выводило имя хотя бы
                            # отдалённо похожее на то что запросил пользователь
            #['lt'], # цена должна быть меньше или равна тому, что указал пользователь
        }
        # поля которые мы будем фильтровать (т.е. отбирать по каким-то критериям,
        # имена берутся из моделей)
