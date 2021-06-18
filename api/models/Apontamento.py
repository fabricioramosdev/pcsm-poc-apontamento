from django.db import models
from ._Base import (Base)
from .OrdemManutencao import (PcsmOm)
from django.contrib.auth.models import User


class PcsmApto(Base):

    """
    Apontamento
    """

    apto_om_cod = models.ForeignKey(PcsmOm, on_delete=models.CASCADE)
    apto_tecnico = models.ForeignKey(User, on_delete=models.PROTECT)
    apto_inicio = models.DateTimeField(null=True, blank=True)
    apto_fim = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Apontamento'
        verbose_name_plural = 'Apontamentos'
        ordering = ['id']

    def __str__(self):
        return f'{self.apto_om_cod}\t{self.apto_inicio}\t{self.apto_fim}'


class PcsmAptoSaldo(Base):

    """
    Apontamento Saldo
    """

    aptocons_om_cod = models.ForeignKey(PcsmOm, on_delete=models.CASCADE)
    aptocons_total = models.FloatField(null=True, blank=True, default=0.0)


    class Meta:
        verbose_name = 'Apontamento Saldo'
        verbose_name_plural = 'Apontamentos Saldos'
        ordering = ['id']

    def __str__(self):
        return self.apto_om_cod
