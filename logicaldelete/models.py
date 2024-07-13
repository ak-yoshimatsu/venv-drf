import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class SoftDeleteModel(models.Model):
    """論理削除基底クラス"""

    deleted_at = models.DateTimeField(
        _("削除日時"),
        default=None,
        null=True,
        blank=True,
    )

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.datetime.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


# カスタムマネージャーの作成
class SoftDeleteManager(models.Manager):
    """論理削除されたオブジェクトを除外する"""

    def get_queryset(self):
        queryset = super().get_queryset().filter(deleted_at__isnull=True)
        return queryset


# Create your models here.
class Event(SoftDeleteModel):
    name = models.CharField(_("イベント名"), max_length=50)
    created_at = models.DateTimeField(_("登録日時"), auto_now_add=True)
    updated_at = models.DateTimeField(_("更新日時"), auto_now=True)

    objects = SoftDeleteManager()
    """カスタムマネージャー"""
    all_objects = models.Manager()
    """全てのオブジェクト"""

    class Meta:
        db_table = "events"
