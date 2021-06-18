from django.contrib import admin

# Register your models here.

from .models.Apontamento import (PcsmApto, PcsmAptoSaldo)
from .models.Equipamento import (PcsmEqpto)
from .models.OrdemManutencao import (PcsmOm)


@admin.register(PcsmApto)
class PcsmApto(admin.ModelAdmin):
    list_display = ('pk', 'apto_om_cod', 'apto_tecnico', 'apto_inicio', 'apto_fim')


@admin.register(PcsmAptoSaldo)
class PcsmAptoSaldo(admin.ModelAdmin):
    list_display = ('pk', 'aptocons_om_cod', 'aptocons_total')


@admin.register(PcsmEqpto)
class PcsmEqpto(admin.ModelAdmin):
    list_display = ('pk', 'eqpto_sap_cod', 'eqpto_descricao', 'eqpto_abc_cod')


@admin.register(PcsmOm)
class PcsmOm(admin.ModelAdmin):
    list_display = ('pk', 'om_sap_cod', 'om_pcsm_cod', 'om_descricao', 'om_tipo_ord', 'om_equipamento', 'om_tecnico')
