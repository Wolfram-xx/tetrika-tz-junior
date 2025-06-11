import inspect
from functools import wraps

# Пришлось вспомнить работу wraps, использовал ее ранее всего 1 раз

def strict(func):
    sign = inspect.signature(func)                  # Из сигнатуры мы потом будем брать переданные значения
    annotations = func.__annotations__              # А из аннотации типы, которые должны быть

    @wraps(func)                                    # Насколько я понимаю, в случае, если мы не используем доп функцию wrapper, то декоратор сработает только при инициилизации
    def wrapper(*args, **kwargs):
        b_args = sign.bind(*args, **kwargs)
        b_args.apply_defaults()

        for name, val in b_args.arguments.items():  # Проходим по всем переданным параметрам и сравниваем их типы с необходимыми
            if name in annotations:
                our_type = annotations[name]
                if not isinstance(val, our_type):   # Сравниваем типы переданного значения и того, который нам нужен
                    raise TypeError(
                        f'У переменной {name} зафиксирован тип {annotations[name]}. Необходим тип {our_type}'
                    )                               # В случае, если они не сходятся, вызываем ошибку
        return func(*args, **kwargs)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError

# Комментарии могут показаться вам плохо написанными, но я просто объясняю свое мышление в процессе выполнения задания