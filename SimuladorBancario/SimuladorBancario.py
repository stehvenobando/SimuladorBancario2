__author__ = "Stehven Alexander Obando Cordoba"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "stehvenobando@gmail.com"

#----------------------------------------------------------------
# Importaciones
#----------------------------------------------------------------

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Asociaciones
    #----------------------------------------------------------------
    
    __cuentaAhorros=CuentaAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
        # Aqui inicia mi codigo
        self.__cuentaCorriente.ConsignarSaldo(monto)
    
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total actual en todas las cuentas"
    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        # total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        # return total
        # Metodo 2
        return self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite pasar saldo de la cuenta de ahorrros a la cuenta corriente"
    def PasarAhorroACorriente(self):
        # Aqui inicia mi codigo
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)
    __method__ = "Ahorrar"
    __parameter__ = "Monto"
    __returns__ = "ninguno"
    __Description__ = "Pasa de la cuenta corriente a la cuenta de ahorros el valor que se entrega como parámetro (suponiendo que hay suficientes fondos)."
    def Ahorrar(self, monto):
        #aqui va mi codigo
        self.__cuentaAhorros.RetirarValor(monto)
    __method__ = "RetirarTodo"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Retira un valor dado de la cuenta de ahorros (suponiendo que hay suficientes fondos)."
    def RetirarTodo(self, monto):
        #aqui va mi codigo
        self.__cuentaAhorros.RetirarValor(self.__cuentaAhorros.DarSaldo())
        self.__cuentaCorriente.retirarValor(self.__cuentaAhorros.DarSaldo())
    __method__ = "duplicar ahorro"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "duplica la cantidad de dinero que hay en la cuenta de ahorros "
    def DuplicarAhorro(self):
        #aqui va mi codigo
        self.__cuentaAhorros.ConsignarValor(self.__cuentaAhorros.DarSaldo())
    __method__ = "DarSaldo"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo de la cuenta de ahorros"
    __Description__ = "Metodo que muestra el saldo de la cuenta de ahorros"
    def DarSaldoCuentaCorriente(self):
        # Aqui inicia mi codigo
        return self.__cuentaCorriente.DarSaldo()

