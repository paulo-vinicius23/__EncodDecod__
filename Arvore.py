COUNT = [10]
class No:
    def __init__(self, raiz = None, esquerda = None, direita = None):
        self.raiz = raiz
        self.direita = esquerda
        self.esquerda = direita

class Arvore_Binaria:
    def __init__(self, raiz=None):
        self.raiz = No(raiz)

    def inserir(self, valor, ra, posi = None):
        cont = 0
        ponte = ''
        ponte_2 = ''
        for i in range(len(valor)):
            cont += 1
            if valor[i] == '1':
                if ponte_2 == '0':
                    return self.inserir(ponte, ra.esquerda, posi)
                elif ra.direita is None:
                    ra.direita = No('1')
                elif (len(ponte) >= cont) or (valor[i] == ponte_2):
                    return self.inserir(ponte, ra.direita, posi)
            elif valor[i] == '0':
                if ponte_2 == '1':
                    return self.inserir(ponte, ra.direita, posi)
                elif ra.esquerda is None:
                    ra.esquerda = No('0')
                elif (len(ponte) >= cont) or (valor[i] == ponte_2):
                    return self.inserir(ponte, ra.esquerda, posi)
            else:
                if ponte_2 == '1':
                        return self.inserir(valor[i], ra.direita, posi)
                elif ponte_2 == '0':
                        return self.inserir(valor[i], ra.esquerda, posi)
                else:
                    if posi == '1':
                        ra.direita = No(valor[i])
                    if posi == '0':
                        ra.esquerda = No(valor[i])
            ponte = ''
            ponte_2 = valor[i]
            for k in range(len(valor)):
                if k+cont < len(valor):
                    ponte += valor[k+cont]
    
    def pre_ord(self, orde, ra):
        if ra.raiz is not None:
            orde.append(ra.raiz)
        if ra.esquerda is not None:
            self.pre_ord(orde, ra.esquerda)
        if ra.direita is not None:
            self.pre_ord(orde, ra.direita)
        return orde

    def busca(self, ordem, ra):
        if (ra.direita == None) and (ra.esquerda == None):
            return ra.raiz
        ponte = ''
        for i in range(len(ordem)):
            if i+1 < len(ordem):
                ponte += ordem[i+1]
        if ordem[0] == '0':
            return self.busca(ponte, ra.esquerda)
        elif ordem[0] == '1':
            return self.busca(ponte, ra.direita)

    def Display(self):
        linhas, *_ = self.Aux_Display(self.raiz)
        for linha in linhas:
            print(linha)

    def Aux_Display(self, ra):
        if ra.direita is None and ra.esquerda is None:
            linha = '%s' % ra.raiz
            largura = len(linha)
            altura = 1
            meio = largura // 2
            return [linha], largura, altura, meio
        if ra.direita is None:
            linhas, n, p, x = self.Aux_Display(ra.esquerda)
            s = '%s' % ra.raiz
            u = len(s)
            Primeira_linha = (x + 1) * ' ' + (n - x - 1) * '_' + s
            Segunda_linha = x * ' ' + '/' + (n - x - 1 + u) * ' '
            linhas_deslocadass = [linha + u * ' ' for linha in linhas]
            return [Primeira_linha, Segunda_linha] + linhas_deslocadass, n + u, p + 2, n + u // 2
        if ra.esquerda is None:
            linhas, n, p, x = self.Aux_Display(ra.direita)
            s = '%s' % ra.raiz
            u = len(s)
            Primeira_linha = s + x * '_' + (n - x) * ' '
            Segunda_linha = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            linhas_deslocadass = [u * ' ' + linha for linha in linhas]
            return [Primeira_linha, Segunda_linha] + linhas_deslocadass, n + u, p + 2, u // 2
        esquerda, n, p, x = self.Aux_Display(ra.esquerda)
        direita, m, q, y = self.Aux_Display(ra.direita)
        s = '%s' % ra.raiz
        u = len(s)
        Primeira_linha = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        Segunda_linha = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            esquerda += [n * ' '] * (q - p)
        elif q < p:
            direita += [m * ' '] * (p - q)
        Linhas_Zipadas = zip(esquerda, direita)
        linhas = [Primeira_linha, Segunda_linha] + [a + u * ' ' + b for a, b in Linhas_Zipadas]
        return linhas, n + m + u, max(p, q) + 2, n + u // 2