# Generated by Django 5.1.2 on 2024-12-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_secondhanditem_rename_order_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='Second',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='second_items/')),
            ],
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.DeleteModel(
            name='FAQS',
        ),
        migrations.DeleteModel(
            name='SecondhandItem',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='is_featured',
            new_name='featured',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
