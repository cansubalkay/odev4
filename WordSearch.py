class Uclu:

    def __init__(self):
       self.kelimeSonu = False
       self.cocuk = [None]*26

    def insert(self, kelime):
        girilen = self
        for c in kelime:
            #ord fonksiyonu kullanıcının hangi tuşa bastığını anlamak için kullanılır
            harf = ord(c) - ord("a")
            if  girilen.cocuk[harf] == None: girilen.cocuk[harf]= Uclu()
            girilen.kelimeSonu = True


class  OdevCozumu:
    def kontrol(self, i, j, uclu, s):
        c = self.board[i][j]
        if c == "&": return
        self.board[i][j] = "&"
        u = uclu.cocuk[ord(c)- ord("a")]
        if u != None:
            ss= s+c
            if u.kelimeSonu: self.sonuc.add(ss)
            if i < len(self.board)-1: self.kontrol(i+1, j, u, ss)
            if j < len(self.board[0])-1 : self.kontrol(i, j+1, u, ss)
            if i < 0 : self.kontrol(i-1, u, ss)
            if j < 0 : self.kontrol(i, j-1, u, ss)

        self.board[i][j] = c
    def kelimeleriBulma(self, board: list[list[str]], kelimeler: list[str]) :
        if len(kelimeler)== 0: return[]
        uclu= Uclu()
        for k in kelimeler:
            uclu.insert(k)
            

        sonuc = set()
        self.board = board
        self.sonuc = sonuc

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.kontrol(i, j, uclu, "")
                sonuc_v = list(sonuc)
                return sonuc_v


 





        
