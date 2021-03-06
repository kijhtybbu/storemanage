# Generated by Django 2.0.2 on 2019-12-09 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='备注日期')),
            ],
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='Opening_date',
            field=models.DateField(blank=True, null=True, verbose_name='开店日期'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='ap',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='AP 数量'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='brand',
            field=models.CharField(choices=[('1', '王品'), ('2', '西堤'), ('3', '舞渔'), ('4', '鹅夫人'), ('5', 'The WANG'), ('6', '鹊玥')], max_length=10, verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='店铺编号'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='completion_date',
            field=models.DateField(blank=True, null=True, verbose_name='工程完工日期'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='contacts',
            field=models.TextField(blank=True, null=True, verbose_name='联系人'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='engineering_head',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='工程部负责人'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='equipment_arrival_date',
            field=models.DateField(blank=True, null=True, verbose_name='设备到店日期'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='expected_installation_date',
            field=models.DateField(blank=True, null=True, verbose_name='预计安装日期'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='firewall_type',
            field=models.CharField(blank=True, max_length=20, verbose_name='防火墙类型'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='storeinformation',
            name='ps',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='storecomment',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_manage.StoreInformation'),
        ),
    ]
