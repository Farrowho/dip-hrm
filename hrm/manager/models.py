from django.db import models


class Applications(models.Model):
    application_id = models.AutoField(primary_key=True)
    application_number = models.CharField(unique=True, max_length=12, verbose_name='Номер заявления')
    document_type = models.ForeignKey('DocumentsTypes', models.DO_NOTHING, verbose_name='Тип документа')
    worker = models.ForeignKey('Workers', models.DO_NOTHING, verbose_name='ФИО сотрудника')
    application_date = models.DateField(verbose_name='Дата заявления')
    application_pdf_path = models.FileField(upload_to='files/', null=True, verbose_name="Файл")

    class Meta:
        managed = False
        db_table = 'applications'
        verbose_name = 'заявление'
        verbose_name_plural = 'Заявления'
        ordering = ['-application_id']

    def __str__(self):
        return self.application_number


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contracts(models.Model):
    contract_id = models.AutoField(primary_key=True)
    contract_number = models.CharField(max_length=11, verbose_name='Номер договора')
    worker = models.ForeignKey('Workers', models.DO_NOTHING, verbose_name='ФИО сотрудника')
    status = models.IntegerField(verbose_name='Статус договора')
    contract_pdf_path = models.FileField(upload_to='files/', null=True, verbose_name="Файл")

    class Meta:
        managed = False
        db_table = 'contracts'
        verbose_name = 'договор'
        verbose_name_plural = 'Договоры'
        ordering = ['-contract_id']

    def __str__(self):
        return self.contract_number


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'departments'
        verbose_name = 'отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.department_name


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentsTypes(models.Model):
    document_type_id = models.AutoField(primary_key=True)
    document_type_name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'documents_types'
        verbose_name = 'тип документа'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.document_type_name


class EducationType(models.Model):
    education_type_id = models.AutoField(primary_key=True)
    education_type_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'education_type'
        verbose_name = 'тип образования'
        verbose_name_plural = 'Тип образования'

    def __str__(self):
        return self.education_type_name


class Log(models.Model):
    log = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    log_number = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'log'
        verbose_name = 'журнальную запись'
        verbose_name_plural = 'Журнал'

    def __int__(self):
        return self.log


class Orders(models.Model):
    order = models.OneToOneField(Applications, models.DO_NOTHING, primary_key=True, verbose_name='Номер заявления ('
                                                                                                 'основание)')
    order_number = models.IntegerField(unique=True, verbose_name='Номер приказа')
    order_date = models.DateField(verbose_name='Дата приказа')
    order_pdf = models.FileField(upload_to='files/', null=True, verbose_name="Файл")

    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name = 'приказ'
        verbose_name_plural = 'Приказы'
        ordering = ['-order']


class Passports(models.Model):
    passport = models.OneToOneField('Workers', models.DO_NOTHING, primary_key=True, verbose_name='ФИО')
    seriya = models.CharField(max_length=5, verbose_name='Серия')
    nomer = models.CharField(unique=True, max_length=6, verbose_name='Номер')
    vidacha_date = models.DateField(verbose_name='Дата выдачи')
    podrazd_code = models.CharField(max_length=7, verbose_name='Код подразделения')
    kem_vidan = models.CharField(max_length=64, verbose_name='Кем выдан')
    birthday = models.DateField(verbose_name='Дата рождения')
    birth_place = models.CharField(max_length=40, verbose_name='Место рождения')
    region_name = models.CharField(max_length=40, verbose_name='Регион')

    class Meta:
        managed = False
        db_table = 'passports'
        verbose_name = 'паспорт'
        verbose_name_plural = 'Паспорта'

    def __str__(self):
        return self.nomer


class Positions(models.Model):
    position_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING)
    position_name = models.CharField(max_length=40)
    salary = models.FloatField()

    class Meta:
        managed = False
        db_table = 'positions'
        verbose_name = 'должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.position_name


class Workers(models.Model):
    worker_id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=20, verbose_name='Табельный номер')
    fio = models.CharField(db_column='FIO', max_length=60, verbose_name='ФИО')  # Field name made lowercase.
    position = models.ForeignKey(Positions, models.DO_NOTHING, verbose_name='Позиция')
    adress_fact = models.CharField(max_length=64, verbose_name='Адрес проживания')
    education_type = models.ForeignKey(EducationType, models.DO_NOTHING, verbose_name='Тип образования')
    education_spec = models.CharField(max_length=30, verbose_name='Специальность')
    inn = models.CharField(db_column='INN', max_length=10, verbose_name='ИНН')  # Field name made lowercase.
    phone = models.CharField(max_length=18, verbose_name='Телефон')
    mail = models.CharField(max_length=40, verbose_name='Почта')
    work_start_date = models.DateField(verbose_name='Дата начала работы')
    work_book_number = models.CharField(max_length=18, verbose_name='Номер трудовой книжки')

    class Meta:
        managed = False
        db_table = 'workers'
        unique_together = (('inn', 'phone', 'mail', 'work_book_number'),)
        verbose_name = 'работника'
        verbose_name_plural = 'Работники'
        ordering = ['worker_id']

    def __str__(self):
        return self.fio