from unittest import TestCase

from dominio import Usuario, Lance, Leilao

class TestAvaliador(TestCase):
    def setUp(self):
            self.gui = Usuario('Gui')
            self.yuri = Usuario("Yuri")
            self.lance_do_gui = Lance(self.gui, 150.0)
            self.lance_do_yuri = Lance(self.yuri, 100.0)
            self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionado_em_ordem_decrescente(self):

        # TELL DON'T ASK
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        #primeiro o valor esperado depois o parâmetro
        self.assertEqual(menor_valor_esperado, self.leilao.lance_minimo)
        self.assertEqual(maior_valor_esperado, self.leilao.lance_maximo)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionado_em_ordem_crescente(self):
    # padrão de nomeclatura: test_deve_..."Função provada no teste"

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # primeiro o valor esperado depois o parâmetro
        self.assertEqual(menor_valor_esperado, self.leilao.lance_minimo)
        self.assertEqual(maior_valor_esperado, self.leilao.lance_maximo)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_1_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.lance_minimo)
        self.assertEqual(150.0, self.leilao.lance_maximo)

    def test_deve_retornar_o_menor_valor_quando_o_leilao_tiver_3_lances(self):
        vini = Usuario("Vini")

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.lance_minimo)
        self.assertEqual(maior_valor_esperado, self.leilao.lance_maximo)







