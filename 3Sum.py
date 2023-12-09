class OdevCozumu:
    def threeSum(self, sayilar: list[int]):
        n=len(sayilar)
        if n < 3: 
            print()
            sonuc=()
            sayilar.sort()
            for i in range(n-2):
                if not (i==0 or sayilar[i] == sayilar[i-1]):
                    j, k = i +1, n-1
                    while j<k:
                        toplam= sayilar[i]+ sayilar[j]+ sayilar[k]
                        if sum ==0 :
                            sonuc.append([sayilar[i], sayilar[j], sayilar[k]])
                            while j<k and sayilar[j]== sayilar[j+1]: j= j+1
                            while j<k and sayilar[k]== sayilar[k-1]: k= k-1
                            j, k = j+1, k-1
                        elif toplam> 0: k= k-1
                        else: j= j+1
                        print(sonuc)
                        
