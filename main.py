# numbers = []
#
# while True:
#     print("Меню:")
#     print("1. Добавить новое число в список")
#     print("2. Удалить все вхождения числа из списка")
#     print("3. Показать содержимое списка")
#     print("4. Проверить есть ли значение в списке")
#     print("5. Заменить значение в списке")
#     print("6. Выйти из программы")
#
#     choice = input("Выберите действие (1-6): ")
#
#     if choice == '1':
#         num = int(input("Введите число для добавления: "))
#         if num in numbers:
#             print("Это число уже есть в списке")
#         else:
#             numbers.append(num)
#
#     elif choice == '2':
#         num = int(input("Введите число для удаления "))
#         numbers = [x for x in numbers if x != num]            # Это генератор списка, который создает новый список, исключая из него все элементы, равные введенному числу num. Таким образом, после выполнения этой строки в списке numbers остаются только те элементы, которые не равны num, то есть все вхождения числа num будут удалены из списка.
#
#
#     elif choice == '3':
#         order = input("Введите начало или конец для отображения списка (по умолчанию - начало): ")
#         if order.lower() == 'конец':
#             print(numbers[::-1])
#         else:
#             print(numbers)
#
#     elif choice == '4':
#         num = int(input("Введите число для проверки: "))
#         if num in numbers:
#             print("Значение найдено в списке")
#         else:
#             print("Значение не найдено в списке")
#
#     elif choice == '5':
#         num = int(input("Введите число для замены: "))
#         replace_num = int(input("Введите новое число: "))
#         replace_all = input("Хотите заменить все вхождения? (да/нет): ").lower()
#         if replace_all == 'да':
#             numbers = [replace_num if x == num else x for x in numbers]
#         else:
#             found = False
#             for i in range(len(numbers)):
#                 if numbers[i] == num:
#                     numbers[i] = replace_num
#                     found = True
#                     break
#
#             if not found:
#                 print(f"Число {num} не найдено в списке")
#
#     if choice == '6':
#         print("До свидания! Программа завершена.")
#         break
#


# 2



# class StringStack:
#     def __init__(self, max_size):
#         self.stack = []
#         self.max_size = max_size
#
#     def push(self, string):
#         if len(self.stack) < self.max_size:
#             self.stack.append(string)
#             print(f"Строка {string} добавлена в стек")
#         else:
#             print("Стек полон, невозможно добавить новую строку")
#
#     def pop(self):
#         if not self.is_empty():
#             popped_string = self.stack.pop()
#             print(f"Строка {popped_string} удалена из стека")
#             return popped_string
#         else:
#             print("Стек пуст")
#
#     def count(self):
#         print(f"Количество строк в стеке: {len(self.stack)}")
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def is_full(self):
#         return len(self.stack) == self.max_size
#
#
#     def clear(self):
#         self.stack = []
#         print("Стек очищен")
#
#     def peek(self):
#         if not self.is_empty():
#             print(f"Верхняя строка в стеке: {self.stack[-1]}")
#         else:
#             print("Стек Пуст")
#
# stack = StringStack(2)
#
# while True:
#     print("\nМеню операций:")
#     print("1. Добавить строку в стек")
#     print("2. Удалить строку из стека")
#     print("3. Количество строк в стеке")
#     print("4. Проверить, пуст ли стек")
#     print("5. Проверить, полон ли стек")
#     print("6. Очистить стек")
#     print("7. Получить верхнюю строку в стеке без удаления")
#     print("0. Выход")
#
#     choice = input("Выберите операцию: ")
#
#     if choice == '1':
#         string = input("Введите строку для добавления в стек: ")
#         stack.push(string)
#     elif choice == '2':
#         stack.pop()
#     elif choice == '3':
#         stack.count()
#     elif choice == '4':
#         print(f"Стек пуст: {stack.is_empty()}")
#     elif choice == '5':
#         print(f"Стек полон: {stack.is_full()}")
#     elif choice == '6':
#         stack.clear()
#     elif choice == '7':
#         stack.peek()
#     elif choice == '0':
#         print("Программа завершена.")
#         break
#     else:
#         print("Некорректный выбор операции. Пожалуйста, выберите операцию из списка.")



# 3



# class DynamicStringStack:
#     def __init__(self):
#         self.stack = []      # В моем коде def __init__(self): self.stack = [], я инициализирую атрибут stack объекта класса DynamicStringStack пустым списком [ ] прямо внутри конструктора. Такой подход позволяет каждому объекту этого класса иметь свой собственный атрибут stack, который будет хранить строки, добавленные в стек и обслуживаться методами класса. Если бы я написал def __init__(self, stack): self.stack = stack, то при создании объекта класса DynamicStringStack я бы должен был передавать начальное значение для stack в качестве аргумента. Однако, в данном случае я хотел создать стек со значением по умолчанию (пустым списком), поэтому просто инициализировал self.stack как пустой список внутри конструктора
#
#     def push(self, string):
#         self.stack.append(string)
#         print(f"Строка {string} добавлена в стек")
#
#     def pop(self):
#         if not self.is_empty():
#             popped_string = self.stack.pop()
#             print(f"Строка {popped_string} удалена из стека")
#             return popped_string
#         else:
#             print("Стек Пуст")
#
#     def count(self):
#         print(f"Количество строк в стеке: {len(self.stack)}")
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def clear(self):
#         self.stack = []
#         print("Стек очищен")
#
#     def peek(self):
#         if not self.is_empty():
#             print(f"Верхняя строка в стеке: {self.stack[-1]}")
#         else:
#             print("Стек пуст")
#
# stack = DynamicStringStack()
#
# while True:
#     print("\nМеню операций:")
#     print("1. Добавить строку в стек")
#     print("2. Удалить строку из стека")
#     print("3. Количество строк в стеке")
#     print("4. Проверить, пуст ли стек")
#     print("5. Очистить стек")
#     print("6. Получить верхнюю строку в стеке без удаления")
#     print("0. Выход")
#
#     choice = input("Выберите операцию: ")
#
#     if choice == '1':
#         string = input("Введите строку для добавления в стек:")
#         stack.push(string)
#     elif choice == '2':
#         stack.pop()
#     elif choice == '3':
#         stack.count()
#     elif choice == '4':
#         print(f"Стек пуст: {stack.is_empty()}")
#     elif choice == '5':
#         stack.clear()
#     elif choice == '6':
#         stack.peek()
#     elif choice == '0':
#         print("Программа завершена")
#         break
#     else:
#         print("Некорректный выбор операции. Пожалуйста, выберите операцию из списка.")



