from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

# sklearn de bulunan göğüs kanseri verisetini kullanarak hastalığın iyi ya da kötü huylu olmasını sınıflandırdım.Veri setinin %70'ini makine öğrenmesi için,
# %30'unu test kısmı için kullandım.
# Karar ağacı doğruluk değeri: 0.9064327485380117
# 10-Katlamalı Çapraz Geçerleme Sonucu:  [0.96491228 0.84210526 0.9122807  0.89473684 0.92982456 0.89473684  0.9122807  0.94736842 0.92982456 0.94642857]
# Ek olarak program çalıştırıldığında hata matrisi görselleşmektedir.

veri = load_breast_cancer()

X = veri.data
y = veri.target

kararagaci = DecisionTreeClassifier(random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 0, stratify = y)

kararagaci.fit(X_train, y_train)

tahminisonuc = kararagaci.predict(X_test)

hatamatrisi = confusion_matrix(y_test, tahminisonuc)

print("Karar ağacı doğruluk değeri: " + str(accuracy_score(tahminisonuc, y_test)))

print( "10-Katlamalı Çapraz Geçerleme Sonucu: ", cross_val_score(kararagaci, veri.data, veri.target, cv=10))

plt.matshow(hatamatrisi)
plt.title("Hata Matrisi")
plt.colorbar()
plt.ylabel("True Label")
plt.xlabel("'Predicted Label")
plt.show()

input





