import uuid

from laboratorio_corte.dominio.producto import Producto
from laboratorio_corte.dominio.video_juego import VideoJuego
from laboratorio_corte.infraestructura.persistencia import PersistenciaProducto
from laboratorio_corte.infraestructura.config import Config

def test_crear_tablas():
    pp=PersistenciaProducto()
    pp.connect()
    vid= VideoJuego()
    vid.consola = "xbox"
    vid.release_date = '2021-02-02'
    vid.nombre = 'Horizont'
    vid.tipo_juego = 'RPG/SLASHER'
    vid.clasificacion = "M"
    vid.empresa = "Microsoft"
    vid.numero_jugadores = 1
    pro = Producto()
    pro.precio = 300000
    pro.iva = 300000*.19
    pro.prendido = False
    pro.garantia_meses= 3
    pro.cantidad_disponible = 10
    pro.tipo = str(type(VideoJuego))
    pro.articulo = vid
    pro.serial = uuid.uuid4()
    pp.guardar_producto(pro)

    assert True


def test_json():
    vid = VideoJuego()
    vid.consola = "xbox"
    vid.release_date = '2021-02-02'
    vid.nombre = 'Horizont'
    vid.tipo_juego = 'RPG/SLASHER'
    vid.clasificacion = "M"
    vid.empresa = "Microsoft"
    vid.numero_jugadores = 1
    pro = Producto()
    pro.precio = 300000
    pro.iva = 300000 * .19
    pro.prendido = False
    pro.garantia_meses = 3
    pro.cantidad_disponible = 10
    pro.tipo = str(type(VideoJuego))
    pro.articulo = vid
    pro.serial = uuid.uuid4()
    PersistenciaProducto.save_json(pro)

def test_config():
    instance=Config.obtener_instancia()
    assert instance is not None

def test_config_update():
    instance=Config.obtener_instancia()
    initial_value=instance.usaBase
    Config.setUsaBase(not initial_value)
    instance = Config.obtener_instancia()
    assert not initial_value == instance.usaBase


