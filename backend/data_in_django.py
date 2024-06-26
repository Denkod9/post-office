from django.db import migrations


# TODO: Готово
# Добавление Улиы в таблицу
def add_address_street(apps, schema_editor):
    Street = apps.get_model('address', 'Street')

    Street.objects.create(type_street='Улица', street='Кремлевская наб')
    Street.objects.create(type_street='Улица', street='Ушинского')
    Street.objects.create(type_street='Улица', street='Дружбы')
    Street.objects.create(type_street='Улица', street='Корабельная')
    Street.objects.create(type_street='Бульвар', street='Машиностроения 1-я,')
    Street.objects.create(type_street='Проспект', street='Загородный 5-й проезд')
    Street.objects.create(type_street='Бульвар', street='Детский пер')
    Street.objects.create(type_street='Улица', street='Шоссейная 3-я')
    Street.objects.create(type_street='Улица', street='Военная Горка (3-я линия)')
    Street.objects.create(type_street='Проспект', street='Ананьевский пер')
    Street.objects.create(type_street='Улица', street='Графитный проезд')
    Street.objects.create(type_street='Улица', street='Ольховая')
    Street.objects.create(type_street='Проспект', street='Албазинская')
    Street.objects.create(type_street='Улица', street='Албазинская')
    Street.objects.create(type_street='Улица', street='Корабельная')
    Street.objects.create(type_street='Проспект', street='Рословка')
    Street.objects.create(type_street='Проспект', street='Палашевский М. пер')
    Street.objects.create(type_street='Проспект', street='Внешняя')
    Street.objects.create(type_street='Бульвар', street='Пенягинская')
    Street.objects.create(type_street='Бульвар', street='Корабельная')
    Street.objects.create(type_street='Улица', street='Ткачей')
    Street.objects.create(type_street='Проспект', street='Академика Миллионщикова')
    Street.objects.create(type_street='Бульвар', street='Албазинская')
    Street.objects.create(type_street='Улица', street='Богдана Хмельницкого')
    Street.objects.create(type_street='Улица', street='Мордовский Лог')
    Street.objects.create(type_street='Бульвар', street='Пестеля 1-я')
    Street.objects.create(type_street='Улица', street='Перерва')
    Street.objects.create(type_street='Проспект', street='Корабельная')
    Street.objects.create(type_street='Улица', street='Очаковский 5-й пер')
    Street.objects.create(type_street='Улица', street='Героев Революции')
    Street.objects.create(type_street='Бульвар', street='Сущевский Вал')
    Street.objects.create(type_street='Улица', street='Гэсстроевский 4-й пер')
    Street.objects.create(type_street='Бульвар', street='Корабельная')
    Street.objects.create(type_street='Улица', street='Очаковский 1-й пер')
    Street.objects.create(type_street='Улица', street='Мочищенский Спуск')
    Street.objects.create(type_street='Проспект', street='Международная')
    Street.objects.create(type_street='Улица', street='Жерновская 3-я')
    Street.objects.create(type_street='Бульвар', street='Шоссейная 3-я')
    Street.objects.create(type_street='Проспект', street='Шоссейная 3-я')
    Street.objects.create(type_street='Улица', street='Новоподмосковный 8-й пер')
    Street.objects.create(type_street='Бульвар', street='Жерновская 3-я')
    Street.objects.create(type_street='Улица', street='Прогонная 1-я')
    Street.objects.create(type_street='Проспект', street='Смоленский 1-й пер')
    Street.objects.create(type_street='Проспект', street='Шоссейная 3-я')
    Street.objects.create(type_street='Улица', street='Гончарный 1-й пер')
    Street.objects.create(type_street='Бульвар', street='Сетуньский 1-й проезд')
    Street.objects.create(type_street='Улица', street='Красногвардейский б-р')
    Street.objects.create(type_street='Проспект', street='Новоподмосковный 8-й пер')
    Street.objects.create(type_street='Бульвар', street='Летний сад')
    Street.objects.create(type_street='Улица', street='Токмаков пер')
    Street.objects.create(type_street='Улица', street='Смоленский 1-й пер')
    Street.objects.create(type_street='Бульвар', street='Лукьяновский проезд')

    # Street.objects.create(type_street='Улица', street='')

    # Street.objects.create(
    #     type_street='Улица',
    #     street=''
    # )


# TODO: Готово
# Добавление Типов Изданий в таблицу
def add_edition_types(apps, schema_editor):
    EditionType = apps.get_model('editions', 'EditionType')

    EditionType.objects.create(type_name='Журнал')
    EditionType.objects.create(type_name='Газета')
    EditionType.objects.create(type_name='Книга')
    EditionType.objects.create(type_name='Альмонах')
    EditionType.objects.create(type_name='Сборник')
    EditionType.objects.create(type_name='Ежегодник')
    EditionType.objects.create(type_name='Справочник')


# TODO: Готово
# Добавление Адресов в таблицу
def add_address(apps, schema_editor):
    Address = apps.get_model('address', 'Address')
    Street = apps.get_model('address', 'Street')

    Address.objects.create(street=Street.objects.get(id=1), house='110', flat='253')
    Address.objects.create(street=Street.objects.get(id=2), house='138', flat='605')
    Address.objects.create(street=Street.objects.get(id=3), house='66a', flat='619')
    Address.objects.create(street=Street.objects.get(id=4), house='17', flat='63')
    Address.objects.create(street=Street.objects.get(id=5), house='117в', flat='109')
    Address.objects.create(street=Street.objects.get(id=6), house='59', flat='853')
    Address.objects.create(street=Street.objects.get(id=7), house='194', flat='527')
    Address.objects.create(street=Street.objects.get(id=8), house='199', flat='225')
    Address.objects.create(street=Street.objects.get(id=9), house='132', flat='362')
    Address.objects.create(street=Street.objects.get(id=10), house='2а', flat='571')
    Address.objects.create(street=Street.objects.get(id=11), house='194', flat='370')
    Address.objects.create(street=Street.objects.get(id=12), house='68в', flat='795')
    Address.objects.create(street=Street.objects.get(id=13), house='170', flat='865')
    Address.objects.create(street=Street.objects.get(id=14), house='145', flat='395')
    Address.objects.create(street=Street.objects.get(id=15), house='96', flat='653')
    Address.objects.create(street=Street.objects.get(id=16), house='33', flat='58')
    Address.objects.create(street=Street.objects.get(id=17), house='162', flat='676')
    Address.objects.create(street=Street.objects.get(id=18), house='52', flat='865')
    Address.objects.create(street=Street.objects.get(id=19), house='145а', flat='358')
    Address.objects.create(street=Street.objects.get(id=20), house='99', flat='332')
    Address.objects.create(street=Street.objects.get(id=21), house='57', flat='978')
    Address.objects.create(street=Street.objects.get(id=22), house='69б', flat='962')
    Address.objects.create(street=Street.objects.get(id=23), house='143', flat='852')
    Address.objects.create(street=Street.objects.get(id=24), house='193', flat='402')
    Address.objects.create(street=Street.objects.get(id=25), house='128а', flat='502')
    Address.objects.create(street=Street.objects.get(id=26), house='147', flat='18')
    Address.objects.create(street=Street.objects.get(id=27), house='140', flat='1')
    Address.objects.create(street=Street.objects.get(id=28), house='77', flat='432')
    Address.objects.create(street=Street.objects.get(id=29), house='245', flat='531')
    Address.objects.create(street=Street.objects.get(id=30), house='36', flat='45')
    Address.objects.create(street=Street.objects.get(id=31), house='102', flat='815')
    Address.objects.create(street=Street.objects.get(id=32), house='120в', flat='836')
    Address.objects.create(street=Street.objects.get(id=33), house='78', flat='238')
    Address.objects.create(street=Street.objects.get(id=34), house='75', flat='145')
    Address.objects.create(street=Street.objects.get(id=35), house='124', flat='455')
    Address.objects.create(street=Street.objects.get(id=36), house='125', flat='13')
    Address.objects.create(street=Street.objects.get(id=37), house='189', flat='651')
    Address.objects.create(street=Street.objects.get(id=38), house='175', flat='827')
    Address.objects.create(street=Street.objects.get(id=39), house='145', flat='675')
    Address.objects.create(street=Street.objects.get(id=40), house='123', flat='149')
    Address.objects.create(street=Street.objects.get(id=41), house='138', flat='432')
    Address.objects.create(street=Street.objects.get(id=42), house='73', flat='952')
    Address.objects.create(street=Street.objects.get(id=43), house='111в', flat='259')
    Address.objects.create(street=Street.objects.get(id=44), house='86а', flat='40')
    Address.objects.create(street=Street.objects.get(id=45), house='2', flat='702')
    Address.objects.create(street=Street.objects.get(id=46), house='101', flat='662')
    Address.objects.create(street=Street.objects.get(id=47), house='19', flat='897')
    Address.objects.create(street=Street.objects.get(id=48), house='50', flat='198')
    Address.objects.create(street=Street.objects.get(id=49), house='125', flat='455')
    Address.objects.create(street=Street.objects.get(id=50), house='11', flat='788')
    Address.objects.create(street=Street.objects.get(id=51), house='3', flat='1')
    # Address.objects.create(street=Street.objects.get(id=), house='', flat='')

    # Address.objects.create(
    #     street=Street.objects.get(id=),
    #     house='',
    #     flat='',
    # )


