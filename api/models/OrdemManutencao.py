from django.db import models
from ._Base import Base
from .Equipamento import (PcsmEqpto)
from django.contrib.auth.models import User


class PcsmOm(Base):

    """
    Ordem de Manutenção
    """

    om_sap_cod = models.CharField(max_length=255, blank=False, null=False)
    om_pcsm_cod = models.CharField(max_length=255, blank=False, null=False)
    om_descricao = models.TextField(blank=True, default='')
    om_tipo_ord = models.CharField(max_length=255, blank=False, null=False)
    om_equipamento = models.ForeignKey(PcsmEqpto, on_delete=models.PROTECT)
    om_tecnico = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Om'
        verbose_name_plural = "Om's"
        ordering = ['id']

    def __str__(self):
        return self.om_sap_cod
