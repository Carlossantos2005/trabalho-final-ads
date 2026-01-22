from django.contrib import admin
from .models import Categoria, Produto, Mesa, Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('mesa', 'produto', 'quantidade', 'status')

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Mesa)
admin.site.register(Pedido, PedidoAdmin)