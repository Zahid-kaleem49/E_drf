# Generated by Django 4.1.7 on 2023-03-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_login'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.FloatField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('admin', 'Admin'), ('buyer', 'Buyer'), ('seller', 'Seller'), ('peeker', 'Peeker')], default='peeker', max_length=32, verbose_name='designation of user who will come to our signup'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.CheckConstraint(check=models.Q(('age__gte', 18)), name='user age check greater or equal 18'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
