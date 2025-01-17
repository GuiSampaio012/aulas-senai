# Generated by Django 4.2.1 on 2023-06-14 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('cpf', models.CharField(max_length=11)),
                ('foto_logo', models.CharField(default='teste', max_length=100)),
                ('data_nascimento', models.DateField()),
                ('celular', models.CharField(max_length=11)),
                ('tipo_cliente', models.CharField(choices=[('F', 'Free'), ('P', 'Premium'), ('M', 'Master')], default='F', max_length=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Transferencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_enviado', models.IntegerField()),
                ('conta_transferencia', models.CharField(default=True, max_length=6)),
                ('conta_remetente', models.CharField(default=True, max_length=6)),
                ('tipo', models.CharField(choices=[('D', 'Deposito'), ('T', 'Transferencia'), ('P', 'Pix')], default='T', max_length=1)),
                ('data_hora', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Transferencias',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=40)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('cliente_endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_abertura', models.DateField(auto_now=True)),
                ('agencia', models.IntegerField()),
                ('numero', models.CharField(max_length=6, unique=True)),
                ('ativa', models.CharField(choices=[('A', 'Ativa'), ('D', 'Desativada')], default='A', max_length=1)),
                ('saldo', models.IntegerField()),
                ('cliente_conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contas',
            },
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=16)),
                ('validade', models.DateField()),
                ('cvv', models.CharField(max_length=3)),
                ('conta_cartao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cartões',
            },
        ),
    ]
