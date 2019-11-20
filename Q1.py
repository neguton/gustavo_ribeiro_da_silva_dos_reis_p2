def path():
    import os
    path = os.getcwd
    return path
def data():
    cadastro=open(path()+"/cadastro.txt","r")
    cont1=0
    cont2=0
    ano=str
    mes=str
    dia=str
    while(cont1<2):
        if(cadastro.read(cont2)==":"):
            cont1+=1
        cont2+=1
    linha_cad1=cadastro.readline()
    for i in range(cont2,cont2+11):
        if(i<cont2+5):
            ano.append(linha_cad1(i))
        elif(cont2+5<i<cont2+8):
            mes.append(linha_cad1(i))
        elif(cont2+8<i<cont2+11)
            dia.append(linha_cad1(i))
    dicio={
        "dia":None,
        "mes":None,
        "ano":None,
    }
    dicio["dia"]=dia
    dicio["mes"]=mes
    dicio["ano"]=ano
    return dicio
def boolstring():
    st=input("inserir resposta da corpo ativo")
    ativo=bool
    if(st=="sim"):
        ativo=true
    elif(st=="não"):
        ativo=false
    elif(st=="sim\n"):
        ativo=true
    elif(st=="não\n"):
        ativo=false
    return ativo
def listastr():
    st=str(input("inserir:"))
    lista=[]
    for i in range(0,len(st)):
        lista.append(i,st[i]+":")
    return lista
def ler():
    lista=[]
    for linha in arquivo
        lista.append(linha)
def main():
    dicio={
        cad1{
            "nome":None,
            "cpf":None,
            "datan":None,
            "datac":None,
            "ativo":None,

        }
        #
        #
        #
        #
        #
    }
    arquivo=open(path+"arquivo.txt","r")
    dicio[cad1["nome"]]=listastr()
    dicio[cad1["cpf"]]=arquivo.read(14)
    dicio[cad1["datan"]]=data()
    dicio[cad1["datac"]]=data()
    dicio[cad1["ativo"]]=boolstring()

    print(dicio)

