# Скрипт для корректировки электронного дневника

Данный скрипт предназначен для удаления плохих оценок (2 и 3), удаления замечаний от учителей и получения похвалы. 

## Запуск

Для корректной работы скрипта необходимо
- скопировать файл `scripts.py` в директорию электронного дневника рядом с файлом `manage.py`,
- запустить интерактивную консоль командой 
```python
python manage.py shell
```
- из базы данных импортировать модели командой
```python
from datacenter.models import *
```
- импортировать из нашего файла необходимые скрипты и библиотеки командами
```python
from random import choice
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from scripts import *
```
## Использование скрипта
- для удаления плохих оценок, а именно: двоек и троек, используем следующую команду в интерактивной консоли с указанием корректной фамилии и имени ученика
```python
fix_marks('Фролов Иван')
```
- для того, чтобы стереть все замечания из дневника, используем аналогично команду
```python
remove_chastisements('фролов Иван')
```
- для получения хвалебного сообщения от учителя пишем в консоли следующую команду с указанием конкретного предмета, от учителя по которому мы хотим получить благодарность
```python
create_commendation('Фролов Иван', 'Математика')
```
Похвала появляется в дневнике на случайно выбранном скриптом уроке по указанному предмету. Сообщения о похвале также пишутся разные, но могут повторяться, злоупотреблять не стоит.

## Возникновение ошибок
В случае неправильно введенной фамилии ученика, его имени или предмета, можно получить сообщение о том, что ученик не найден или наоборот найдено более одного ученика. Также может быть сообщение о некорректном написании предмета. В данном случае нужно будет повторить заново все шаги пункта "Запуск" и обратить внимание на правильность написания указанных параметров.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
