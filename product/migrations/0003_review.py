# Generated by Django 4.1.7 on 2023-02-17 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_tag_product_category_product_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.IntegerField(choices=[(1, '*'), (2, '* * '), (3, '* * * '), (4, '* * * * '), (5, '* * * * * ')], default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='product.product')),
            ],
        ),
    ]