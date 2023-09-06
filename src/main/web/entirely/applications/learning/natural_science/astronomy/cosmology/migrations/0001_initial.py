# Generated by Django 4.1 on 2023-06-02 18:12

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("standard_encoding", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LearningNaturalScienceAstronomyCosmologyCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "CREATE_TIME",
                    simplepro.components.fields.DateTimeField(
                        auto_now_add=True, verbose_name="创建时间"
                    ),
                ),
                (
                    "UPDATE_TIME",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "STATUS_IS_DELETE",
                    models.BooleanField(default=False, verbose_name="逻辑删除"),
                ),
                (
                    "STATUS_IS_EFFECTIVE",
                    models.BooleanField(default=True, verbose_name="是否有效"),
                ),
                (
                    "NAME",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=100, null=True, verbose_name="中文描述"
                    ),
                ),
                (
                    "ID_PARENT",
                    simplepro.components.fields.TreeComboboxField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cosmology.learningnaturalscienceastronomycosmologycode",
                        verbose_name="父级",
                    ),
                ),
                (
                    "STATUS_AUTHORITY",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="权限控制",
                        to="standard_encoding.provenancesystemsettingsstandardcodemaindict",
                        verbose_name="权限控制",
                    ),
                ),
            ],
            options={
                "verbose_name": "天体基本信息",
                "verbose_name_plural": "天体基本信息",
                "db_table": "LearningNaturalScienceAstronomyCosmologyCode",
                "ordering": ["-CREATE_TIME"],
            },
        ),
    ]
