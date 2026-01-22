from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return f"Mesa {self.numero}"

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('F', 'Fazendo'),
        ('E', 'Entregue'),
    ]
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"