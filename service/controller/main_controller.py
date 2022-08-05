from flask import request
from flask_restplus import Resource
from loguru import logger

from service.service.main_service import PersonagemService
from service.restplus import api, objResponse
from service.constants import mensagens, codeHttp
from service.util import doc_swagger

pa = api.namespace("")


@pa.route('/main/<string:name>')
class GETService(Resource):

    def get(self, name) -> dict:
        try:
            main_service = PersonagemService()
            resp = main_service.get(name)
            
            if resp != False:
                response = objResponse.send_success(data=resp, messages=mensagens.SUCESSO_GET, status=codeHttp.SUCCESS_200)
            else :
                response = objResponse.send_exception(objError='Not Found', messages=mensagens.ERROR_NOT_FOUND, status=codeHttp.ERROR_404)
       
        except OSError as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_OS, status=codeHttp.ERROR_500)
            logger.error(mensagens.ERROR_NONE_TYPE)

        except TypeError as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_NONE_TYPE, status=codeHttp.ERROR_500)
            logger.error(mensagens.ERROR_NONE_TYPE)

        except Exception as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_GENERIC, status=codeHttp.ERROR_500)
            logger.error(error)

        return response

    def delete(self, name) -> dict:
        try:
            main_service = PersonagemService()
            resp = main_service.delete(name)
            
            if resp:
                response = objResponse.send_success(data='', messages=mensagens.SUCESSO_DELETADO, status=codeHttp.SUCCESS_200)
            else :
                response = objResponse.send_exception(objError='Not Found', messages=mensagens.ERROR_NOT_FOUND, status=codeHttp.ERROR_404)
       
        except OSError as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_OS, status=codeHttp.ERROR_500)
            logger.error(mensagens.ERROR_NONE_TYPE)

        except TypeError as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_NONE_TYPE, status=codeHttp.ERROR_500)
            logger.error(mensagens.ERROR_NONE_TYPE)

        except Exception as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_GENERIC, status=codeHttp.ERROR_500)
            logger.error(error)

        return response

@pa.route('/main')
class PostService(Resource):
    @api.expect(doc_swagger.INPUT_MAIN_SERVICE)
    def post(self) -> dict:
        try:
            dados_request = request.get_json()
            main_service = PersonagemService()
            resp = main_service.post(dados_request)
            
            if resp != False:
                response = objResponse.send_success(data=resp, messages=mensagens.SUCESSO_PREDICT, status=codeHttp.SUCCESS_200)
            else :
                response = objResponse.send_exception(objError='Not Found', messages=mensagens.ERROR_NOT_FOUND, status=codeHttp.ERROR_404)
       
        except OSError as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_OS, status=codeHttp.ERROR_500)
            logger.error(mensagens.ERROR_NONE_TYPE)

        except TypeError as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_NONE_TYPE, status=codeHttp.ERROR_500)
            logger.error(mensagens.ERROR_NONE_TYPE)

        except Exception as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_GENERIC, status=codeHttp.ERROR_500)
            logger.error(error)

        return response

    @api.expect(doc_swagger.INPUT_MAIN_SERVICE)
    def put(self) -> dict:
        try:
            dados_request = request.get_json()
            main_service = PersonagemService()
            resp = main_service.put(dados_request)
            
            if resp != False:
                response = objResponse.send_success(data=resp, messages=mensagens.SUCESSO_PREDICT, status=codeHttp.SUCCESS_200)
            else :
                response = objResponse.send_exception(objError='Not Found', messages=mensagens.ERROR_NOT_FOUND, status=codeHttp.ERROR_404)
       
        except OSError as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_OS, status=codeHttp.ERROR_500)
            logger.error(mensagens.ERROR_NONE_TYPE)

        except TypeError as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_NONE_TYPE, status=codeHttp.ERROR_500)
            logger.error(mensagens.ERROR_NONE_TYPE)

        except Exception as error:
            response = objResponse.send_exception(objError=error, messages=mensagens.ERROR_GENERIC, status=codeHttp.ERROR_500)
            logger.error(error)

        return response