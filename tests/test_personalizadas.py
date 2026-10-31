import pytest
from engconvert import personalizadas as p


def test_adicionar_e_converter():
    unidades = p.adicionar({}, 'Comprimento', 'minha_unidade', 2)
    assert p.converter(3, 'Comprimento', 'minha_unidade', 'm', unidades) == pytest.approx(6)


@pytest.mark.parametrize('fator', ['0', '-2', 'nan', 'inf', 'texto'])
def test_fator_invalido(fator):
    with pytest.raises(ValueError):
        p.adicionar({}, 'Pressão', 'unidade_teste', fator)


def test_duplicata_e_temperatura():
    with pytest.raises(ValueError):
        p.adicionar({}, 'Pressão', 'bar', 2)
    with pytest.raises(ValueError):
        p.adicionar({}, 'Temperatura', 'nova_escala', 2)


def test_excluir_sem_afetar_original():
    unidades = p.adicionar({}, 'Área', 'quadra', 100)
    novas = p.excluir(unidades, 'Área', 'quadra')
    assert 'quadra' in unidades['Área']
    assert 'quadra' not in novas['Área']


def test_salvar_e_reabrir(tmp_path):
    arquivo = tmp_path / 'custom.json'
    unidades = p.adicionar({}, 'Volume', 'tanque', 3)
    p.salvar(unidades, arquivo)
    assert p.carregar(arquivo) == unidades


def test_json_invalido(tmp_path):
    arquivo = tmp_path / 'custom.json'
    arquivo.write_text('{erro', encoding='utf-8')
    assert p.carregar(arquivo) == {}
