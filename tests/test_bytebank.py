from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        #given (contexto)
        entrada = '13/03/2000'
        esperado = 22

        Funcionario_teste = Funcionario("Teste", entrada, 1111)
        
        #when (ação)
        resultado = Funcionario_teste.idade()

        #then (desfecho)
        assert resultado == esperado
    
    def test_quando_sobrenome_recebe_Lucas_Carvallho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        lucas =  Funcionario(entrada, '13/03/2000', 1111)
        resultado = lucas.sobrenome()
        assert resultado == esperado