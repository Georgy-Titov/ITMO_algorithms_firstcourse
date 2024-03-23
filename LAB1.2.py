def guess_student(step, sl):
    if isinstance(sl, str):
        print(f'Человек найден. Это {sl}')
        exit(0)

    print(questions[step])
    ans = input()

    if ans not in sl:
        print('Такого человека не существует или данные введены некорректно')
        exit(0)
    guess_student(step + 1, sl[ans])


group = {"девочка": {"свтелые": {"да": {"курит": {"спорт": "Маркова Наталья", "не спорт": "Иванова София"},
                                        "не курит": "Калинина Алиса"},
                                 "нет": {"курит": "Копылова яна", "не курит": "Горбачева Алиса"}},
                     "темные": {"да": {"курит": "Лебедева Арина", "не курит": "Бессонова Анфиса"},
                                "нет": "Наумова Вероника"}},
         "мальчик": {"светлые": {"да": "Головин Степан",
                                 "нет": "Тимлфеев федор"},
                     "темные": {"да": {"курит": {"спорт": "Медведев Глеб",
                                                 "не спорт": "Комиссаров Алексей"},
                                       "не курит": "Трофимов Савелий"},
                                "нет": {"курит": {"спорт": {"да": "Рябов Никита", "нет": "Кузнецо Николай"}},
                                        "не курит": "Курочкин Константин"}}}}

questions = ["Какого пола загадданный человек? девочка/мальчик",
             "Какого цвета у человека волосы? светлые/темные",
             "Хорошие ли отметки у этого человека? да/нет",
             "Курит ли этот человек? курит/не курит",
             "Занимается ли этот человек в спортивных секциях ИТМО? спорт/не спорт",
             "Играет ли он за сборную ИТМО по мини-футболу? да/нет"]

print('Программа для поиска человека в группе. Ответьте на несколько вопросов')
guess_student(0, group)