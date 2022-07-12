import mysql.connector

from class_estoque import Estoque
from class_fabric import Fabric
from class_info import *
class Db_estoque:

    def __init__(self):
        self.cConnect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'q1w2e3',
            database = 'estoque'
        ) 
        self.mycursor = self.cConnect.cursor()
        self.Estq = Estoque()
        self.fabr = Fabric()
        self.quan_inicial = 0

        

    def exib(self):
        self.mycursor.execute('select * from estoque'  )
        list = self.mycursor.fetchall()
        for i in list:
           print('==================================================')
           print("•",i,">>>")
           print('==================================================')

#U


    def update(self):
        nome  = input('Informe um novo nome:')
        cod  = int(input('Informe o codigo:'))
        sql = f'update pessoas set nome = "{nome}" where id="{cod}"'
        self.mycursor.execute(sql)
        self.cConnect.commit()





#D

    def delete(self):
        cod2  = int(input('Informe o codigo:'))
        sql2 = f'delete from pessoas 2 where id = {cod2}'
        self.mycursor.execute(sql2)
        self.conexao.commit()



    def cadastrar_produto(self):
        list = []
        codl = []

        self.mycursor.execute(f'select nomeFabri from fabricante;')
        var = self.mycursor.fetchall()

        for i  in var:
            list.append(var)
           
        liststr = str(list)
        
       
        print('----------------------------- -----------------------------\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

        cod = len(self.Estq.armazena)+1
        print(f'Codigo gerado:',cod)
        nome  = input('Informe um novo nome:')
        fabric_des = input('Informe a emrpesa fornecedora:')
        
        if fabric_des in liststr:
            print('.............  ............................... ............... ............ .......... ........ ....')
            
            executesql = f'insert into produto (nome,empr,quan) value ("{nome}","{fabric_des}",{self.quan_inicial})'
            self.mycursor.execute(executesql)
            self.cConnect.commit() 
            self.Estq.armazena.append(Info(cod=cod, nome=nome,fabric=fabric_des,quan=self.quan_inicial))
            print('Cadastro efetuado com sucesso!!!')
        else:
            print('erro!!!')



    def listar_tudo(self):
        self.mycursor.execute('select * from  produto' )
        list = self.mycursor.fetchall()
        for i in list:
           print('==================================================')
           print("•",i,">>>")
           print('==================================================')



    def listar_unidade(self,code):
        
        if code == '':
            self.mycursor.execute('select * from  produto' )
            list = self.mycursor.fetchall()
            for i in list:
                print('==================================================')
                print("•",i,">>>")
                print('==================================================')
                return i
        
        else:
            self.mycursor.execute(f'select * from  produto where cod={code}' )
            list = self.mycursor.fetchall()
            for i in list:
            
                print('==================================================')
                print("•",i,">>>")
                print('==================================================')
                return i

    
    def update_produto(self,cod,new_name):
        code = input('insira o codigo do produto:')
        new_name = input('Digite o novo nome:')
        self.mycursor.execute(f'update produto set nome = "{new_name}" where cod={code}' )
        self.cConnect.commit()
       


    



    '''else:
            print('Empresa inexistente!')
            print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n----------------------------- -----------------------------')'''
           

    '''def create(self):
        cod = len(self.Estq.armazena)+1
        print(f'Codigo gerado:{cod}')
        nome  = input('Informe um novo nome:')
        quant  = input('Informe a quantidade desejada:')
        self.mycursor.execute(f'insert into produto (nome,quan) value ("{nome}","{quant}")')
        self.cConnect.commit()   #EXECUTA O SCRIPT SQL NO BANCO'''




    