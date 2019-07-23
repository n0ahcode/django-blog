# Generated by Django 2.1.7 on 2019-07-22 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('thumnail', models.ImageField(blank=True, null=True, upload_to='card_thumnail/')),
                ('view_counter', models.IntegerField(default=0, verbose_name='閲覧数')),
                ('detail', models.TextField(blank=True, verbose_name='記事の説明')),
            ],
            options={
                'verbose_name': 'カード',
                'verbose_name_plural': 'カード',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='CardChemicalTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='カード化学タグ')),
            ],
            options={
                'verbose_name': 'カード化学タグ',
                'verbose_name_plural': 'カード化学タグ',
            },
        ),
        migrations.CreateModel(
            name='CardComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='名前')),
                ('text', models.TextField(verbose_name='コメント')),
                ('thumnail', models.ImageField(blank=True, null=True, upload_to='comment_thumnail/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_app.Card', verbose_name='対象記事')),
            ],
            options={
                'verbose_name': 'カードコメント',
                'verbose_name_plural': 'カードコメント',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='CardPostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='カード記事タグ')),
            ],
            options={
                'verbose_name': 'カード記事タグ',
                'verbose_name_plural': 'カード記事タグ',
            },
        ),
        migrations.CreateModel(
            name='CardReComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='名前')),
                ('text', models.TextField(verbose_name='コメント')),
                ('thumnail', models.ImageField(blank=True, null=True, upload_to='recomment_thumnail/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_app.CardComment')),
            ],
            options={
                'verbose_name': 'カードコメントの返信',
                'verbose_name_plural': 'カードコメントの返信',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='card',
            name='chemical_tag',
            field=models.ManyToManyField(blank=True, to='card_app.CardChemicalTag', verbose_name='化学カードタグ'),
        ),
        migrations.AddField(
            model_name='card',
            name='friend_posts',
            field=models.ManyToManyField(blank=True, related_name='_card_friend_posts_+', to='card_app.Card', verbose_name='関連記事'),
        ),
        migrations.AddField(
            model_name='card',
            name='post_tag',
            field=models.ManyToManyField(blank=True, to='card_app.CardPostTag', verbose_name='記事カードタグ'),
        ),
    ]