# TODO: Готово
# Добавление Почтвого адреса и информации в таблицу
def add_address_post_office_info(apps, schema_editor):
    PostOfficeInfo = apps.get_model('address', 'PostOfficeInfo')
    Address = apps.get_model('address', 'Address')

    PostOfficeInfo.objects.create(
        title='Post Office',
        address=Address.objects.get(id=51),
        manager_info='Заведующий этой компании его почта politsa042@gmail.com, номер телефона +38 (050) 19-72-852'
    )
    PostOfficeInfo.objects.create(
        title='Post Delivery',
        address=Address.objects.get(id=11),
        manager_info='Заведующий этой компании его почта admin@gmail.com, номер телефона +38 (050) 19-72-852'
    )

    # PostOfficeInfo.objects.create(
    #     title='',
    #     address=Address.objects.get(id=),
    #     manager_info=''
    # )


# TODO: Готово
# Добавление Пользователей в таблицу
def add_users(apps, schema_editor):
    UserAccount = apps.get_model('accounts', 'UserAccount')
    Address = apps.get_model('address', 'Address')

    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        # last_login='2022-09-02 16:38:35.331420',
        is_superuser=1,
        email='a@a.com',
        first_name='admin',
        last_name='admin',
        date_of_birth='1994-05-04',
        role='ADMIN',
        phone='+38(050)334-94-88',
        address=Address.objects.get(id=51),
        is_active=1,
        is_staff=1
    )
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=1, email='politsa042@gmail.com', first_name='Den', last_name='Pro',
        date_of_birth='1991-04-03', role='MANAGER', phone='+38(050)529-44-99',
        address=Address.objects.get(id=51), is_active=1, is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=1, email='politsa044@gmail.com', first_name='Den', last_name='Pro',
        date_of_birth='1991-04-03', role='OPERATOR', phone='+38(050)242-56-86',
        address=Address.objects.get(id=51), is_active=1, is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='valentinsidorov110@gmail.com', first_name='Валентин',
        last_name='Сидоров', date_of_birth='1989-08-21', role='SUBSCRIBER',
        phone='+38(050)812-89-96', address=Address.objects.get(id=1), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='kseniyamalysheva342@gmail.com', first_name='Ксения',
        last_name='Малышева', date_of_birth='2000-07-29', role='SUBSCRIBER',
        phone='+38(050)312-80-08', address=Address.objects.get(id=2), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='seliverstkudryavtsev60@gmail.com', first_name='Селиверст',
        last_name='Кудрявцев', date_of_birth='1984-01-01', role='SUBSCRIBER',
        phone='+38(050)370-77-06', address=Address.objects.get(id=3), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='larisatihomirova547@gmail.com', first_name='Лариса',
        last_name='Тихомирова', date_of_birth='2000-01-18', role='SUBSCRIBER',
        phone='+38(050)485-17-13', address=Address.objects.get(id=4), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='nikamironova213@gmail.com', first_name='Ника',
        last_name='Миронова', date_of_birth='1985-06-20', role='SUBSCRIBER',
        phone='+38(050)353-25-05', address=Address.objects.get(id=5), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='melanyazagitova804@gmail.com', first_name='Меланья',
        last_name='Загитова', date_of_birth='1986-05-09', role='SUBSCRIBER',
        phone='+38(050)277-27-68', address=Address.objects.get(id=6), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='maksimilyandidichenko499@gmail.com', first_name='Максимильян',
        last_name='Дидиченко', date_of_birth='2002-04-19', role='SUBSCRIBER',
        phone='+38(050)499-19-50', address=Address.objects.get(id=7), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='liyakrasnova274@gmail.com', first_name='Лия',
        last_name='Краснова', date_of_birth='1986-04-02', role='SUBSCRIBER',
        phone='+38(050)290-20-95', address=Address.objects.get(id=8), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='osipmamedov859@gmail.com', first_name='Осип',
        last_name='Мамедов', date_of_birth='1987-05-22', role='SUBSCRIBER',
        phone='+38(050)869-16-26', address=Address.objects.get(id=9), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='kallistratkukolevskiy66@gmail.com', first_name='Каллистрат',
        last_name='Куколевский', date_of_birth='1987-10-16', role='SUBSCRIBER',
        phone='+38(050)272-95-84', address=Address.objects.get(id=10), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='serafimchernyshov6@gmail.com', first_name='Серафим',
        last_name='Чернышов', date_of_birth='1988-07-01', role='SUBSCRIBER',
        phone='+38(050)561-72-87', address=Address.objects.get(id=11), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='rozaandreeva541@gmail.com', first_name='Роза',
        last_name='Андреева', date_of_birth='1983-07-08', role='SUBSCRIBER',
        phone='+38(050)778-87-47', address=Address.objects.get(id=12), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='modestkrymskiy539@gmail.com', first_name='Модест',
        last_name='Крымский', date_of_birth='1993-10-25', role='SUBSCRIBER',
        phone='+38(050)177-79-49', address=Address.objects.get(id=13), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='dominikarodochinskaya566@gmail.com', first_name='Доминика',
        last_name='Родочинская', date_of_birth='1999-08-05', role='SUBSCRIBER',
        phone='+38(050)211-89-56', address=Address.objects.get(id=14), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='vladilenarzaeva32@gmail.com', first_name='Владилена',
        last_name='Рзаева', date_of_birth='1995-02-28', role='SUBSCRIBER',
        phone='+38(050)282-56-91', address=Address.objects.get(id=15), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='karppodorozhnyy214@gmail.com', first_name='Карп',
        last_name='Подорожный', date_of_birth='1996-08-30', role='SUBSCRIBER',
        phone='+38(050)792-54-91', address=Address.objects.get(id=16), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='agniyadidichenko676@gmail.com', first_name='Агния',
        last_name='Дидиченко', date_of_birth='1983-09-21', role='SUBSCRIBER',
        phone='+38(050)782-62-28', address=Address.objects.get(id=17), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='emmaprosvetova396@gmail.com', first_name='Эмма',
        last_name='Просветова', date_of_birth='1977-12-25', role='SUBSCRIBER',
        phone='+38(050)738-15-60', address=Address.objects.get(id=18), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='beatrisastalina36@gmail.com', first_name='Беатриса',
        last_name='Сталина', date_of_birth='1996-05-13', role='SUBSCRIBER',
        phone='+38(050)877-31-13', address=Address.objects.get(id=19), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='bernarlapin395@gmail.com', first_name='Бернар',
        last_name='Лапин', date_of_birth='1976-08-31', role='SUBSCRIBER',
        phone='+38(050)462-39-77', address=Address.objects.get(id=20), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='nataliyaohotnikova319@gmail.com', first_name='Наталия',
        last_name='Охотникова', date_of_birth='1994-10-31', role='SUBSCRIBER',
        phone='+38(050)089-30-67', address=Address.objects.get(id=21), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='samsonveshtiy544@gmail.com', first_name='Самсон',
        last_name='Вещий', date_of_birth='2002-09-13', role='SUBSCRIBER',
        phone='+38(050)068-52-99', address=Address.objects.get(id=22), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='vladislavzhdanov898@gmail.com', first_name='Владислав',
        last_name='Жданов', date_of_birth='1993-10-17', role='SUBSCRIBER',
        phone='+7 (976) 515-18-20', address=Address.objects.get(id=23), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='svyatopolkvasyutin796@gmail.com', first_name='Святополк',
        last_name='Васютин', date_of_birth='1987-09-15', role='SUBSCRIBER',
        phone='+38(050)674-88-88', address=Address.objects.get(id=24), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='matveyzhdanov642@gmail.com', first_name='Матвей',
        last_name='Жданов', date_of_birth='1972-10-01', role='SUBSCRIBER',
        phone='+38(050)516-49-48', address=Address.objects.get(id=25), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='radasergeeva283@gmail.com', first_name='Рада',
        last_name='Сергеева', date_of_birth='1984-12-17', role='SUBSCRIBER',
        phone='+38(050)273-24-10', address=Address.objects.get(id=26), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='innokentiysokolov404@gmail.com', first_name='Иннокентий',
        last_name='Соколов', date_of_birth='1984-07-24', role='SUBSCRIBER',
        phone='+38(050)780-07-01', address=Address.objects.get(id=27), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='hristoforrepin413@gmail.com', first_name='Христофор',
        last_name='Репин', date_of_birth='1977-08-19', role='SUBSCRIBER',
        phone='+38(050)753-64-29', address=Address.objects.get(id=28), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='mariyakozhina223@gmail.com', first_name='Мария',
        last_name='Кожина', date_of_birth='1982-12-09', role='SUBSCRIBER',
        phone='+38(050)363-30-23', address=Address.objects.get(id=29), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='arkadiyyakovenko992@gmail.com', first_name='Аркадий',
        last_name='Яковенко', date_of_birth='1988-06-10', role='SUBSCRIBER',
        phone='+38(050)965-48-59', address=Address.objects.get(id=30), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='angelinaegorova319@gmail.com', first_name='Ангелина',
        last_name='Егорова', date_of_birth='1998-12-25', role='SUBSCRIBER',
        phone='+38(050)406-20-77', address=Address.objects.get(id=31), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='anatoliypolyakov90@gmail.com', first_name='Анатолий',
        last_name='Поляков', date_of_birth='1986-08-21', role='SUBSCRIBER',
        phone='+38(050)304-72-46', address=Address.objects.get(id=32), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='nikonrubentsov738@gmail.com', first_name='Никон',
        last_name='Рубенцов', date_of_birth='1997-04-23', role='SUBSCRIBER',
        phone='+38(050)009-12-34', address=Address.objects.get(id=33), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='antonidadementeva640@gmail.com', first_name='Антонида',
        last_name='Дементьева', date_of_birth='2000-09-19', role='SUBSCRIBER',
        phone='+38(050)097-85-64', address=Address.objects.get(id=34), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='elenashmidt124@gmail.com', first_name='Елена',
        last_name='Шмидт', date_of_birth='1988-11-05', role='SUBSCRIBER',
        phone='+38(050)613-69-05', address=Address.objects.get(id=35), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='viktorshapovalov74@gmail.com', first_name='Виктор',
        last_name='Шаповалов', date_of_birth='1981-03-05', role='SUBSCRIBER',
        phone='+38(050)199-44-61', address=Address.objects.get(id=36), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='valeryanvirskiy430@gmail.com', first_name='Валерьян',
        last_name='Вирский', date_of_birth='1995-04-18', role='SUBSCRIBER',
        phone='+38(050)706-04-12', address=Address.objects.get(id=37), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='gremislavmilovanov716@gmail.com', first_name='Гремислав',
        last_name='Милованов', date_of_birth='1991-01-18', role='SUBSCRIBER',
        phone='+38(050)003-66-87', address=Address.objects.get(id=38), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='yuriylavrentev905@gmail.com', first_name='Юрий',
        last_name='Лаврентьев', date_of_birth='1992-12-21', role='SUBSCRIBER',
        phone='+38(050)909-81-50', address=Address.objects.get(id=39), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='liliyasorokina282@gmail.com', first_name='Лилия',
        last_name='Сорокина', date_of_birth='1988-01-05', role='SUBSCRIBER',
        phone='+38(050)407-97-84', address=Address.objects.get(id=40), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='iraidazagitova758@gmail.com', first_name='Ираида',
        last_name='Загитова', date_of_birth='1982-03-01', role='SUBSCRIBER',
        phone='+38(050)915-32-88', address=Address.objects.get(id=41), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='evgeniyashapovalova332@gmail.com', first_name='Евгения',
        last_name='Шаповалова', date_of_birth='1991-02-18', role='SUBSCRIBER',
        phone='+38(050)810-59-78', address=Address.objects.get(id=42), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='marinaizofatova182@gmail.com', first_name='Марина',
        last_name='Изофатова', date_of_birth='1983-04-14', role='SUBSCRIBER',
        phone='+38(050)887-03-83', address=Address.objects.get(id=43), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='georgiysharipov632@gmail.com', first_name='Георгий',
        last_name='Шарипов', date_of_birth='1994-03-21', role='SUBSCRIBER',
        phone='+38(050)907-69-12', address=Address.objects.get(id=44), is_active=1,
        is_staff=1)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='naumlevchenko365@gmail.com', first_name='Наум',
        last_name='Левченко', date_of_birth='1992-05-10', role='SUBSCRIBER',
        phone='+38(050)372-56-18', address=Address.objects.get(id=45), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='miheyefimov142@gmail.com', first_name='Михей',
        last_name='Ефимов', date_of_birth='1986-02-19', role='SUBSCRIBER',
        phone='+38(050)280-16-80', address=Address.objects.get(id=46), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='fadeyantonov570@gmail.com', first_name='Фадей',
        last_name='Антонов', date_of_birth='1981-04-11', role='SUBSCRIBER',
        phone='+38(050)774-06-78', address=Address.objects.get(id=47), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='antoninmartynov116@gmail.com', first_name='Антонин',
        last_name='Мартынов', date_of_birth='2004-05-18', role='SUBSCRIBER',
        phone='+38(050)862-88-47', address=Address.objects.get(id=48), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='agrafenashershova863@gmail.com', first_name='Аграфена',
        last_name='Шершова', date_of_birth='1989-11-02', role='SUBSCRIBER',
        phone='+38(050)587-94-77', address=Address.objects.get(id=49), is_active=1,
        is_staff=0)
    UserAccount.objects.create(
        password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
        is_superuser=0, email='izotartimovich654@gmail.com', first_name='Изот',
        last_name='Артимович', date_of_birth='2002-09-21', role='SUBSCRIBER',
        phone='+38(050)886-43-02', address=Address.objects.get(id=50), is_active=1,
        is_staff=0)

    # UserAccount.objects.create(
    #     password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
    #     is_superuser=0, email='valentinsidorov110@gmail.com', first_name='',
    #     last_name='', date_of_birth='1989-08-21', role='SUBSCRIBER',
    #     phone='', address=Address.objects.get(id=), is_active=1,
    #     is_staff=0)

    # UserAccount.objects.create(
    #     password='pbkdf2_sha256$390000$RgEMctXIR4bJBdULPdoyZV$CEJ2saiy01sxniWbhl0yslxn7xO/14Uj8yZZ2QAXXww=',
    #     is_superuser=0,
    #     email='valentinsidorov110@gmail.com',
    #     first_name='',
    #     last_name='',
    #     date_of_birth='1989-08-21',
    #     role='SUBSCRIBER',
    #     phone='+38(050)508-76-31',
    #     address=Address.objects.get(id=),
    #     is_active=1,
    #     is_staff=0
    # )


