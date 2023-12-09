class OdevCozumu:
    def TwoSum(self, sayilar: list[int], hedef: int ): 
        for i in range(len(sayilar)-1):
            for j in range(i+1, len(sayilar)):
                if sayilar[i]+ sayilar[j]== hedef:
                    print([i,j])
               
            