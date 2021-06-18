from django.db import models
from ._Base import Base


class PcsmEqpto(Base):

    """
    Equipamento
    """

    eqpto_sap_cod = models.CharField(max_length=255, blank=False, null=False, unique=True)
    eqpto_descricao = models.CharField(max_length=255, blank=False, null=False)
    eqpto_abc_cod = models.CharField(max_length=1, blank=False, null=False)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

        ordering = ['id']

    def __str__(self):
        return self.eqpto_sap_cod
