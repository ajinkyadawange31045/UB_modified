# Generated by Django 4.1.2 on 2022-10-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_team_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('value_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('quote', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='quote/')),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='team/'),
        ),
    ]
