# Generated by Django 2.1.1 on 2018-09-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('USERID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('USERNAME', models.CharField(max_length=50)),
                ('REALNAME', models.CharField(max_length=50, null=True)),
                ('EMAIL', models.CharField(max_length=100)),
                ('TELNO', models.CharField(max_length=20, null=True)),
                ('MOBILE', models.CharField(max_length=20, null=True)),
                ('QUESTION', models.CharField(max_length=50, null=True)),
                ('ANSWER', models.CharField(max_length=50, null=True)),
                ('PASSWORD', models.CharField(max_length=32)),
                ('USERSTATE', models.BooleanField()),
            ],
            options={
                'db_table': 'USER',
            },
        ),
    ]