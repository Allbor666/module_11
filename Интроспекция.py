import inspect

def introspection_info(obj):
    # Создание словаря для хранения информации об объекте
    info = {}

    # Получаем тип объекта
    info['type'] = type(obj)

    # Получаем атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект (если возможно)
    info['module'] = getattr(obj, '__module__', None)

    # Получаем дополнительные интересные свойства
    info['doc'] = inspect.getdoc(obj)  # Докстринг объекта
    info['detail'] = str(obj)  # Строковое представление объекта

    return info

# Пример использования функции
number_info = introspection_info(42)
print("Интроспекция числа 42:")
print(number_info)

list_info = introspection_info([1, 2, 3])
print("\nИнтроспекция списка [1, 2, 3]:")
print(list_info)

class MyClass:
    def my_method(self):
        """Это метод экземпляра класса MyClass."""
        pass

class_info = introspection_info(MyClass)
print("\nИнтроспекция класса MyClass:")
print(class_info)
