# Generated by Django 3.2 on 2021-04-11 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labeling_data', models.TextField()),
                ('creative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.creative')),
            ],
        ),
    ]
