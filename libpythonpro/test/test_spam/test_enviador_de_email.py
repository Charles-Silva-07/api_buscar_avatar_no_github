from libpythonpro.spam.enviador_de_email import Enviar


def test_criar_enviador_de_email():
    enviardor= Enviar()
    assert enviardor is not None


def test_remetente():
    enviador = Enviar()
    enviador.enviar(
        'charlleshp@hotmail.com',
        'charllesrocklp@gmail.com',
        'curso pythonpro',
        'primeira turma de python'
    )
