import json
import random

import falcon
from falcon import API

from Clases.clase_28_09_2021.Infraestructura.PersistenciaGuitarra import \
    PersistenciaGuitarra


class HolaMundo():

    def on_get(self, req, resp, uuid):
        db=PersistenciaGuitarra()
        gui=db.load_json(uuid+'.json')
        mensajes = ['Hola Mindo','Hola Que hace', 'Adio', 'Ciao','2+2=4']
        resp.body = json.dumps(gui)
        resp.status =falcon.HTTP_OK


def iniciar() ->  API:
#run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = API()
    api.add_route("/guitarra/{uuid}",HolaMundo())

    return api

app=iniciar()


