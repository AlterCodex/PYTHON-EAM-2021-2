import json

import falcon

from tienda_video_juegos.dominio.video_juego import VideoJuego
from tienda_video_juegos.infraestructura.persistencia_videojuego \
    import PersistenciaVideoJuego


class VideoJuegoController():

    def on_get(self, req, resp):
        print("hola")
        video_juego_repositorio = PersistenciaVideoJuego()
        juegos=video_juego_repositorio.cargar_todo()
        template = """<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
                    <h1 style="color: #5e9ca0;">La Tienda de los Nerds</h1>
                    <h2 style="color: #2e6c80;">Juegos En Existencia:</h2>
                    <h2 style="color: #2e6c80;">Cleaning options:</h2>
                    <table class="editorDemoTable" style="height: 362px;">
                    <thead>
                    <tr style="height: 18px;">
                    <td style="height: 18px; width: 263.172px;">Nombre</td>
                    <td style="height: 18px; width: 348.625px;">Clasificacion</td>
                    <td style="height: 18px; width: 55.2031px;">Consola</td>
                    </tr>
                    </thead>
                    <tbody>
                """
        for juego in juegos:
            juego_template  = f"""<tr style="height: 22px;">
                                <td style="height: 22px; width: 263.172px;">{juego.nombre}</td>
                                <td style="height: 22px; width: 348.625px;">{juego.clasificacion}</td>
                                <td style="height: 22px; width: 55.2031px;">{juego.consola}</td>
                                </tr>
                                """
            template+=juego_template
        template+="""</tbody>
        </table>"""
        resp.body = template
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        juego= VideoJuego(**req.media)
        juego.guardar()
        resp.status = falcon.HTTP_CREATED

    def on_put(self, req, resp, id):
        video_juego_repositorio = PersistenciaVideoJuego()
        video_juego = video_juego_repositorio.cargar(id)
        video_juego.update(req.media)
        video_juego.id = id
        video_juego.guardar()
        resp.body = video_juego.__dict__

    def on_delete(self):
        pass
