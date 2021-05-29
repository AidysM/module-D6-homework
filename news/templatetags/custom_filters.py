from django import template


register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает
    # где именно их искать и фильтры потеряются (


@register.filter(name='multiply') # регестрируем наш фильтр под именем multiply, чтоб django понимал,
    # что это именно фильтр, а не простая функция
def multiply(value, arg): # первый аргумент здесь это то значение, к которому надо применить фильтр,
            # второй аргуменит — это аргумент фильтра, т.е. примерно следующее будет в шаблоне
            # value|multiply:arg
    # return str(value) * arg # возвращаемое функцией значение — это то значение, которой подставится
            # к нам в шаблон
            if isinstance(value, str) and isinstance(arg, int):  # проверяем, что value — это точно
                    # строка, а arg — точно число, чтобы не возникло курьёзов
                return str(value) * arg
            else:
                raise ValueError(
                    f'Нельзя умножить {type(value)} на {type(arg)}')  # в случае если кто-то неправильно
                        # воспользовался нашим тегом выводим ошибку


@register.filter(name='censor')
def censor(value, arg):
    words = value.split()
    value1 = ''
    for word in words:
        if isinstance(word, str) and isinstance(arg, str):
            if word == arg:
                word = '!censor!'
            value1 += word + ' '
        else:
            raise ValueError(f'Нельзя {type(word)}!')
    return value1


