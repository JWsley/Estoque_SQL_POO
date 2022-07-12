from class_estoque import *



class Venda:
    def __init__(self):
        self.remove = Estoque()
       
        self.conet = mysql.connector.connect(
            host = 'Localhost',
            user= 'root',
            password = 'q1w2e3',
            database = 'estoque'

        )
        self.curs = self.conet.cursor()
        self.history_sell = []
        

    def vender(self):

        list = []
        self.curs.execute(f'select cod from produto;')
        var = self.curs.fetchall()
        for i  in var:
            list.append(var)

        listcode = str(list)

        print(listcode)


        print('|■■■■■■■■■■■■■■■■■■■■■■■■■■|')
        print('|Informe o codigo desejado:|')
        print('|■■■■■■■■■■■■■■■■■■■■■■■■■■|')    
        verify = str(input('|:'))
        print(verify)
        if verify in listcode:
                convert = int(verify)
                self.history_sell.append(convert)
               
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ')
                print('---=======--------=======-------=====-----=====---')
                print('        •••Digite a quantidade Desejada•••        ')
                print('---=======--------=======-------=====-----=====---')
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                quantidade =  int(input('|:'))
                intcode = int(convert)

                self.curs.execute(f'update produto set  quan = (quan - {quantidade}) where cod = {intcode} and quan > {quantidade}')
                self.conet.commit()
                print(f' QUANTIDADE SOLICITADA::•╫╫ { quantidade } ╫╫• FORAM  VENDIDOS COM SUCESSO$!!') 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''rint('|■■■■■■■■■■■■■■■■■■■■■■■■■■|')
        print('|Informe o codigo desejado:|')
        print('|■■■■■■■■■■■■■■■■■■■■■■■■■■|')    
        verify = str(input('|:'))
        for i in range(len(self.remove.armazena)):
            if verify == self.remove.armazena[i].cod:
                self.codstr2.append(self.remove.armazena[i].cod)
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ')
                print('---=======--------=======-------=====-----=====---')
                print('        •••Digite a quantidade Desejada•••        ')
                print('---=======--------=======-------=====-----=====---')
                print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
                a = int(input('|:'))
                if a<=self.remove.armazena[i].quan:
                    self.remove.armazena[i].quan -= a
                    print(f' QUANTIDADE SOLICITADA::•╫╫ { a } ╫╫• FORAM  VENDIDOS COM SUCESSO$!!\n POSSUE: { self.remove.armazena[i].quan} DISPONIVEL...') 
                else:
                    print('VALOR EXCEDIDO...')


                    
                '''