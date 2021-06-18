from rest_framework import viewsets

from .models.Apontamento import (PcsmApto, PcsmAptoSaldo)
from .models.OrdemManutencao import (PcsmOm)
from .models.Equipamento import (PcsmEqpto)


from .serializers import (PcsmOmSerializer, PcsmAptoSerializer, PcsmAptoSaldoSerializer, PcsmEqptoSerializer)


class PcsmOmViewSet(viewsets.ModelViewSet):
    """
    Ordem de Manutenção
    """

    queryset = PcsmOm.objects.all()
    serializer_class = PcsmOmSerializer


class PcsmAptoViewSet(viewsets.ModelViewSet):
    """
    Apontamento
    """

    queryset = PcsmApto.objects.all()
    serializer_class = PcsmAptoSerializer


class PcsmAptoSaldoViewSet(viewsets.ModelViewSet):
    """
    Apontamento Saldo
    """

    queryset = PcsmAptoSaldo.objects.all()
    serializer_class = PcsmAptoSaldoSerializer


class PcsmEqptoViewSet(viewsets.ModelViewSet):
    """
    Equipamento
    """

    queryset = PcsmEqpto.objects.all()
    serializer_class = PcsmEqptoSerializer