# TODO: Готово
# Добавление Изданий в таблицу
def add_editions(apps, schema_editor):
    Edition = apps.get_model('editions', 'Edition')
    EditionType = apps.get_model('editions', 'EditionType')

    Edition.objects.create(
        image='1.jpg',
        index='55290',
        title='Автомобилестроение',
        price='5982',
        edition_type=EditionType.objects.get(id=1),
        description='Информационный бюллетень. Издание Всероссийского института научной и технической информации Российской академии наук (ВИНИТИ РАН).'
    )
    Edition.objects.create(
        image='2.jpg',
        index='27839',
        title='Автомобильная промышленность',
        price='4360',
        edition_type=EditionType.objects.get(id=2),
        description='Освещает отечественный и зарубежный опыт в области экономики и организации производства; конструирования, испытаний и обслуживания автомототехники; технологий, оборудования и материалов.'
    )
    Edition.objects.create(
        image='3.jpg',
        index='29489',
        title='Автомобильный транспорт',
        price='2713',
        edition_type=EditionType.objects.get(id=2),
        description='Журнал издается с 1923 г. для профессионалов автотранспорта. Информирует об опыте организации грузовых и пассажирских перевозок, новостях автомобильной техники, ТО и ремонте, БДД, экономике, законодательстве автотранспорта и др.'
    )
    Edition.objects.create(
        image='4.jpg',
        index='55291',
        title='Автомобильный транспорт',
        price='420',
        edition_type=EditionType.objects.get(id=4),
        description='Информационный бюллетень. Издание Всероссийского института научной и технической информации Российской академии наук (ВИНИТИ РАН).'
    )
    Edition.objects.create(
        image='5.jpg',
        index='36744',
        title='Автомобильный транспорт: грузовые перевозки',
        price='7820',
        edition_type=EditionType.objects.get(id=5),
        description='Издается с 2008г. Руководителям АТП, ПАТП, начальникам транспортных подразделений промышленных предприятий, топ-менеджерам структурных подразделений; руководителям и специалистам отделов логистики, служб закупок и снабжения, коммерческим директорам, а также всем заинтересованным специалистам. Регулирование: законодательные акты и инициативы, таможенное регулирование, межправительственные соглашения, региональные программы, контроль автоперевозок. Проекты. Комплексные решения: проекты и решения транспортных компаний, дорожная и придорожная инфраструктура.'
    )
    Edition.objects.create(
        image='6.jpg',
        index='13647',
        title='Автопанорама',
        price='659',
        edition_type=EditionType.objects.get(id=4),
        description='Эксклюзивные тесты суперкаров. Статьи о выдающихся машинах, раритетных выставочных концептах, экспедициях во все части света. История автомобилей, материалы о ремонте и сервисном обслуживании, обзоры предложений тюнинговых компаний, цены в автосалонах.'
    )
    Edition.objects.create(
        image='7.jpg',
        index='10444',
        title='Автопарк - 5 колесо',
        price='525',
        edition_type=EditionType.objects.get(id=7),
        description='Для профессионалов в области коммерческого транспорта. Новинки, грузовая, строительная и специализированная техника. Материалы по подвижному составу, экономика отрасли, технологии. Тесты.'
    )
    Edition.objects.create(
        image='8.jpg',
        index='16618',
        title='АВТОТРАНСПОРТ: ЭКСПЛУАТАЦИЯ - ОБСЛУЖИВАНИЕ - РЕМОНТ',
        price='892',
        edition_type=EditionType.objects.get(id=6),
        description='Единственный в России научно-практический журнал для руководителей автотранспортных и авторемонтных предприятий, технического персонала транспортных цехов, специалистов-диагностов, водителей всех категорий автотранспортных средств по комплексу вопросов эксплуатации, обслуживания и ремонта транспортных средств для коммерческого использования.'
    )
    Edition.objects.create(
        image='9.jpg',
        index='14471',
        title='Academia. Архитектура и строительство',
        price='997',
        edition_type=EditionType.objects.get(id=1),
        description='Научные статьи по архитектуре, градостроительству и строительству, написанные членами Академии архитектуры и строительных наук, ее советниками, сотрудниками академических институтов, ведущими специалистами в этих областях.'
    )
    Edition.objects.create(
        image='10.jpg',
        index='45010',
        title='Construction and Geotechnics (старое название Вестник ПНИПУ. Строительство и архитектура)',
        price='2669',
        edition_type=EditionType.objects.get(id=2),
        description='Журнал предназначен для научных сотрудников, специализирующихся в области архитектуры и строительных наук, студентов старших курсов, обучающихся по направлению "Строительство".'
    )
    Edition.objects.create(
        image='11.jpg',
        index='73193',
        title='АКАДЕМИЧЕСКИЙ ВЕСТНИК УРАЛНИИПРОЕКТ РААСН',
        price='259',
        edition_type=EditionType.objects.get(id=2),
        description='Журнал освещает широкий круг вопросов по архитектуре, градостроительству, строительным наукам, технической эстетике, а также проблемы социально-гуманитарного развития общества. Журнал предназначен для ученых, архитекторов и градостроителей, а также для студентов, магистрантов, аспирантов, докторантов.'
    )
    Edition.objects.create(
        image='12.jpg',
        index='41056',
        title='АКВА-ТЕРМ',
        price='1321',
        edition_type=EditionType.objects.get(id=3),
        description='Журнал для специалистов по отоплению, водоснабжению и водоподготовке.'
    )
    Edition.objects.create(
        image='13.jpg',
        index='29254',
        title='Архитектура и строительство России',
        price='1346',
        edition_type=EditionType.objects.get(id=3),
        description='Журнал по архитектуре, градостроительству, садово-парковому дизайну, экологии среды обитания, строительным материалам и технологиям, дизайну интерьеров и мебели. Включен в Перечень ВАК.'
    )
    Edition.objects.create(
        image='14.jpg',
        index='79619',
        title='Архитектура, строительство, транспорт',
        price='988',
        edition_type=EditionType.objects.get(id=7),
        description='Научно-информационное издание посвящено рассмотрению широкого круга вопросов теоретического и практического характера, направленных на решение проблем в области архитектуры, строительства и транспорта'
    )
    Edition.objects.create(
        image='15.jpg',
        index='85502',
        title='Бетон и железобетон',
        price='188',
        edition_type=EditionType.objects.get(id=7),
        description='Научные исследования в области материаловедения, технологии бетонов, конструкций из бетона и железобетона, практика строительства. WWW.RIFSM.RU'
    )
    Edition.objects.create(
        image='16.jpg',
        index='42231',
        title='Вентиляция, отопление, кондиционирование воздуха, теплоснабжение и строительная теплофизика (АВОК)',
        price='2266',
        edition_type=EditionType.objects.get(id=6),
        description='Журнал о современных системах ОВК, энергоэффективном строительстве в России и за рубежом, новых нормативных документах и стандартах.'
    )
    Edition.objects.create(
        image='17.jpg',
        index='41629',
        title='Information Security/ Информационная безопасность',
        price='373',
        edition_type=EditionType.objects.get(id=6),
        description='Системы защиты информации в компьютерных системах, объектовое обеспечение информационной безопасности, специальные технологии и средства информационной защиты и анализа информации www.icenter.ru'
    )
    Edition.objects.create(
        image='18.jpg',
        index='00103',
        title='SECURITY SAFETY MARKET IN RUSSIA(на русском языку)',
        price='782',
        edition_type=EditionType.objects.get(id=6),
        description='Маркетологам и руководителям, отвечающим за развитие бизнеса; специалистам по безопасности; дистрибьюторам оборудования и систем безопасности; сотрудникам российских правительств зарубежных компаний. Бюллетень создан для того, чтобы упорядочивать и отслеживать тенденции рынка безопасности в России, является также базой для изучения примеров интеграции зарубежного бизнеса на российский рынок и отслеживания рынка в целом. Российское регулирование. Слияния и поглощения. Дистрибьюторские соглашения и технологическое партнерство.'
    )
    Edition.objects.create(
        image='19.jpg',
        index='11440',
        title='STOP-газета',
        price='886',
        edition_type=EditionType.objects.get(id=6),
        description='Основная задача газеты - воспитание законопослушного участника дорожного движения. Регулярно публикует аналитические материалы по ситуации с безопасностью дорожного движения на дорогах России и мира'
    )
    Edition.objects.create(
        image='20.jpg',
        index='85480',
        title='Адвокатская практика',
        price='891',
        edition_type=EditionType.objects.get(id=6),
        description='Практический журнал для адвоката. В журнале даются советы по составлению процессуальных документов, освещается деятельность Федеральной палаты адвокатов, адвокатских палат субъектов РФ.'
    )
    Edition.objects.create(
        image='21.jpg',
        index='11162',
        title='Административное право и процесс',
        price='1098',
        edition_type=EditionType.objects.get(id=5),
        description='Журнал предназначен для практического решения актуальных вопросов в области административной юрисдикции, для решения вопросов в области административно-правовой организации управления экономикой.'
    )
    Edition.objects.create(
        image='22.jpg',
        index='85473',
        title='Арбитражный и гражданский процесс',
        price='1106',
        edition_type=EditionType.objects.get(id=5),
        description='Комментарии АПК, ГПК, разрешение экономических споров судами. Особенности производства по делам о банкротстве, производство по делам с участием иностранных лиц, обобщение судебной и арбитражной практики, вопросы исполнения судебных решений, исполнительное производство. Правовое положение иностранцев и лиц без гражданства в гражданском процессе. Доказательственное право. Несудебные формы защиты.'
    )
    Edition.objects.create(
        image='23.jpg',
        index='91886',
        title='Безопасность бизнеса',
        price='724',
        edition_type=EditionType.objects.get(id=4),
        description='Журнал посвящен правовым проблемам безопасности бизнеса, судебной практике, защите прав предпринимателей, актуальным проблемам правового сопровождения предпринимательской деятельности. Также изданием рассматривается такой вопрос как юридическая защита предпринимателей и прав налогоплательщиков.'
    )
    Edition.objects.create(
        image='24.jpg',
        index='41829',
        title='Безопасность в нефтегазовом комплексе',
        price='7820',
        edition_type=EditionType.objects.get(id=4),
        description='Издается с 2005г. Главным инженерам и технологам, начальникам лабораторий НК и ТД, экологам, начальникам служб безопасности и охраны компаний нефтегазового комплекса. Производителям и поставщикам противопожарного, экологического, антикоррозийного, изоляционного, взрывозащитного оборудования для транспортных магистралей и объектов НГК, комплексных систем безопасности и охраны, антитеррористических средств, средств индивидуальной защиты.'
    )
    Edition.objects.create(
        image='25.jpg',
        index='41047',
        title='Ars Administrandi',
        price='719',
        edition_type=EditionType.objects.get(id=3),
        description='Журнал «ARS ADMINISTRANDI» («Искусство управления») является научным изданием и адресован специалистам в сфере государственного и муниципального управления: исследователям, управленцам – практикам, преподавателям вузов, а также широкому кругу читателей, интересующихся вопросами развития государственного управления и местного самоуправления в России и за рубежом. В журнале публикуются авторские статьи по фундаментальным и прикладным проблемам в сфере государственного и муниципального управления, экономики и политологии.'
    )
    Edition.objects.create(
        image='26.jpg',
        index='18931',
        title='Business Excellence (Деловое совершенство)',
        price='272',
        edition_type=EditionType.objects.get(id=3),
        description='Лучшие российские и зарубежные эталоны ведения бизнеса, успешные технологии построения бизнес-процессов и сокращения издержек. Методики повышения качества, формирования команды и воспитания лидерских навыков сотрудников.'
    )
    Edition.objects.create(
        image='27.jpg',
        index='33341',
        title='Business Excellence (Деловое совершенство)(годовая)',
        price='1626',
        edition_type=EditionType.objects.get(id=3),
        description='Лучшие российские и зарубежные эталоны ведения бизнеса, успешные технологии построения бизнес-процессов и сокращения издержек. Методики повышения качества, формирования команды и воспитания лидерских навыков сотрудников.'
    )
    Edition.objects.create(
        image='28.jpg',
        index='79134',
        title='E-Management',
        price='916',
        edition_type=EditionType.objects.get(id=3),
        description='Журнал издается с 2018 года. Целевую аудиторию журнала составляют отечественные и зарубежные специалисты-практики, изучающие аспекты электронного менеджмента, применения технологий искусственного интеллекта в управлении, а также преподаватели, научные сотрудники, докторанты, аспиранты и магистранты российских и зарубежных научных, исследовательских и образовательных учреждений и организаций, интересующиеся данными вопросами. Журнал включен в Перечень ВАК по следующим направлениям: 5.2.3 Региональная и отраслевая экономика; 5.2.5. Мировая экономика; 5.2.6. Менеджмент.'
    )
    Edition.objects.create(
        image='29.jpg',
        index='32998',
        title='HR-менеджмент. Практика управления персоналом',
        price='782',
        edition_type=EditionType.objects.get(id=7),
        description='Издается с 2010г. Топ-менеджерам государственных и коммерческих организаций. Руководителям и специалистам кадровых служб, отделов обучения и развития персонала. Директорам и менеджерам служб управления персоналом. Сотрудникам кадровых агентств и консалтинговых компаний. Внутренним аудиторам, тренерам и психологам компаний. Государственное регулирование. Партнерство. Соглашения. Комплексные решения: опыт компаний; сертификация. Лицензирование. Стандарты. Практические аспекты: технологии управления персоналом, информационное обеспечение, практика решения трудовых вопросов, организация работы HR-службы. Индикаторы развития: тенденции, аналитика, обзоры, экспертные мнения. Проблемы. Конфликты. Инциденты. ТОП Мероприятия. Информационный бюллетень. www.icenter.ru'
    )
    Edition.objects.create(
        image='30.jpg',
        index='41639',
        title='Information Security/ Информационная безопасность',
        price='373',
        edition_type=EditionType.objects.get(id=1),
        description='Системы защиты информации в компьютерных системах, объектовое обеспечение информационной безопасности, специальные технологии и средства информационной защиты и анализа информации www.icenter.ru'
    )
    Edition.objects.create(
        image='31.jpg',
        index='00254',
        title='IT EXPERT / ИТ ИНФРАСТРУКТУРА БИЗНЕСА',
        price='1701',
        edition_type=EditionType.objects.get(id=1),
        description='Справочник по выбору устройств и программного обеспечения для различных задач как в бизнесе, так и повседневной жизни. Руководство пользователя по самостоятельной настройке и применению современных технологий в офисе и дома. Обзоры и тесты оборудования и ПО, ответы на вопросы.'
    )
    Edition.objects.create(
        image='32.jpg',
        index='00256',
        title='IT MANAGER / АДМИНИСТРАТОР ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ',
        price='2036',
        edition_type=EditionType.objects.get(id=2),
        description='Бизнес-издание в сфере управления и решения технических задач с использованием информационных технологий. Развитие и трансформация бизнеса и государственного сектора в эпоху развития цифровой экономики.'
    )
    Edition.objects.create(
        image='33.jpg',
        index='11869',
        title='Автономные учреждения: акты и комментарии для бухгалтера',
        price='1666',
        edition_type=EditionType.objects.get(id=2),
        description='В журнале «Автономные учреждения: акты и комментарии для бухгалтера» публикуются тексты новых документов, затрагивающих финансово-хозяйственную деятельность этих учреждений, и даются комментарии к ним. Разъяснения по спорным вопросам применения налогового законодательства и законодательства РФ, регламентирующего правила ведения бухгалтерского учета, содержатся в письмах Минфина и ФНС, наиболее интересные из которых (а также комментарии к ним) приводятся на страницах журнала.'
    )
    Edition.objects.create(
        image='34.jpg',
        index='00049',
        title='Автономные учреждения: акты и комментарии для бухгалтера(годовая)',
        price='1361',
        edition_type=EditionType.objects.get(id=1),
        description='В журнале «Автономные учреждения: акты и комментарии для бухгалтера» публикуются тексты новых документов, затрагивающих финансово-хозяйственную деятельность этих учреждений, и даются комментарии к ним. Разъяснения по спорным вопросам применения налогового законодательства и законодательства РФ, регламентирующего правила ведения бухгалтерского учета, содержатся в письмах Минфина и ФНС, наиболее интересные из которых (а также комментарии к ним) приводятся на страницах журнала.'
    )
    Edition.objects.create(
        image='35.jpg',
        index='15068',
        title='Автономные учреждения: бухгалтерский учет и налогообложение',
        price='3625',
        edition_type=EditionType.objects.get(id=1),
        description='В издании всегда освещаются актуальные темы, касающиеся организации и ведения бухгалтерского и налогового учета, составления бухгалтерской и иной отчетности автономных учреждений, последние изменения в законодательстве, приводятся разъяснения специалистов органов государственной власти, ответы на вопросы читателей, обзоры новостей и другая полезная информация. Весь материал излагается в доступной форме, с практическими примерами и корреспонденцией счетов.'
    )
    Edition.objects.create(
        image='36.jpg',
        index='00048',
        title='Автономные учреждения: бухгалтерский учет и налогообложение(годовая)',
        price='285',
        edition_type=EditionType.objects.get(id=2),
        description='В издании всегда освещаются актуальные темы, касающиеся организации и ведения бухгалтерского и налогового учета, составления бухгалтерской и иной отчетности автономных учреждений, последние изменения в законодательстве, приводятся разъяснения специалистов органов государственной власти, ответы на вопросы читателей, обзоры новостей и другая полезная информация. Весь материал излагается в доступной форме, с практическими примерами и корреспонденцией счетов.'
    )
    Edition.objects.create(
        image='37.jpg',
        index='47480',
        title='АУДИТ',
        price='108',
        edition_type=EditionType.objects.get(id=4),
        description='Новое в аудите, бухучете, налогах, законодательстве, интервью, консультации, советы, анализ, статистика, события аудита, управление, кадры, финансы.'
    )
    Edition.objects.create(
        image='38.jpg',
        index='38910',
        title='Аудит и финансовый анализ / Audit and Financial Analysis',
        price='1219',
        edition_type=EditionType.objects.get(id=5),
        description='Журнал входит в перечень СМИ, рекомендуемых ВАК для публикации научных результатов кандидатских и докторских диссертаций: по экономике, управлению, вычислительной технике и информатике.'
    )
    Edition.objects.create(
        image='39.png',
        index='43050',
        title='Аудитор',
        price='433',
        edition_type=EditionType.objects.get(id=5),
        description='Научно-практический журнал для аудиторов, бухгалтеров, руководителей, преподавателей и научных сотрудников. Рубрики: теория и практика аудита, внутренний аудит, учет и отчетность, диагностика и прогнозирование, международные стандарты. Входит в Перечень ВАК.'
    )
    Edition.objects.create(
        image='40.jpg',
        index='80698',
        title='Аудиторские ведомости',
        price='2382',
        edition_type=EditionType.objects.get(id=5),
        description='На страницах журнала обсуждаются вопросы дальнейшего развития рынка аудиторских услуг, формирования стратегии работы аудиторских компаний, организации и осуществления контроля качества аудита, внедрения МСА, практики применения МСФО, включая алгоритмы действий по решению трудных и спорных вопросов аудиторской практики и многое другое.'
    )
    Edition.objects.create(
        image='41.jpg',
        index='18346',
        title='Берг-Коллегия',
        price='525',
        edition_type=EditionType.objects.get(id=5),
        description='Промышленная безопасность. Энергетика. Экология.'
    )
    Edition.objects.create(
        image='42.jpg',
        index='29003',
        title='Бурение и нефть',
        price='621',
        edition_type=EditionType.objects.get(id=5),
        description='Материалы о новейших научно-технических и технологических разработках, применяемых в нефтегазовой отрасли, а также статьи по проблемам экономики, экологии, права; экспертиза, статистика, зарубежный опыт.'
    )
    Edition.objects.create(
        image='43.jpg',
        index='45162',
        title='Вестник Владикавказского научного центра',
        price='2553',
        edition_type=EditionType.objects.get(id=6),
        description='В журнале публикуются научные статьи по вопросам истории, общества, языкознания, литературоведения, экологии, экономики, региональной политики, наук о Земле.'
    )
    Edition.objects.create(
        image='44.jpg',
        index='82102',
        title='Вестник ЗабГУ(годовая)',
        price='703',
        edition_type=EditionType.objects.get(id=7),
        description='Журнал представляет собой сборник оригинальных и обзорных научных статей по политологии, экономическим наукам, науках о земле. Издание входит в Перечень ВАК.'
    )
    Edition.objects.create(
        image='45.jpg',
        index='13015',
        title='3/9 царство',
        price='369',
        edition_type=EditionType.objects.get(id=7),
        description='В красочных комиксах и веселых сказках читателей ждут необычные встречи с героями русского фольклора. Интересные и сложные головоломки, конкурсы, ценные призы для подписчиков.'
    )
    Edition.objects.create(
        image='46.jpg',
        index='39192',
        title='ENGLISH. Книги для чтения на английском языке для школьников',
        price='1198',
        edition_type=EditionType.objects.get(id=7),
        description='Увлекательные книги на английском языке с упражнениями и словарём, адаптированные для учащихся школы. В первом полугодии 2023г. выходят: "Жар-птица и другие чудесные сказки", "Кот в сапогах"; "Тайна волшебного замка"; "Легенды о Робин Гуде"; "Мэри Поппинс"; "Экскалибур. Меч короля Артура". В подписке повторно.'
    )
    Edition.objects.create(
        image='47.jpg',
        index='39189',
        title='ENGLISH. Читаем вместе детские сказки',
        price='871',
        edition_type=EditionType.objects.get(id=6),
        description='Красочно иллюстрированные ДЕТСКИЕ СКАЗКИ НА АНГЛИЙСКОМ ЯЗЫКЕ с занимательными упражнениями и словарём, адаптированы для детей дошкольного и младшего школьного возраста. В первом полугодии 2023 г. выходят: "Колобок"; "Как обезьяна медузу перехитрила"; "Лисичка-сестричка и братец волк"; "Мужик и заяц"; "Сказка о рыбаке"; "Ученик чародея". В подписке повторно.'
    )
    Edition.objects.create(
        image='48.jpg',
        index='43134',
        title='А почему? Приложение к журналу "Юный техник"',
        price='1444',
        edition_type=EditionType.objects.get(id=6),
        description='Для детей о науке, природе, путешествиях в ответах на вопросы. Сказки, комиксы, игротека помогут приятно и творчески провести досуг.'
    )
    Edition.objects.create(
        image='49.jpg',
        index='81202',
        title='1001 совет и секрет',
        price='557',
        edition_type=EditionType.objects.get(id=1),
        description='Более 20 рубрик бесценных советов на каждый день!'
    )
    Edition.objects.create(
        image='50.jpg',
        index='29120',
        title='OTTOBRE (ОТТОБРЕ)',
        price='1589',
        edition_type=EditionType.objects.get(id=1),
        description='Качественное издание для любителей шитья детям. Каждый номер включает выкройки и инструкции к 40 актуальным моделям для детей и подростков ростом от 56 до 170 см. Высокое качество бумаги и печати делают его настольной книгой рукодельницы.'
    )
    Edition.objects.create(
        image='51.jpg',
        index='43700',
        title='Ах, тёща моя!',
        price='651',
        edition_type=EditionType.objects.get(id=1),
        description='Газета для всей семьи, содержащая полезные советы и рецепты, хорошо сдобренная юмором и разбавленная красочными рисунками. Журнальный вариант.'
    )
    # Edition.objects.create(
    #     image='',
    #     index='',
    #     title='',
    #     price='',
    #     edition_type=EditionType.objects.get(id=),
    #     description=''
    # )


