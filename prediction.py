from sklearn import tree
X=[[183,82,44], [169,62,40], [175,75,42], [160,55,38], [178,78,43], [185,88,45], [172,68,41], [165,60,39], [190,95,46], [177,73,42],
[181,80,43], [168,58,39], [174,72,41], [159,53,37], [180,79,43], [186,92,46], [171,67,40], [164,57,38], [193,98,47], [176,74,42],
[179,76,43], [167,61,39], [173,70,41], [161,56,38], [182,81,44], [188,90,45], [170,66,40], [163,59,38], [195,100,48], [175,73,42],
[185,85,44], [166,62,39], [178,77,42], [162,54,37], [183,83,45], [189,94,46], [169,65,40], [160,52,37], [192,97,47], [174,71,41],
[180,78,43], [165,59,38], [172,69,40], [158,50,36], [177,74,42], [187,91,45], [168,63,39], [157,49,36], [194,99,48], [173,72,41],
[184,84,44], [164,58,38], [171,68,40], [156,48,35], [179,75,43], [191,96,47], [167,64,39], [155,47,35], [196,101,49], [176,70,41],
[182,79,43], [162,55,37], [170,67,40], [154,46,34], [175,72,41], [186,89,45], [166,61,39], [153,45,34], [193,98,47], [171,69,40],
[181,81,44], [159,53,36], [169,65,39], [151,44,33], [178,76,42], [190,93,46], [165,60,38], [150,43,33], [195,100,48], [174,71,41]]
Y=['male', 'female', 'male', 'female', 'male', 'male', 'female', 'female', 'male', 'male',
'male', 'female', 'male', 'female', 'male', 'male', 'female', 'female', 'male', 'male',
'male', 'female', 'male', 'female', 'male', 'male', 'female', 'female', 'male', 'male',
'male', 'female', 'male', 'female', 'male', 'male', 'female', 'female', 'male', 'male',
'male', 'female', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'male',
'male', 'female', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'male',
'male', 'female', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'female',
'male', 'female', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'male']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
print("Write height,weight,shoe size :")
height = int(input("Enter height (cm): "))
weight = int(input("Enter weight (kg): "))
shoe_size = int(input("Enter shoe size: "))

data = [height, weight, shoe_size]
print("Collected Data:", data)
prediction=clf.predict([data])
print ('The predicted human is : '+prediction[0])