from django.utils import timezone
from django.db import models

# Create your models here.
class Producto(models.Model):
	CATEGORIAS = [
		("Carreras", "Carreras"),
		("Simulación", "Simulación"),
		("Acción", "Acción"),
		("Horror", "Horror"),
		("Aventura", "Aventura"),
		("Supervivencia", "Supervivencia"),
		("Sandbox", "Sandbox"),
		("Estrategia", "Estrategia"),
		("Party", "Party"),
		("Deportes", "Deportes"),
		("Rol", "Rol")
	]

	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	precio = models.DecimalField(max_digits=12, decimal_places=0)
	stock = models.IntegerField(null=True, default=0)
	descripcion = models.TextField()
	imagen = models.ImageField(null=True, blank=True, upload_to="img/")
	categoria = models.CharField(max_length=100, choices=CATEGORIAS, null=True)
	en_descuento = models.BooleanField(default=False)
	en_restock = models.BooleanField(default=False)
	descuento = models.DecimalField(max_digits=3, decimal_places=0, default=0)
	descuento_subs = models.DecimalField(max_digits=3, decimal_places=0, default=0)

	def __str__(self):
		return f"#{self.id} | {self.nombre}"

class Boleta(models.Model):
	ESTADO_PEDIDOS = [
		("Anulado", "Anulado"),
		("En proceso", "En proceso"),
		("Despachado", "Despachado"),
		("Entregado", "Entregado"),
		("Vendido", "Vendido")
	]

	id = models.AutoField(primary_key=True)
	rut = models.CharField(max_length=12, blank=True, null=True)
	productos = models.ManyToManyField(Producto, through="ProductoEnBoleta")
	fecha = models.DateTimeField(default=timezone.now)
	total = models.DecimalField(max_digits=12, decimal_places=0)
	estado_pedido = models.CharField(max_length=20, choices=ESTADO_PEDIDOS, default="En proceso")

	def __str__(self):
		return f"Boleta #{self.id} - {self.fecha}"
	
class Cuenta(models.Model):
	ROLES = [
		("Cliente", "Cliente"), 
		("Administrador", "Administrador")
	]

	rut = models.CharField(max_length=12, unique=True)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	correo = models.EmailField(unique=True)
	direccion = models.TextField(max_length=100)
	contraseña = models.CharField(max_length=100)
	subscrito = models.BooleanField(default=False)
	imagen = models.ImageField(null=True, blank=True, upload_to="perfil/")
	rol = models.CharField(max_length=20, choices=ROLES, default="Cliente")
	favoritos = models.ManyToManyField(Producto, related_name="favorited_by", blank=True)

	def __str__(self):
		return f"{self.correo}"
	
class ProductoEnBoleta(models.Model):
	boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.producto.nombre} - Cantidad: {self.cantidad}"