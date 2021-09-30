def birthday(x):
    if x == 'apurva':
        print(x,'Birthday is on',data['apurva'])
    if x== 'ankita':
        print(x,"Birthday is on",data['ankita'])
    if x=='madhu':
        print(x, "Birthday is on",data['madhu'])
    if x == 'kavita':
        print(x, "Birthday is on",data['kavita'])
name = ['apurva','ankita','madhu','kavita']
data= {'apurva': '2/11/1996', 'ankita':'1/11/1996', 'madhu':'09/12/1998', 'kavita':'23/04/1998'}
print("Welcome to Birthday Dictionary!!")
print("We know the Birthday's of")
for i in range(len(name)):
    print(name[i])
x = input("Who's birthday would you like to know :")
birthday(x)





