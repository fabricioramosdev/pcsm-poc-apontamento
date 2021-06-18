from rest_framework import serializers

from .models.Equipamento import (PcsmEqpto)
from .models.OrdemManutencao import (PcsmOm)
from .models.Apontamento import (PcsmApto, PcsmAptoSaldo)


class PcsmOmSerializer(serializers.ModelSerializer):

    class Meta:
        model = PcsmOm
        fields = (
            'id',
            'om_sap_cod',
            'om_pcsm_cod',
            'om_descricao',
            'om_tipo_ord',
            'om_equipamento',
            'om_tecnico'
        )


class PcsmAptoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PcsmApto
        fields = (
            'id',
            'apto_om_cod',
            'apto_tecnico',
            'apto_inicio',
            'apto_fim'
        )


class PcsmAptoSaldoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PcsmAptoSaldo
        fields = (
            'id',
            'aptocons_om_cod',
            'aptocons_total'
        )


class PcsmEqptoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PcsmEqpto
        fields = (
            'id',
            'eqpto_sap_cod',
            'eqpto_descricao',
            'eqpto_abc_cod'
        )
