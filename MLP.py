from sklearn.neural_network import MLPClassifier

def train_model(clf):
    ##this is your data that you want to learn from
    ## X_train = describes your data
    ## y_train = labels your data

    ##[0,1] = 2 features with "0" label

    X_train = [[80, 81, 71, 89], [85, 86, 78, 94], [82, 82, 89, 92], [79, 79, 85, 95],
               [82, 85, 80, 97], [79, 81, 84, 88], [91, 92, 94, 97], [81, 83, 86, 94]]

    y_train = [4, 5, 1, 1, 4, 2, 6, 3]

    ##clf.fit only for two classes (eg true and false)

    ##clf.fit(X_train, y_train)

    ##we use clf.partial_fit for 6 classes

    clf.partial_fit(X_train, y_train, classes=[1,2,3,4,5,6])

def test_model(clf):
    X_test = [[96, 96, 96, 96]]

    ##y_test = 

    print(clf.predict(X_test))

    ##does the result match y_test?? - measure this than output the accuracy TP + TN/(TP+FP+FN+TN)
    ## TP = true positive, FP = false positive, FN = false negative, TN = true negative 

def run():
    ##Multi-layer perceprton algorith with 2 layers of size 5, 2 - can be changed, the larger the
    ##number the deeper the network (you want deeper networks if you have lots of data)

    ##solver/optimisation algorithm - https://en.wikipedia.org/wiki/Limited-memory_BFGS

    ##early_stopping is a method to stop overfitting

    ##activation function adds bias - can have sigmoid, tanh, relu etc

    ##learning_rate and momentum are parameters to tweak your training data 
    clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

    train_model(clf)
    test_model(clf)

    ##below is all the properties you can set for the MLPClassifier

    ##MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
    ##       beta_1=0.9, beta_2=0.999, early_stopping=False,
    ##       epsilon=1e-08, hidden_layer_sizes=(5, 2), learning_rate='constant',
    ##       learning_rate_init=0.001, max_iter=200, momentum=0.9,
    ##       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
    ##       solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
    ##       warm_start=False)

