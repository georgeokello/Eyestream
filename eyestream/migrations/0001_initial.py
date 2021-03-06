# Generated by Django 3.2.9 on 2022-02-22 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('facebook', models.CharField(max_length=120, null=True)),
                ('twitter', models.CharField(max_length=120, null=True)),
                ('google', models.CharField(max_length=120, null=True)),
                ('channel_picture', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='channel_pics')),
                ('channel_banner', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='channel_banner_pics')),
                ('subscribers', models.ManyToManyField(related_name='subscribers_count', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=120)),
                ('catergory', models.CharField(max_length=120)),
                ('video', models.FileField(upload_to='uploaded_videos')),
                ('about', models.TextField(max_length=120)),
                ('thumbnail', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='video_thumbnail')),
                ('date', models.DateField(auto_now=True)),
                ('channel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_channel', to='eyestream.channels')),
            ],
        ),
        migrations.CreateModel(
            name='VideoViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(max_length=120)),
                ('session', models.CharField(max_length=120)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_count', to='eyestream.videos')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
