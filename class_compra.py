from class_estoque import *
import mysql.connector

class Compra:
    def __init__(self):
        self.add = Estoque()
        self.codstr = []
        self.conet = mysql.connector.connect(
            host = 'Localhost',
            user= 'root',
            password = 'q1w2e3',
            database = 'estoque'

        )
        self.curs = self.conet.cursor()
        self.history_buy = []


    def comprar(self):
        list = []
        self.curs.execute(f'select cod from produto;')
        var = self.curs.fetchall()
        for i  in var:
            list.append(var)

        listcode = str(list)
        self.curs.execute(f'')

        print(listcode)


        print('|■■■■■■■■■■■■■■■■■■■■■■■■■■|')
        print('|Informe o codigo desejado:|')
        print('|■■■■■■■■■■■■■■■■■■■■■■■■■■|')    
        verify = str(input('|:'))
        print(verify)
        if verify in listcode:
                convert = int(verify)
                self.history_buy.append(convert)
                print(self.history_buy)
               
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ')
                print('---=======--------=======-------=====-----=====---')
                print('        •••Digite a quantidade Desejada•••        ')
                print('---=======--------=======-------=====-----=====---')
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                quantidade =  int(input('|:'))
                intcode = int(convert)
                
                

                self.curs.execute(f'update produto set  quan = (quan + {quantidade}) where cod = {intcode}')
                self.conet.commit()
                print(f' QUANTIDADE SOLICITADA::•╫╫ {quantidade} ╫╫• FORAM  COMPRADOS COM SUCESSO!!') 
        
