import requests
import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd

with open('./service/Marvel.json','r') as arquivo:

    personagens = json.load(arquivo)

class PersonagemService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_model()


    def load_model(self):
        logger.debug(mensagens.FIM_LOAD_MODEL)
    
    def update_file(obj):
        open("Marvel.json", "w").write(
            json.dumps(obj, indent=4)
        )

    def find_name(name):
        items = []
        for personagem in personagens:
            if name.casefold() in personagem['Name'].casefold():
                items.append(personagem)
        if len(items) > 0:
            return items
        return False

    def find_name_especific(name):
        for personagem in personagens:
            if personagem['Name'].casefold() == name.casefold():
                return personagem 
        return False

    def get(self, name):
        response = []
        personagens = PersonagemService.find_name(name)
        if personagens != False:
            for personagem in personagens:
                response.append(personagem)
            return response           
        return False
   
    def post(self, dados):
        novo_personagem = {
        'Name' : dados['name'],
        'Description' : dados['description']
        }
        personagens.append(novo_personagem)
        PersonagemService.update_file(personagens)
        return novo_personagem

    def put(self, dados):
        name = dados['name']
        novo_personagem =    {
            'Name' : name,
            'Description' : dados['description']
        }
        personagem = PersonagemService.find_name_especific(name)
        if personagem:
            personagem.update(novo_personagem)
            PersonagemService.update_file(personagens)
            return personagem
        personagens.append(novo_personagem)
        PersonagemService.update_file(personagens)
        return novo_personagem

    def delete(self, name):
        personagem = PersonagemService.find_name_especific(name)
        if personagem:
            personagens.remove(personagem)
            PersonagemService.update_file(personagens)
            return True
        else:          
            return False
    