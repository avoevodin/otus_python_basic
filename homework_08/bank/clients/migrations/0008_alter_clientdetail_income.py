# Generated by Django 4.0.6 on 2022-07-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0007_rename_salary_clientdetail_income"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientdetail",
            name="income",
            field=models.IntegerField(null=True),
        ),
    ]