# TODO: Готово
# Добавление Подписок в таблицу
def add_subscriptions(apps, schema_editor):
    Subscription = apps.get_model('editions', 'Subscription')
    UserAccount = apps.get_model('accounts', 'UserAccount')
    Edition = apps.get_model('editions', 'Edition')

    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=3),
        edition=Edition.objects.get(id=3),
        date_of_subscription='2022-09-10',
        duration=1,
        is_subscription=True
    )
    # Subscription.objects.create(
    #     subscriber=UserAccount.objects.get(id=3),
    #     edition=Edition.objects.get(id=1),
    #     date_of_subscription='2022-09-10',
    #     duration=1,
    #     is_subscription=True
    # )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=4),
        edition=Edition.objects.get(id=4),
        date_of_subscription='2022-09-5',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=5),
        edition=Edition.objects.get(id=5),
        date_of_subscription='2022-09-5',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=6),
        date_of_subscription='2022-09-5',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=1),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=2),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=3),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=4),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=5),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=9),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=10),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=11),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=12),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=13),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=14),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=15),
        date_of_subscription='2017-09-5',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=7),
        date_of_subscription='2022-09-10',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=8),
        date_of_subscription='2018-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=9),
        date_of_subscription='2018-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=10),
        date_of_subscription='2018-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=11),
        date_of_subscription='2018-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=12),
        date_of_subscription='2018-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=13),
        date_of_subscription='2018-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=14),
        date_of_subscription='2018-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=15),
        date_of_subscription='2018-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=8),
        date_of_subscription='2022-09-10',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=9),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=10),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=11),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=12),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=13),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=14),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=15),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=16),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=17),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=18),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=20),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=21),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=22),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=9),
        date_of_subscription='2022-09-01',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=10),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=11),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=12),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=13),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=14),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=15),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=16),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=17),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=18),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=19),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=20),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=21),
        date_of_subscription='2020-09-01',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=10),
        date_of_subscription='2022-09-22',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=11),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=12),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=13),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=14),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=15),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=16),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=17),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=18),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=19),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=20),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=21),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=22),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=23),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=24),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=25),
        date_of_subscription='2021-03-11',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=11),
        edition=Edition.objects.get(id=11),
        date_of_subscription='2022-09-22',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=12),
        edition=Edition.objects.get(id=12),
        date_of_subscription='2022-09-22',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=13),
        edition=Edition.objects.get(id=13),
        date_of_subscription='2022-09-22',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=14),
        edition=Edition.objects.get(id=14),
        date_of_subscription='2022-09-11',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=15),
        edition=Edition.objects.get(id=15),
        date_of_subscription='2022-09-11',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=16),
        edition=Edition.objects.get(id=16),
        date_of_subscription='2022-09-11',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=3),
        edition=Edition.objects.get(id=1),
        date_of_subscription='2019-09-10',
        duration=1,
        is_subscription=True
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=23),
        edition=Edition.objects.get(id=34),
        date_of_subscription='2020-04-15',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=24),
        edition=Edition.objects.get(id=25),
        date_of_subscription='2022-03-21',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=41),
        edition=Edition.objects.get(id=23),
        date_of_subscription='2022-11-24',
        duration=1,
        is_subscription=False
    )
    Subscription.objects.create(
        subscriber=UserAccount.objects.get(id=34),
        edition=Edition.objects.get(id=12),
        date_of_subscription='2022-12-11',
        duration=1,
        is_subscription=False
    )
    # Subscription.objects.create(
    #     subscriber=UserAccount.objects.get(id=),
    #     edition=Edition.objects.get(id=),
    #     date_of_subscription='0000-00-00',
    #     duration=1,
    #     is_subscription=True
    # )


