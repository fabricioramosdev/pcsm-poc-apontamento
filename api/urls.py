from django.urls import path
from rest_framework.routers import SimpleRouter
from .viewsets import (PcsmOmViewSet, PcsmAptoViewSet, PcsmAptoSaldoViewSet, PcsmEqptoViewSet)
router = SimpleRouter()
router.register('ordem', PcsmOmViewSet)
router.register('apontamento', PcsmAptoViewSet)
router.register('apontamento-saldo', PcsmAptoSaldoViewSet)
router.register('equipamento', PcsmEqptoViewSet)
