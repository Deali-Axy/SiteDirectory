from django.db import models
from django_starter.db.models import ModelExt


class Category(ModelExt):
    name = models.CharField('名称', max_length=100)
    description = models.TextField('说明', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '网站分类'
        verbose_name_plural = verbose_name


class WebSite(ModelExt):
    name = models.CharField('名称', max_length=100)
    description = models.TextField('说明', blank=True, null=True)
    category = models.ForeignKey('Category', db_constraint=False, on_delete=models.DO_NOTHING)
    url = models.URLField('链接')
    extra_urls = models.ManyToManyField('URL', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '网站'
        verbose_name_plural = verbose_name


class URL(ModelExt):
    url = models.URLField('链接')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = '链接'
        verbose_name_plural = verbose_name


class ClickLog(ModelExt):
    website = models.ForeignKey('WebSite', db_constraint=False, on_delete=models.DO_NOTHING)
    ip_address = models.GenericIPAddressField('IP地址')

    def __str__(self):
        return f'{self.website}_{self.ip_address}'

    class Meta:
        verbose_name = '点击记录'
        verbose_name_plural = verbose_name
