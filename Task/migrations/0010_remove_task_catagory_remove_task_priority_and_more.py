# Generated by Django 5.1.2 on 2025-01-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0009_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='catagory',
        ),
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Small', max_length=6),
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
    ]
