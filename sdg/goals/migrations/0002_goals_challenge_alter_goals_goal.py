# Generated by Django 4.2.7 on 2023-11-12 01:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='challenge',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='challenges.challenge'),
        ),
        migrations.AlterField(
            model_name='goals',
            name='goal',
            field=models.CharField(choices=[('1', 'No Poverty'), ('2', 'Zero Hunger'), ('3', 'Good Health and Wellbeing'), ('4', 'Quality Education'), ('5', 'Gender Equality'), ('6', 'Clean Water and Sanitation'), ('7', 'Affordable and Clean Energy'), ('8', 'Decent Work and Economic Growth'), ('9', 'Industry, Innovation and Infrastructure'), ('10', 'Reduced Inequalities'), ('11', 'Sustainable Cities and Communities'), ('12', 'Responsible Consumption and Production'), ('13', 'Climate Action'), ('14', 'Life Below Water'), ('15', 'Life on Land'), ('16', 'Peace, Justice and Strong Institutions'), ('17', 'Partnership for the Goals')], default='17', max_length=100),
        ),
    ]