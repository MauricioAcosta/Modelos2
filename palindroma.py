def palindromo(s):
    print("hola")
    return (len(s)<2)or(s[0]!=s[-1])or(palindromo(s[1:-1]))
print("ingrese la palabra o frase")
frase = input()
if(frase==palindromo(frase)):
    print("es palindroma")
else:
    print("no es palindroma")
