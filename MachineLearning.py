import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv("zoo.csv")#verilerin okunması

X = dataset.iloc[:,1:-1] #ilk column hariç tüm veriler
y = dataset.iloc[:,-1] #son column

#decision tree işlemleri
decision_tree_clf = DecisionTreeClassifier(random_state = 0)
X_train_dt, X_test_dt, y_train_dt, y_test_dt = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 0, stratify = y)
#eğitim
decision_tree_clf.fit(X_train_dt, y_train_dt)
#tahminleme
decision_predict = decision_tree_clf.predict(X_test_dt)

decision_dogruluk = accuracy_score(decision_predict, y_test_dt)
decision_matrix = confusion_matrix(y_test_dt, decision_predict)
decision_fold = cross_val_score(decision_tree_clf, X, y, cv = 10)

#knn işlemleri
standart = StandardScaler()
X_train_kn, X_test_kn, y_train_kn, y_test_kn = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 0, stratify = y)
X_train_kn = standart.fit_transform(X_train_kn)
X_test_kn = standart.fit_transform(X_test_kn)
knn_clf = KNeighborsClassifier(n_neighbors = 3)
#eğitim
knn_clf.fit(X_train_kn,y_train_kn)
#tahminleme
knn_predict = knn_clf.predict(X_test_kn)

knn_dogruluk = accuracy_score(knn_predict,y_test_kn)
knn_matrix = confusion_matrix(y_test_kn,knn_predict)
knn_fold = cross_val_score(knn_clf, X, y, cv = 10)

print("Doğruluk Oranları:", "\n", "Decision Tree için:", decision_dogruluk, "\n", "k-NN için:", knn_dogruluk)
print("Hata Matrisleri:", "\n", "Decision Tree için:\n", decision_matrix, "\n", "k-NN için:\n", knn_matrix)
print("10-Fold Cross Validation Puanları:", "\n", "Decision Tree için:", decision_fold, "\n", "k-NN için:", knn_fold)

#kullanıcı girişi
input = [float(x) for x in input("Tahminlemesini istediğiniz verileri giriniz: ").split(",")]
new_prediction = np.array(input).reshape(1, -1)

decision_result = decision_tree_clf.predict(new_prediction)
knn_result = knn_clf.predict(new_prediction)

print("Decision Tree Tahmini: " , decision_result)
print("k-NN Tahmini: ", knn_result)
