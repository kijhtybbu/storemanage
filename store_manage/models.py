import uuid
from datetime import date, datetime, timezone

from MySQLdb.converters import NoneType
from django.db import models


class StoreInformation(models.Model):
    STATUS_CHOICES = (
        ('1', '筹备'),
        ('5', '筹备-施工'),
        ('6', '筹备-发货'),
        ('7', '筹备-安装'),
        ('8', '筹备-完工'),
        ('2', '正常'),
        ('3', '护肤'),
        ('4', '闭店'),
    )
    BRAND_CHOICES = (
        ('1', '王品'),
        ('2', '西堤'),
        ('3', '舞渔'),
        ('4', '鹅夫人'),
        ('5', 'The WANG'),
        ('6', '鹊玥'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 品牌
    brand = models.CharField(max_length=10, choices=BRAND_CHOICES, blank=False, verbose_name="品牌")
    # 店铺编号
    code = models.CharField(max_length=10, null=True, blank=True, verbose_name="店铺编号")
    # 店铺名称
    name = models.CharField(max_length=100, null=True, blank=False, verbose_name="店铺名称")
    # 地址
    address = models.CharField(max_length=300, null=True, blank=True, verbose_name="地址")
    # IP
    ip = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True, verbose_name="IP")
    # AP 数量
    ap = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="AP 数量")
    # 客用wifi
    guest_wifi = models.BooleanField(default=False, verbose_name="客用wifi")
    # 联系人
    contacts = models.TextField(null=True, blank=True, verbose_name="联系人")
    # 设备到店日期
    equipment_arrival_date = models.DateField(null=True, blank=True, verbose_name="设备到店日期")
    # 工程完工日期
    completion_date = models.DateField(null=True, blank=True, verbose_name="工程完工日期")
    # 预计安装日期
    expected_installation_date = models.DateField(null=True, blank=True, verbose_name="预计安装日期")
    # 开店日期
    Opening_date = models.DateField(null=True, blank=True, verbose_name="开店日期")
    # 闭店日期
    closed_date = models.DateField(null=True, blank=True, verbose_name="闭店日期")
    # 工程部负责人
    engineering_head = models.CharField(max_length=100, null=True, blank=True, verbose_name="工程部负责人")
    # 防火墙类型
    firewall_type = models.CharField(max_length=20, blank=True, verbose_name="防火墙类型")
    # 状态：1，筹备 2，正常 3，护肤 4，闭店
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="状态")
    # 备注
    ps = models.TextField(max_length=300, null=True, blank=True, verbose_name="备注")
    # 修改时间
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)
    top_star = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="星标")

    @property
    def is_date_new(self):
        date_new = datetime.now(timezone.utc)
        return (date_new - self.modified_date).days < 3

    @property
    def get_away_date(self):
        """返回安装时间距离现在的天数"""
        if isinstance(self.expected_installation_date,NoneType):
            return 999
        date_new = datetime.now(timezone.utc)
        return (self.expected_installation_date - date_new.date()).days

    class Meta:
        # 末尾不加s
        verbose_name_plural = '店铺'
        # 末尾加s
        # verbose_name='标签'


class StoreComment(models.Model):
    store = models.ForeignKey(StoreInformation, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True, verbose_name="备注日期")
