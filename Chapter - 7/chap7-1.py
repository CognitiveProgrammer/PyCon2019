# Odd Numbers
for i in range(1,10,2):
    X_train, X_test, y_train, y_test = train_test_split(iris_db.data, iris_db.target, test_size=0.25)
    k_test = KNeighborsClassifier(i)
    k_test.fit(X_train, y_train)
    score = k_test.score(X_test, y_test)
    print("For k => {}  Score =>  {}".format(i, score))

