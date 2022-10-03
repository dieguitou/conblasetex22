from django.urls import path
from .views import *

# login
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(IndexA.as_view()), name='indexadmin'),
    path('mandarcorreo', login_required(RegistrarUsu.as_view()), name="mandar catalogo"),
    path('usuari/', login_required(ListarUsu.as_view()), name='listar_usuarios'),
    path('mandar/correo/', login_required(Mandarcorreo2.as_view()), name='mandarcorreo2'),

    path('Chamarras/', login_required(Chamarras.as_view()), name='vista_chamarra'),

    path('eliminar-chamarra/<id>/', login_required(eliminar_chamarra), name="eliminar-chamarra"),

    # new registro de prendas
    path('regitrar/prenda/<int:pk>', login_required(Registrar.as_view()), name="regitrar-prenda"),
    path('regitrar/prenda_v1/<int:pk>', login_required(Registrarv1.as_view()), name="regitrar-prenda-v1"),
    # path('vista/listar/', login_required(ListarPrenda.as_view()), name="vista_listar"),
    path('vista/agragar/', login_required(CreatePrenda.as_view()), name="vista_agragar"),

    # editar chamarra
    path('editar/prenda2/<int:pk>', login_required(Editarprenda2.as_view()), name="editar-prendas2"),

    path('vista/chamarra/vistadetalle/<int:pk>', login_required(VistaDetalles.as_view()), name='vistaChamarraDetalle2'),
    path('vista/eliminar/mensaje/<id>/', eliminar_correo, name='eliminar-correo'),

    # urls nuevas del sistema de administracion
    path('vista/producto/<int:pk>', login_required(ListarPrendas.as_view()), name='vista_producto_prenda'),
    path('vista/eliminar/new/<id>/', login_required(eliminar_producto), name='eliminar-productos'),
    path('vista/adicionar/pro', login_required(AdicionarProd.as_view()), name='Agragar_prod'),
    # eliminar productos Prod Epp
    path('vista/eliminar/ProdEpp/<id>/', login_required(eliminar_Prod_Edd), name='eliminarprodepp'),

    # new vitacora
    path('vista/vitacora/<int:pk>', login_required(ListarVita.as_view()), name='listar-vitacora'),
    # new RegistrarPrendaEpp
    path('vista/vista/registrar/', login_required(RegistrarPrendaEpp.as_view()), name='registrarPrendaEpp'),

    # new registrar epp
    path('Regitrar/Epp/<int:pk>', login_required(RegistrarEpp.as_view()), name="regitrar-Epp"),

    # new Editar EPP Prenda

    path('editar/prendaEppPrenda/<int:pk>', login_required(EditarprendaEpp.as_view()), name="editarPrendaEpp"),
    # new editar cantidad
    path('editar/cantidad/<int:pk>', login_required(EditarCantidad.as_view()), name="editar-cantidad"),
    # new editar Epp
    path('editar/Epp/<int:pk>', login_required(EditarEpp.as_view()), name="editarEpp"),
]
