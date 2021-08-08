import numpy as np
from sklearn.linear_model import LinearRegression

# Program E e yada e ile yeni maaş tahmini yapmakta, C yada c ile sonlandırılmaktadır.Menude ki girdilerin hata kontrolü yapışmıştır.
# Çalışma süresi girilirken lütfen ondalıklı sayıları nokta ile giriniz.(örneğin 5.3)

egitimverisi = np.array([[1.1, 6000], [2.4, 6500], [3, 6100], [5, 8000], [6, 7800], [6.7, 8100], [10, 9700], [11.8, 13500],
               [13, 13000], [17, 16500]])

X = np.array([[1.1], [2.4], [3],[5], [6], [6.7], [10], [11.8], [13], [17]])
Y = np.array([[6000], [6500], [6100], [8000], [7800], [8100], [9700], [13500], [13000], [16500]])

model = LinearRegression()
model.fit(X, Y)

test_yıl = np.array(float(input("Tahmini maaşınızı öğrenmek için lütfen çalıştığınız yıl sayısını giriniz:"))).reshape(1,-1)


tahminimaas=model.predict(test_yıl)

print(f"Girdiğiniz çalışma süresine göre tahmini maaşınız: ", "%.2f" % tahminimaas)

while True:

    print("Başka bir maaş tahmini yapmak ister misiniz?")
    yenigirdi = input("1.Yeni bir maaş tahmini yapmak için lütfen E ye basınız.\n"
                      "2.Programı kapatmak için lütfen C ye basınız.\n")

    if yenigirdi == "E" or yenigirdi == "e":

        test_yıl = np.array(float(input("Tahmini maaşınızı öğrenmek için lütfen çalıştığınız yıl sayısını giriniz:"))).reshape(1, -1)
        tahminimaas = model.predict(test_yıl)
        print(f"Girdiğiniz çalışma yılına göre tahmini maaşınız: ", "%.2f" % tahminimaas)

    elif yenigirdi == "C" or yenigirdi == "c":
        exit()

    else:
        print("Hatalı giriş.Lütfen yeniden giriş yapınız.")


input()


























