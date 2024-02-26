# Generated by Django 4.2.3 on 2024-02-20 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_alter_staff_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='staff',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='staff',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_members', to='feed.warehouse'),
        ),
    ]
