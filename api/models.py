import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Author(models.Model):
    """著名モデル"""

    uuid = models.UUIDField(
        _("uuid"),
        unique=True,
        null=False,
        blank=False,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(_("著者名"), max_length=20)
    created_at = models.DateTimeField(_("登録日"), auto_now_add=True)

    class Meta:
        db_table = "authors"


class Book(models.Model):
    uuid = models.UUIDField(
        _("uuid"),
        unique=True,
        null=False,
        blank=False,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(_("タイトル"), max_length=50, null=False)
    price = models.IntegerField(_("価格"), null=True, blank=True)
    authers = models.ManyToManyField(
        to=Author,
        verbose_name=_("著者"),
        blank=True,
    )
    created_at = models.DateTimeField(_("登録日"), auto_now_add=True)

    class Meta:
        db_table = "books"
