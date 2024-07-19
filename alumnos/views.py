from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno, AgregarProductos
from .forms import devolucionForm, PagarForm, AgregarProductosForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout

def is_admin(user):
    return user.is_superuser

def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(request, 'alumnos/index.html', context)

def carrito(request):
    productos = AgregarProductos.objects.filter(activo=True)
    return render(request, 'alumnos/carrito.html', {'productos': productos})



def productos(request):
    productos = Alumno.objects.all()
    context = {"productos": productos}
    return render(request, 'alumnos/Productos.html', context)

def quienes_somos(request):
    quienes_somos = Alumno.objects.all()
    context = {"quienes_somos": quienes_somos}
    return render(request, 'alumnos/quienes_somos.html', context)

def pagar(request):
    if request.method == 'POST':
        form = PagarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = PagarForm()
    
    data = {
        'formenvios': form
    }
    return render(request, 'alumnos/pagar.html', data)


def devolucion(request):
    enviado = False
    
    if request.method == 'POST':
        form = devolucionForm(request.POST)
        if form.is_valid():
            form.save()
 
            enviado = True
   
            return redirect('devolucion')
    else:
        form = devolucionForm()
    
    data = {
        'form': form,
        'enviado': enviado,
    }
    return render(request, 'alumnos/devolucion.html', data)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página principal después del registro
    else:
        form = UserCreationForm()
    return render(request, 'alumnos/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                form.add_error(None, "Invalid username or password")  # Agregar un mensaje de error si la autenticación falla
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'alumnos/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')



@login_required
@user_passes_test(is_admin)
def crud(request):
    productos = AgregarProductos.objects.all()
    return render(request, 'alumnos/crud.html', {'productos': productos})

def agregarproductos_lista(request):
    productos = AgregarProductos.objects.all()
    return render(request, 'alumnos/productos.html', {'productos': productos})

@login_required
@user_passes_test(is_admin)
def agregarproductos_nuevo(request):
    if request.method == "POST":
        form = AgregarProductosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregarproductos_lista')
    else:
        form = AgregarProductosForm()
    return render(request, 'alumnos/agregarproductos_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def agregarproductos_editar(request, id):
    producto = get_object_or_404(AgregarProductos, id=id)
    
    if request.method == "POST":
        form = AgregarProductosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('agregarproductos_lista')
    else:
        form = AgregarProductosForm(instance=producto)
    
    return render(request, 'alumnos/agregarproductos_editar.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def agregarproductos_confirmar_eliminar(request, id):
    producto = get_object_or_404(AgregarProductos, id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('agregarproductos_lista')
    
    return render(request, 'alumnos/agregarproductos_confirmar_eliminar.html', {'producto': producto})

def vaciar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']  
    return redirect('carrito')  

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(AgregarProductos, id=producto_id)
    
    if 'carrito' not in request.session:
        request.session['carrito'] = []
    
    carrito = request.session['carrito']
    carrito.append({
        'id': producto.id,
        'nombre': producto.nombre,
        'precio': float(producto.precio),  # Convertir el Decimal a float
        # Puedes incluir más detalles del producto si lo necesitas
    })
    
    request.session['carrito'] = carrito
    
    return redirect('carrito')  # Redirige a la página del carrito o a donde desees

def eliminar_del_carrito(request, producto_id):
    if 'carrito' in request.session:
        carrito = request.session['carrito']
        if producto_id in carrito:
            del carrito[producto_id]
            request.session['carrito'] = carrito
    return redirect('carrito')  # Redirigir al usuario de vuelta al carrito después de eliminar el producto
