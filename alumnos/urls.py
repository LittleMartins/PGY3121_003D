from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('carrito/', views.carrito, name='carrito'),
    path('productos/', views.productos, name='productos'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('pagar/', views.pagar, name='pagar'),
    path('devolucion/', views.devolucion, name='devolucion'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('crud/', views.crud, name='crud'),
    path('agregarproductos/', views.agregarproductos_lista, name='agregarproductos_lista'),
    path('agregarproductos/nuevo/', views.agregarproductos_nuevo, name='agregarproductos_nuevo'),
    path('agregarproductos/<int:id>/', views.agregarproductos_editar, name='agregarproductos_editar'),
    path('confirmar_eliminar/<int:id>/', views.agregarproductos_confirmar_eliminar, name='agregarproductos_confirmar_eliminar'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('logout/', views.logout_view, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