# TODO: Готово
# Добавление Почтальонов в таблицу
def add_postmans(apps, schema_editor):
    Postman = apps.get_model('postman', 'Postman')
    UserAccount = apps.get_model('accounts', 'UserAccount')

    Postman.objects.create(
        user=UserAccount.objects.get(id=23),
        employment_date='2012-01-12',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=14),
        employment_date='2012-08-24',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=15),
        employment_date='2017-03-01',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=45),
        employment_date='2022-09-17',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=33),
        employment_date='2011-11-25',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=31),
        employment_date='2018-08-11',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=28),
        employment_date='2020-09-15',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=17),
        employment_date='2017-03-01',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=18),
        employment_date='2019-06-06',
        topicality=True,
    )
    Postman.objects.create(
        user=UserAccount.objects.get(id=20),
        employment_date='2020-11-01',
        topicality=True,
    )
    # Postman.objects.create(
    #     user=UserAccount.objects.get(id=),
    #     employment_date='0000-00-00',
    #     topicality=False,
    # )


# TODO: Готово
# Добавление Доставок в таблицу
def add_delivery(apps, schema_editor):
    Delivery = apps.get_model('delivery', 'Delivery')
    UserAccount = apps.get_model('accounts', 'UserAccount')
    Edition = apps.get_model('editions', 'Edition')

    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=3),
        edition=Edition.objects.get(id=3),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=4),
        edition=Edition.objects.get(id=4),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=5),
        edition=Edition.objects.get(id=5),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=6),
        edition=Edition.objects.get(id=6),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=7),
        edition=Edition.objects.get(id=7),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=8),
        edition=Edition.objects.get(id=8),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=9),
        edition=Edition.objects.get(id=9),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=10),
        edition=Edition.objects.get(id=10),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=11),
        edition=Edition.objects.get(id=11),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=12),
        edition=Edition.objects.get(id=12),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=13),
        edition=Edition.objects.get(id=13),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=14),
        edition=Edition.objects.get(id=14),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=15),
        edition=Edition.objects.get(id=15),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=16),
        edition=Edition.objects.get(id=16),
        expected=True
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=3),
        edition=Edition.objects.get(id=1),
        expected=False
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=23),
        edition=Edition.objects.get(id=34),
        expected=False
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=24),
        edition=Edition.objects.get(id=25),
        expected=False
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=41),
        edition=Edition.objects.get(id=23),
        expected=False
    )
    Delivery.objects.create(
        subscriber=UserAccount.objects.get(id=34),
        edition=Edition.objects.get(id=12),
        expected=False
    )

    # Delivery.objects.create(
    #     subscriber=UserAccount.objects.get(id=),
    #     edition=Edition.objects.get(id=),
    #     expected=True
    # )


