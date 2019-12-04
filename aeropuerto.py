class Aeropuerto:
    ''' Representa un aeropuerto '''
    def __init__(self, ciudad, codigo, latitud, longitud):
        self._ciudad = ciudad
        self._codigo = codigo
        self.latitud = latitud
        self.longitud = longitud

    def ciudad(self):
        return self.ciudad

    def codigo(self):
        return self.codigo

    def ubicacion(self):
        return (self.longitud, self.latitud)