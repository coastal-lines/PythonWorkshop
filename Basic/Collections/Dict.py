#dictonary
myDict = { 
        'Me': 10,
        'Anna': 20,
        'John': 30,
        'Hamza': 40,
        'Victoria': 50
        }
print(myDict)

myDict2 = dict(Me=10, Anna=20)
print(myDict)

print(myDict['Victoria'])
print(myDict.get('Victoria'))

#add
myDict['Denis'] = 60
print(myDict)
#update
myDict['Denis'] = 600
print(myDict)
#del
del myDict['Denis']
print(myDict)

#keys and values to list
k = list(myDict.keys())
print(k)
v = list(myDict.values())
print(v)

print('Anna' in myDict)
print('Lena' not in myDict)

k =  myDict.pop('Me')
print(k)
