# Generated by Django 5.0.6 on 2024-06-28 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_itemmenu_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='itemmenu',
            options={'ordering': ['nome'], 'verbose_name': 'Item Menu', 'verbose_name_plural': 'Itens do Menu'},
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='ingredientes',
            field=models.CharField(default='Desconhecido', max_length=200),
        ),
        migrations.AlterField(
            model_name='itemmenu',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='post_img'),
        ),
        migrations.AlterField(
            model_name='itemmenu',
            name='preco',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='itemmenu',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.categoria'),
        ),
    ]
