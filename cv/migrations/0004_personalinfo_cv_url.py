# Generated by Django 4.2.5 on 2023-10-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_alter_education_image_alter_experience_diplome_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='cv_url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='CV URL'),
        ),
    ]
