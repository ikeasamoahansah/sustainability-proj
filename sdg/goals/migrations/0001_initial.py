# Generated by Django 4.2.7 on 2023-11-11 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('goal', models.CharField(choices=[('1', 'No Poverty'), ('2', 'Zero Hunger'), ('3', 'Good Health and Wellbeing'), ('4', 'Quality Education'), ('5', 'Gender Equality'), ('6', 'Clean Water and Sanitation'), ('7', 'Affordable and Clean Energy'), ('8', 'Decent Work and Economic Growth'), ('9', 'Industry, Innovation and Infrastructure'), ('10', 'Reduced Inequalities'), ('11', 'Sustainable Cities and Communities'), ('12', 'Responsible Consumption and Production'), ('13', 'Climate Action'), ('14', 'Life Below Water'), ('15', 'Life on Land'), ('16', 'Peace, Justice and Strong Institutions'), ('17', 'Partnership for the Goals')], default='Partnership for the Goals', max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]