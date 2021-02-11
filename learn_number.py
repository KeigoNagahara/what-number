from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# sklearnに入っている数字のデータセット
X, y = datasets.load_digits(return_X_y=True)
clf = LogisticRegression(random_state=0, solver='liblinear', multi_class='auto')
#これで学習させる
clf.fit(X,y)

# 学習したモデルをpickle化
with open('trained-model.pickle', 'wb') as f:
    pickle.dump(clf, f)

print("learned")

# 正確性テスト
# 教師データとテストデータの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# 同じくロジスティック回帰モデルをつかう
clf_acc = LogisticRegression(random_state=0, solver='liblinear', multi_class='auto')
clf_acc.fit(X_train, y_train)
# ラベルを予測
y_pred = clf_acc.predict(X_test)
# テストの正解率
print(accuracy_score(y_test, y_pred))
