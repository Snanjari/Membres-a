from abc import ABC, abstractmethod


class Membresia(ABC):
    """
    Clase abstracta base para las membresías.
    """

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """
        Inicializa una membresía con el correo del suscriptor y el número de tarjeta.

        Args:
            correo_suscriptor (str): Correo electrónico del suscriptor.
            numero_tarjeta (str): Número de tarjeta de la membresía.
        """
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        """
        Retorna el correo del suscriptor.

        Returns:
            str: Correo del suscriptor.
        """
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        """
        Retorna el número de tarjeta de la membresía.

        Returns:
            str: Número de tarjeta de la membresía.
        """
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción de la membresía.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        """
        Crea una nueva membresía según el tipo especificado.

        Args:
            nueva_membresia (int): Tipo de membresía.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        if nueva_membresia == 1:
            return BasicaMembresia(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return FamiliarMembresia(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexionMembresia(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return ProMembresia(self.correo_suscriptor, self.numero_tarjeta)


class GratisMembresia(Membresia):
    """
    Clase para la membresía gratuita.
    """
    costo = 0
    cantidad_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción de la membresía gratuita.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        if nueva_membresia < 1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


class BasicaMembresia(Membresia):
    """
    Clase para la membresía básica.
    """
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)

        if isinstance(self, FamiliarMembresia) or isinstance(self, SinConexionMembresia):
            self.__dias_regalo = 7

        elif isinstance(self, ProMembresia):
            self.__dias_regalo = 15

    def cancelar_suscripcion(self):
        """
        Cancela la suscripción de la membresía básica.

        Returns:
            GratisMembresia: Objeto de membresía gratuita.
        """
        return GratisMembresia(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción de la membresía básica.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


class FamiliarMembresia(BasicaMembresia):
    """
    Clase para la membresía familiar.
    """
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción de la membresía familiar.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        pass


class SinConexionMembresia(BasicaMembresia):
    """
    Clase para la membresía sin conexión.
    """
    costo = 3500

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción de la membresía sin conexión.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
        pass


class ProMembresia(FamiliarMembresia, SinConexionMembresia):
    """
    Clase para la membresía Pro.
    """
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        """
        Cambia la suscripción de la membresía Pro.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


# Se crea una instancia de la membresía gratuita (GratisMembresia) con el correo electrónico "correo@prueba.cl" y el número de tarjeta "123 456 789".
g = GratisMembresia("correo@prueba.cl", "123 456 789")
# Se imprime el tipo de objeto de la instancia g (GratisMembresia).
print(type(g))
# Se cambia la suscripción de la membresía gratuita (g) a una membresía básica (BasicaMembresia).
b = g.cambiar_suscripcion(1)
# Se imprime el tipo de objeto de la instancia b (BasicaMembresia).
print(type(b))
# Se cambia la suscripción de la membresía básica (b) a una membresía familiar (FamiliarMembresia).
f = b.cambiar_suscripcion(2)
# Se imprime el tipo de objeto de la instancia f (FamiliarMembresia).
print(type(f))
# Se omite el resto del código, ya que la variable sc no se utiliza más adelante.
