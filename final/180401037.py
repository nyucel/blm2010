#Berivan Aras
#180401037

def yamuk(k,a,b):
    x_delta = 0.0001
    m, sonuc = int((b-a)/x_delta), 0

    for i in range(1,m):
        sonuc += g(k,a+i * x_delta)
    integral = (x_delta/2) * (g(k,a) + g(g,b) + 2*sonuc)
    
    print("integral sonucu : ", integral)


def veriyle_bulma(veri,a,b):
    f,h = 1, veri[a-1]
    
    while(a<b):
        
        h = h + (veri[a-1] + veri[a+f-1]) * f/2
        a = a + f
    print("integral sonucu : " ,h)


def best_polynomial(pol2,pol1):
    eniyi_pol1, eniyi_pol2 = 0, 0

    for j in range(len(pol1)):
        if (pol1[j] > eniyi_pol1):
            eniyi_pol1 = pol1[j]
            eniyi_pol2 = pol2[j]
            
    return eniyi_pol2


def g(k,x):
    topsonucu = 0
    for j in range(len(k)):
        topsonucu += (x**j) * g[j]
        
    return topsonucu


def interpolasyon(derece,veri):
    matrix=[]
    d=0

    for i in range(derece+1):
        line = []
        for j in range(derece+1):
            toplam=0
            for k in range(1,len(veri)+1):
                toplam += k**d
            line.append(toplam)
            d = d + 1
        matrix.append(line)
        d -= derece


    cozum = []
    for i in range(derece+1):
        toplam=0
        for j in range(len(veri)):
            toplam += veri[j]*(j+1)**i
        cozum.append(toplam)


    for i in range(derece+1):
        cozum[i]=cozum[i]/matrix[i][i]
        
    y_ortalama = 0
    
    for i in range (len(veri)):
        y_ortalama += veri[i]
        
    y_ortalama = y_ortalama/len(veri)
    
    y_ortalama_t, y_ortalama_r = 0, 0
    
    for i in range(len(veri)):
        z = veri[i]
        y_ortalama_t += (veri[i]-y_ortalama)**2
        
        for j in range(len(cozum)):
            z -= cozum[j]*(i+1)**j
        z=z**2
        y_ortalama_r += z
        
    n=((y_ortalama_t - y_ortalama_r)/y_ortalama_t)**(1/2)
    
    return cozum,n

file = open("../../Documents/GitHub/blm2010/final/veriler.txt", "r")

veri = file.readlines()

for i in range(len(veri)):
    veri[i]=int(veri[i])


pol1,n1 = interpolasyon(1,veri)

pol2,n2 = interpolasyon(2,veri)

pol3,n3 = interpolasyon(3,veri)

pol4,n4 = interpolasyon(4,veri)

pol5,n5 = interpolasyon(5,veri)

pol6,n6 = interpolasyon(6,veri)

file.close()

katsayılar = [pol1,pol2,pol3,pol4,pol5,pol6]

polinom_bulma = [n1,n2,n3,n4,n5,n6]


eniyi_pol2 = best_polynomial(pol2,pol1)

a=7 #18040103-7
b=len(veri)

veriyle_bulma(veri,a,b)
yamuk(eniyi_pol2, a, b)

def yorum(file2):
    file2.write("Gerçek veriler kullanılarak yapılan işlem sonucu ile polinom kullanılarak yapılan işlemin sonucu \n"
                "birbirinden farklı çıkmaktadır.Bunun sebebi polinom kullanarak bulduğumuz verilerin gerçekte olan \n"
                "verilerden farklı olmasıdır")
    
file2 = open("180401037_yorum.txt","w")
yorum(file2)
file2.close()
