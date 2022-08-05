from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'Body', {
    'name': fields.List(fields.String(), required=True, description="Nome do personagem"),
    'description': fields.List(fields.String(), required=True, description="Descrição do personagem")})
