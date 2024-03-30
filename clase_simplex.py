import numpy as np

class SIMPLEX:

    def __init__(self, c, A, b):
        self.__c = c            # coeficientes de la función objetivo
        self.__A = A            # restricciones del problema
        self.__b = b            # vector de soluciones
        self.m, self.n = A.shape
        self.iteracion=1

    def calcula(self):

        # Fase 1: Introducir variables artificiales
        c_fase1 = np.concatenate((np.zeros(self.n), np.ones(self.m)))
        A_fase1 = np.hstack((self.__A, np.eye(self.m)))
        self.base = np.arange(self.n, self.n + self.m)
        self.no_base = np.arange(self.n)

        # Resolver problema de SBF fase 1
        resolvemos_fase1 = self.fase1_1(A_fase1, self.__b, c_fase1)
        if resolvemos_fase1 == 'No hay solución factible':
            return resolvemos_fase1
        # Fase 2: Resolver problema original
        self.no_base = self.no_base[self.no_base < self.n]
        resultado=self.SIMPLEX(self.__A, self.__b, self.__c)
        if resultado=='No acotado':
            print()
            print(resultado)
            return resultado
        else:
            print()
            print('Solució òptima trobada:')
            print()
            print('vb = ',resultado[0])
            print('Xb = ',resultado[1])
            print('z = ',resultado[2])
            print('r = ',resultado[3])
            return resultado
    def theta(self,d_b,x_b):

        menor=float('inf')
        theta=[]
        for i,valor in enumerate(d_b):
            if valor<0:
                a=-x_b[i]/valor
                theta.append(-x_b[i]/valor)
                if a<=menor:
                        menor=a
                        indice_variable_sale=i
                else:
                    if a<menor:
                        if self.base[i]<self.base[indice_variable_sale]:
                            menor=a
                            indice_variable_sale=i
        return menor,indice_variable_sale
    def actualizacion_inv(self,indice_variable_sale,d_b,B_inv_old):
        fila, columna = B_inv_old.shape
        # Crea una matriz identidad del mismo tamaño
        E = np.eye(fila, columna)
        for i in range(0,fila):
            if i==indice_variable_sale:
                E[i,indice_variable_sale]= (-1/d_b[indice_variable_sale])
            else:
                E[i,indice_variable_sale]= ((-d_b[i])/d_b[indice_variable_sale])
        return np.dot(E,B_inv_old)
        
    def SIMPLEX(self, A, b, c):
        self.no_base.sort()
        B = A[:, self.base]
        An = A[:, self.no_base]
        B_inv = np.linalg.inv(B)
        x_b = np.dot(B_inv, b)
        x_n=np.zeros(len(self.no_base))
        c_b = c[self.base]
        print(c)
        print(self.no_base)
        c_n = c[self.no_base]
        
        r = np.array(c_n - np.dot(np.dot(c_b, B_inv),An))
        z = np.dot(c_b, x_b)+np.dot(c_n, x_n)

        if np.all(r >= 0):
            self.iteracion+=1
            print('Solució òptima trobada, iteració',self.iteracion,'z= ',z)
            print('Fi SIMPLEX primal')
            return [self.base,x_b,z,r]
        
        indice_variable_entra = np.where(r < 0)[0][0]

        d_b = np.dot(-B_inv, A[:, self.no_base[indice_variable_entra]])
        if np.all(d_b >= 0):
            return "No acotado"

        theta,indice_variable_sale=self.theta(d_b,x_b)
        print('Fase 2')
        print('[Dani_Lola_SIMPLEX] Iteració ',self.iteracion,':p = ',indice_variable_sale,', q = ',indice_variable_entra,', B(p) = ',self.base[indice_variable_sale],', theta*= ',theta,', z= ',z)
        self.iteracion+=1

        variable_sale = self.base[indice_variable_sale]
        self.base[indice_variable_sale] = self.no_base[indice_variable_entra]
        self.no_base[indice_variable_entra] = variable_sale
        return self.SIMPLEX2(A,b,c,d_b,indice_variable_sale,B_inv)
    def SIMPLEX2(self,A,b,c,d_b,indice_variable_sale,B_inv_old):
        while True:
            An = A[:, self.no_base]
            B = A[:, self.base]

            B_inv=self.actualizacion_inv(indice_variable_sale,d_b,B_inv_old)
            x_b = np.dot(B_inv, b)
            x_n=np.zeros(len(self.no_base))
            c_b = c[self.base]
            c_n = c[self.no_base]
            z = np.dot(c_b, x_b)+np.dot(c_n, x_n)
            r = np.array(c_n - np.dot(np.dot(c_b, B_inv),An))
        
            if np.all(r >= 0):
                self.iteracion+=1
                print('Solució òptima trobada, iteració',self.iteracion,'z= ',z)
                print('Fi SIMPLEX primal')
                return [self.base,x_b,z,r]
            
            indice_variable_entra = np.where(r < 0)[0][0]

            d_b = np.dot(-B_inv, A[:, self.no_base[indice_variable_entra]])
            if np.all(d_b >= 0):
                return "No acotado"

            theta,indice_variable_sale=self.theta(d_b,x_b)
            print('[Dani_Lola_SIMPLEX] Iteració ',self.iteracion,':p = ',indice_variable_sale,',q = ',indice_variable_entra,',B(p) = ',self.base[indice_variable_sale],',theta*= ',theta,',z= ',z)
            self.iteracion+=1
            variable_sale = self.base[indice_variable_sale]
            self.base[indice_variable_sale] = self.no_base[indice_variable_entra]
            self.no_base[indice_variable_entra] = variable_sale
            
            B_inv_old=B_inv
    def fase1_1(self, A, b, c):
        self.no_base.sort()
        B = A[:, self.base]
        An = A[:, self.no_base]
        B_inv = np.linalg.inv(B)
        x_b = np.dot(B_inv, b)
        x_n=np.zeros(len(self.no_base))
        c_b = c[self.base]
        c_n = c[self.no_base]
        
        r = np.array(c_n - np.dot(np.dot(c_b, B_inv),An))
        z = np.dot(c_b, x_b)+np.dot(c_n, x_n)

        if np.all(r >= 0):
            if z != 0:
                print()
                print("No hay solución factible")
                return "No hay solución factible"
            self.iteracion+=1
            print('Solució básica factible trobada, iteració',self.iteracion)
            return [z, self.base]
        
        indice_variable_entra = np.where(r < 0)[0][0]

        d_b = np.dot(-B_inv, A[:, self.no_base[indice_variable_entra]])
        if np.all(d_b >= 0):
            return "No acotado"

        theta,indice_variable_sale=self.theta(d_b,x_b)
        print('Fase 1')
        print('[Dani_Lola_SIMPLEX] Iteració ',self.iteracion,':p = ',indice_variable_sale,',q = ',indice_variable_entra,',B(p) = ',self.base[indice_variable_sale],',theta*= ',theta,',z= ',z)
        self.iteracion+=1       
        variable_sale = self.base[indice_variable_sale]
        self.base[indice_variable_sale] = self.no_base[indice_variable_entra]
        self.no_base[indice_variable_entra] = variable_sale
        return self.fase1_2(A,b,c,d_b,indice_variable_sale,B_inv)
    def fase1_2(self,A,b,c,d_b,indice_variable_sale,B_inv_old):
        while True:
            B = A[:, self.base]
            An = A[:, self.no_base]
            B_inv=self.actualizacion_inv(indice_variable_sale,d_b,B_inv_old)
            x_b = np.dot(B_inv, b)
            x_n=np.zeros(len(self.no_base))
            c_b = c[self.base]
            c_n = c[self.no_base]
            z = np.dot(c_b, x_b)+np.dot(c_n, x_n)
            r = np.array(c_n - np.dot(np.dot(c_b, B_inv),An))
        
            if np.all(r >= 0):
                if z != 0:
                    print()
                    print("No hay solución factible")
                    return "No hay solución factible"
                self.iteracion+=1
                print('Solució básica factible trobada, iteració',self.iteracion)
                return [z, self.base]
            
            indice_variable_entra = np.where(r < 0)[0][0]

            d_b = np.dot(-B_inv, A[:, self.no_base[indice_variable_entra]])
            if np.all(d_b >= 0):
                return "No acotado"

            theta,indice_variable_sale=self.theta(d_b,x_b)

            print('[Dani_Lola_SIMPLEX] Iteració ',self.iteracion,':p = ',indice_variable_sale,',q = ',indice_variable_entra,',B(p) = ',self.base[indice_variable_sale],',theta*= ',theta,',z= ',z)
            self.iteracion+=1             
            variable_sale = self.base[indice_variable_sale]
            self.base[indice_variable_sale] = self.no_base[indice_variable_entra]
            self.no_base[indice_variable_entra] = variable_sale
            
            B_inv_old=B_inv
