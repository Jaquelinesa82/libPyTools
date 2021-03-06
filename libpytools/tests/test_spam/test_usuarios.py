from libpytools.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='jaqueline', email='jaquelinesa.82@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Jaqueline', email='jaquelinesa.82@gmail.com'),
        Usuario(nome='Ana', email='jaquelinesa.82@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
