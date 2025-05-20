# Criar um fluxo de caixa mensal para determinados perfis

class Perfis:
    def __init__(self, nome, renda,despesas):
        self.nome = nome
        self.renda = renda
        self.despesas = despesas
    
    def fluxo_de_caixa(self):
        return self.renda - self.despesas
    
    def __str__(self):
        return f"De acordo com a pesquisa o {self.nome}, de renda: R${self.renda} e despesas: R${self.despesas}, possui um fluxo de caixa de R${self.fluxo_de_caixa():.2f}"
    
# Criar perfis
perfil1 = Perfis("Perfil 1", 800, 1313.43)
print(perfil1)