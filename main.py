print("Bem-Vindo")

frutas = ['maça','mamao','Banana']
for i in frutas:
    print(i)

for i in range(len(frutas)):
    print(frutas[i])

while True:
 
    
    nome = input("Qual é o seu nome? \n")
    idade = int(input("Qual é sua idade? \n"))

    if idade == 0:
        break

    if idade >= 18:
        print("Maior de idade")
    elif idade < 18 and idade >= 13:
        print(" Adolescente")
    else:
        print("Criança")
    if nome == "" or nome == "0":
        print("Nome com erro")   