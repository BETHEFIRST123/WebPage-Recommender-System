# Generated by Django 2.2.5 on 2019-11-27 04:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WebPage1', models.IntegerField(choices=[(1, 'Front Page'), (2, 'Weather'), (3, 'Health'), (4, 'Living'), (5, 'Business'), (6, 'News'), (7, 'Tech'), (8, 'Local'), (9, 'Opinion'), (10, 'On Air'), (11, 'Misc'), (12, 'Sports'), (13, 'Summary'), (14, 'BBS'), (15, 'Travel'), (16, 'MSN News'), (17, 'MSN Sports')], default=1)),
                ('WebPage2', models.IntegerField(choices=[(1, 'Front Page'), (2, 'Weather'), (3, 'Health'), (4, 'Living'), (5, 'Business'), (6, 'News'), (7, 'Tech'), (8, 'Local'), (9, 'Opinion'), (10, 'On Air'), (11, 'Misc'), (12, 'Sports'), (13, 'Summary'), (14, 'BBS'), (15, 'Travel'), (16, 'MSN News'), (17, 'MSN Sports')], default=1)),
                ('WebPage3', models.IntegerField(choices=[(1, 'Front Page'), (2, 'Weather'), (3, 'Health'), (4, 'Living'), (5, 'Business'), (6, 'News'), (7, 'Tech'), (8, 'Local'), (9, 'Opinion'), (10, 'On Air'), (11, 'Misc'), (12, 'Sports'), (13, 'Summary'), (14, 'BBS'), (15, 'Travel'), (16, 'MSN News'), (17, 'MSN Sports')], default=1)),
                ('WebPage4', models.IntegerField(choices=[(1, 'Front Page'), (2, 'Weather'), (3, 'Health'), (4, 'Living'), (5, 'Business'), (6, 'News'), (7, 'Tech'), (8, 'Local'), (9, 'Opinion'), (10, 'On Air'), (11, 'Misc'), (12, 'Sports'), (13, 'Summary'), (14, 'BBS'), (15, 'Travel'), (16, 'MSN News'), (17, 'MSN Sports')], default=1)),
                ('WebPage5', models.IntegerField(choices=[(1, 'Front Page'), (2, 'Weather'), (3, 'Health'), (4, 'Living'), (5, 'Business'), (6, 'News'), (7, 'Tech'), (8, 'Local'), (9, 'Opinion'), (10, 'On Air'), (11, 'Misc'), (12, 'Sports'), (13, 'Summary'), (14, 'BBS'), (15, 'Travel'), (16, 'MSN News'), (17, 'MSN Sports')], default=1)),
                ('WebPage6', models.IntegerField(choices=[(1, 'Front Page'), (2, 'Weather'), (3, 'Health'), (4, 'Living'), (5, 'Business'), (6, 'News'), (7, 'Tech'), (8, 'Local'), (9, 'Opinion'), (10, 'On Air'), (11, 'Misc'), (12, 'Sports'), (13, 'Summary'), (14, 'BBS'), (15, 'Travel'), (16, 'MSN News'), (17, 'MSN Sports')], default=1)),
                ('predicted_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('num', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predict', to='accounts.UserProfileInfo')),
            ],
        ),
    ]