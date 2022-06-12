from django.db import models


class Applications(models.Model):
    application_id = models.AutoField(primary_key=True)
    application_number = models.CharField(unique=True, max_length=12)
    document_type = models.ForeignKey('DocumentsTypes', models.DO_NOTHING)
    worker = models.ForeignKey('Workers', models.DO_NOTHING)
    application_date = models.DateField()
    application_pdf_path = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'applications'
        verbose_name = 'заявление'
        verbose_name_plural = 'Заявления'


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
    contract_number = models.CharField(max_length=11)
    worker = models.ForeignKey('Workers', models.DO_NOTHING)
    status = models.IntegerField()
    contract_pdf_path = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'contracts'
        verbose_name = 'договор'
        verbose_name_plural = 'Договоры'


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'departments'
        verbose_name = 'отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        '''Метод для нормального отображения заголовка значения в админке'''
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
        '''Метод для нормального отображения заголовка значения в админке'''
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
        '''Метод для нормального отображения заголовка значения в админке'''
        return self.education_type_name


class Log(models.Model):
    log = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    log_number = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'log'
        verbose_name = 'журнальную запись'
        verbose_name_plural = 'Журнал'


class Orders(models.Model):
    order = models.OneToOneField(Applications, models.DO_NOTHING, primary_key=True)
    order_number = models.IntegerField(unique=True)
    order_date = models.DateField()
    order_pdf = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name = 'приказ'
        verbose_name_plural = 'Приказы'


class Passports(models.Model):
    passport = models.OneToOneField('Workers', models.DO_NOTHING, primary_key=True)
    seriya = models.CharField(max_length=5)
    nomer = models.CharField(unique=True, max_length=6)
    vidacha_date = models.DateField()
    podrazd_code = models.CharField(max_length=7)
    kem_vidan = models.CharField(max_length=64)
    birthday = models.DateField()
    birth_place = models.CharField(max_length=40)
    region_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'passports'
        verbose_name = 'паспорт'
        verbose_name_plural = 'Паспорта'

    def __str__(self):
        '''Метод для нормального отображения заголовка значения в админке'''
        return self.passport


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
        '''Метод для нормального отображения заголовка значения в админке'''
        return self.position_name


class Workers(models.Model):
    worker_id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=20)
    fio = models.CharField(db_column='FIO', max_length=60)  # Field name made lowercase.
    position = models.ForeignKey(Positions, models.DO_NOTHING)
    adress_fact = models.CharField(max_length=64)
    education_type = models.ForeignKey(EducationType, models.DO_NOTHING)
    education_spec = models.CharField(max_length=30)
    inn = models.CharField(db_column='INN', max_length=10)  # Field name made lowercase.
    phone = models.CharField(max_length=18)
    mail = models.CharField(max_length=40)
    work_start_date = models.DateField()
    work_book_number = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'workers'
        unique_together = (('inn', 'phone', 'mail', 'work_book_number'),)
        verbose_name = 'работника'
        verbose_name_plural = 'Работники'

    def __str__(self):
        '''Метод для нормального отображения заголовка значения в админке'''
        return self.fio