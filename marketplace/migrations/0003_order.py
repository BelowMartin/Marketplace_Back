# Generated by Django 4.0.3 on 2022-03-14 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('from_to', models.CharField(max_length=100)),
                ('where_to', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=1, max_digits=2)),
                ('award', models.DecimalField(decimal_places=1, max_digits=2)),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.photo')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.user')),
            ],
        ),
    ]