class hash:
    def __init__(self, larg):
        self.larg = larg
        self.tab = [None]*larg
        self.est = [1]*larg
    def inserir(self, num):
        if None not in self.tab:
            print('Hash Cheio!')
            return
        posi = num % self.larg
        while True:
            if self.est[posi] == 1:
                self.tab[posi] = num
                self.est[posi] = 0
                return
            posi += 1
            if posi == self.larg:
                posi = 0
    def guardar(self):
        tab = ''
        for i in range(self.larg):
            bi = '{0:b}'.format(i)
            for k in range(4):
                if len(bi) < 5:
                    bi = '0' + bi
            tab += (f'{chr(self.tab[i])}, {bi}\n')
        return tab