# TODO: Готово
# Добавление Улицы по районам и прикрепленные к ним почтальоны в таблицу
def add_districts_district_street(apps, schema_editor):
    DistrictStreet = apps.get_model('districts', 'DistrictStreet')
    Postman = apps.get_model('postman', 'Postman')
    Street = apps.get_model('address', 'Street')

    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=1),
        street=Street.objects.get(id=1)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=1),
        street=Street.objects.get(id=2)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=1),
        street=Street.objects.get(id=3)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=1),
        street=Street.objects.get(id=4)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=1),
        street=Street.objects.get(id=5)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=2),
        street=Street.objects.get(id=6)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=2),
        street=Street.objects.get(id=7)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=2),
        street=Street.objects.get(id=8)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=2),
        street=Street.objects.get(id=9)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=2),
        street=Street.objects.get(id=10)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=3),
        street=Street.objects.get(id=11)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=3),
        street=Street.objects.get(id=12)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=3),
        street=Street.objects.get(id=13)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=3),
        street=Street.objects.get(id=14)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=3),
        street=Street.objects.get(id=15)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=4),
        street=Street.objects.get(id=16)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=4),
        street=Street.objects.get(id=17)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=4),
        street=Street.objects.get(id=18)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=4),
        street=Street.objects.get(id=19)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=4),
        street=Street.objects.get(id=20)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=5),
        street=Street.objects.get(id=21)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=5),
        street=Street.objects.get(id=22)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=5),
        street=Street.objects.get(id=23)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=5),
        street=Street.objects.get(id=24)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=5),
        street=Street.objects.get(id=25)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=6),
        street=Street.objects.get(id=26)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=6),
        street=Street.objects.get(id=27)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=6),
        street=Street.objects.get(id=28)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=6),
        street=Street.objects.get(id=29)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=6),
        street=Street.objects.get(id=30)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=7),
        street=Street.objects.get(id=31)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=7),
        street=Street.objects.get(id=32)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=7),
        street=Street.objects.get(id=33)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=7),
        street=Street.objects.get(id=34)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=7),
        street=Street.objects.get(id=35)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=8),
        street=Street.objects.get(id=36)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=8),
        street=Street.objects.get(id=37)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=8),
        street=Street.objects.get(id=38)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=8),
        street=Street.objects.get(id=39)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=8),
        street=Street.objects.get(id=40)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=9),
        street=Street.objects.get(id=41)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=9),
        street=Street.objects.get(id=42)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=9),
        street=Street.objects.get(id=43)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=9),
        street=Street.objects.get(id=44)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=9),
        street=Street.objects.get(id=45)
    )


    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=10),
        street=Street.objects.get(id=46)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=10),
        street=Street.objects.get(id=47)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=10),
        street=Street.objects.get(id=48)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=10),
        street=Street.objects.get(id=49)
    )
    DistrictStreet.objects.create(
        postman=Postman.objects.get(id=10),
        street=Street.objects.get(id=50)
    )

    # DistrictStreet.objects.create(
    #     postman=Postman.objects.get(id=),
    #     street=Street.objects.get(id=)
    # )


