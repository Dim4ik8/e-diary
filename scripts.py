from random import choice
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def find_schoolkid(schoolkid):
    try:
        kid = Schoolkid.objects.get(full_name__contains=schoolkid)
    except ObjectDoesNotExist:
        print('Ученик не найден, попробуй еще раз')
        exit()
    except MultipleObjectsReturned:
        print(f'Найдено несколько учеников {schoolkid}, укажите конкретнее! ')
        exit()
    return kid

def fix_marks(schoolkid):
    kid = find_schoolkid(schoolkid)
    marks = Mark.objects.filter(schoolkid=kid, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    kid = find_schoolkid(schoolkid)
    chast = Chastisement.objects.filter(schoolkid=kid)
    chast.delete()


def create_commendation(schoolkid, subject):
    kid = find_schoolkid(schoolkid)
    commendations = [
        'Молодец!', 'Отлично!', 'Хорошо!', 'Великолепно!',
        'Прекрасно!', 'Сказано здорово – просто и ясно!',
        'Очень хороший ответ!', 'Талантливо!', 'Уже существенно лучше!',
        'Потрясающе!', 'Замечательно!', 'Прекрасное начало!',
        'Так держать!', 'Ты на верном пути!', 'Здорово!',
        'Это как раз то, что нужно!', 'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
        'Ты растешь над собой!', 'Теперь у тебя точно все получится!'
    ]

    lesson = Lesson.objects.filter(
        year_of_study=kid.year_of_study,
        group_letter=kid.group_letter,
        subject__title=subject
    ).order_by('?').first()

    if not lesson:
        print('Проверьте правильность написания предмета!')
        exit()

    Commendation.objects.create(
        text=choice(commendations),
        created=lesson.date,
        schoolkid=kid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )