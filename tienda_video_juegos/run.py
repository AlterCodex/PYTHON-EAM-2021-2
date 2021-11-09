from falcon import App

from tienda_video_juegos.controlador.video_juego_controller import \
    VideoJuegoController, Demo



def iniciar() -> App:
#run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = App()
    api.add_route("/video-juego/", VideoJuegoController())
    api.add_route("/video-juego/{id:int}",VideoJuegoController())
    api.add_route("/demo/", Demo())
    return api

app = iniciar()