# TODO: Готово
# Добавление Районов в таблицу
def add_districts(apps, schema_editor):
    District = apps.get_model('districts', 'District')
    DistrictStreet = apps.get_model('districts', 'DistrictStreet')

    District.objects.create(
        number=1,
        title='Центр',
        district_street=DistrictStreet.objects.get(id=1)
    )
    District.objects.create(
        number=1,
        title='Центр',
        district_street=DistrictStreet.objects.get(id=2)
    )
    District.objects.create(
        number=1,
        title='Центр',
        district_street=DistrictStreet.objects.get(id=3)
    )
    District.objects.create(
        number=1,
        title='Центр',
        district_street=DistrictStreet.objects.get(id=4)
    )
    District.objects.create(
        number=1,
        title='Центр',
        district_street=DistrictStreet.objects.get(id=5)
    )


    District.objects.create(
        number=2,
        title='Край',
        district_street=DistrictStreet.objects.get(id=6)
    )
    District.objects.create(
        number=2,
        title='Край',
        district_street=DistrictStreet.objects.get(id=7)
    )
    District.objects.create(
        number=2,
        title='Край',
        district_street=DistrictStreet.objects.get(id=8)
    )
    District.objects.create(
        number=2,
        title='Край',
        district_street=DistrictStreet.objects.get(id=9)
    )
    District.objects.create(
        number=2,
        title='Край',
        district_street=DistrictStreet.objects.get(id=10)
    )


    District.objects.create(
        number=3,
        title='Днепровский',
        district_street=DistrictStreet.objects.get(id=11)
    )
    District.objects.create(
        number=3,
        title='Днепровский',
        district_street=DistrictStreet.objects.get(id=12)
    )
    District.objects.create(
        number=3,
        title='Днепровский',
        district_street=DistrictStreet.objects.get(id=13)
    )
    District.objects.create(
        number=3,
        title='Днепровский',
        district_street=DistrictStreet.objects.get(id=14)
    )
    District.objects.create(
        number=3,
        title='Днепровский',
        district_street=DistrictStreet.objects.get(id=15)
    )


    District.objects.create(
        number=4,
        title='Октябрьский',
        district_street=DistrictStreet.objects.get(id=16)
    )
    District.objects.create(
        number=4,
        title='Октябрьский',
        district_street=DistrictStreet.objects.get(id=17)
    )
    District.objects.create(
        number=4,
        title='Октябрьский',
        district_street=DistrictStreet.objects.get(id=18)
    )
    District.objects.create(
        number=4,
        title='Октябрьский',
        district_street=DistrictStreet.objects.get(id=19)
    )
    District.objects.create(
        number=4,
        title='Октябрьский',
        district_street=DistrictStreet.objects.get(id=20)
    )


    District.objects.create(
        number=5,
        title='Железнодорожный',
        district_street=DistrictStreet.objects.get(id=21)
    )
    District.objects.create(
        number=5,
        title='Железнодорожный',
        district_street=DistrictStreet.objects.get(id=22)
    )
    District.objects.create(
        number=5,
        title='Железнодорожный',
        district_street=DistrictStreet.objects.get(id=23)
    )
    District.objects.create(
        number=5,
        title='Железнодорожный',
        district_street=DistrictStreet.objects.get(id=24)
    )
    District.objects.create(
        number=5,
        title='Железнодорожный',
        district_street=DistrictStreet.objects.get(id=25)
    )


    District.objects.create(
        number=6,
        title='Ленинградский',
        district_street=DistrictStreet.objects.get(id=26)
    )
    District.objects.create(
        number=6,
        title='Ленинградский',
        district_street=DistrictStreet.objects.get(id=27)
    )
    District.objects.create(
        number=6,
        title='Ленинградский',
        district_street=DistrictStreet.objects.get(id=28)
    )
    District.objects.create(
        number=6,
        title='Ленинградский',
        district_street=DistrictStreet.objects.get(id=29)
    )
    District.objects.create(
        number=6,
        title='Ленинградский',
        district_street=DistrictStreet.objects.get(id=30)
    )


    District.objects.create(
        number=7,
        title='Минский',
        district_street=DistrictStreet.objects.get(id=31)
    )
    District.objects.create(
        number=7,
        title='Минский',
        district_street=DistrictStreet.objects.get(id=32)
    )
    District.objects.create(
        number=7,
        title='Минский',
        district_street=DistrictStreet.objects.get(id=33)
    )
    District.objects.create(
        number=7,
        title='Минский',
        district_street=DistrictStreet.objects.get(id=34)
    )
    District.objects.create(
        number=7,
        title='Минский',
        district_street=DistrictStreet.objects.get(id=35)
    )


    District.objects.create(
        number=8,
        title='Московский',
        district_street=DistrictStreet.objects.get(id=36)
    )
    District.objects.create(
        number=8,
        title='Московский',
        district_street=DistrictStreet.objects.get(id=37)
    )
    District.objects.create(
        number=8,
        title='Московский',
        district_street=DistrictStreet.objects.get(id=38)
    )
    District.objects.create(
        number=8,
        title='Московский',
        district_street=DistrictStreet.objects.get(id=39)
    )
    District.objects.create(
        number=8,
        title='Московский',
        district_street=DistrictStreet.objects.get(id=40)
    )


    District.objects.create(
        number=9,
        title='Печерский',
        district_street=DistrictStreet.objects.get(id=41)
    )
    District.objects.create(
        number=9,
        title='Печерский',
        district_street=DistrictStreet.objects.get(id=42)
    )
    District.objects.create(
        number=9,
        title='Печерский',
        district_street=DistrictStreet.objects.get(id=43)
    )
    District.objects.create(
        number=9,
        title='Печерский',
        district_street=DistrictStreet.objects.get(id=44)
    )
    District.objects.create(
        number=9,
        title='Печерский',
        district_street=DistrictStreet.objects.get(id=45)
    )


    District.objects.create(
        number=10,
        title='Подольский',
        district_street=DistrictStreet.objects.get(id=46)
    )
    District.objects.create(
        number=10,
        title='Подольский',
        district_street=DistrictStreet.objects.get(id=47)
    )
    District.objects.create(
        number=10,
        title='Подольский',
        district_street=DistrictStreet.objects.get(id=48)
    )
    District.objects.create(
        number=10,
        title='Подольский',
        district_street=DistrictStreet.objects.get(id=49)
    )
    District.objects.create(
        number=10,
        title='Подольский',
        district_street=DistrictStreet.objects.get(id=50)
    )
    # District.objects.create(
    #     number=,
    #     title='',
    #     district_street=DistrictStreet.objects.get(id=)
    # )


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_address_street),
        migrations.RunPython(add_edition_types),
        migrations.RunPython(add_address),
        migrations.RunPython(add_address_post_office_info),
        migrations.RunPython(add_users),
        migrations.RunPython(add_editions),
        migrations.RunPython(add_subscriptions),
        migrations.RunPython(add_postmans),
        migrations.RunPython(add_delivery),
        migrations.RunPython(add_districts_district_street),
        migrations.RunPython(add_districts),
    ]