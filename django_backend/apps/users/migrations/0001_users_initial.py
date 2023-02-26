# Generated by Django 4.0.6 on 2022-09-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    #replaces = [('users', '0001_initial'), ('users', '0002_alter_user_username'), ('users', '0003_user_is_active_user_is_superuser'), ('users', '0004_user_is_staff'), ('users', '0005_remove_user_is_active_remove_user_is_staff_and_more')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]