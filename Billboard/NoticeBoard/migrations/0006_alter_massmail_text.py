# Generated by Django 4.0.4 on 2022-10-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoticeBoard', '0005_alter_massmail_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massmail',
            name='text',
            field=models.TextField(),
        ),
    ]