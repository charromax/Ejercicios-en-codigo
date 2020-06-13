
def semana(i):                          # semana es una FUNCION que devuelve un dia de la semana 
        diasDeLaSemana={                # basado en un ARGUMENTO i de tipo int
                0:'Domingo',            # diasDeLaSemana es un objeto diccionario
                1:'Lunes',
                2:'Martes',
                3:'Miercoles',
                4:'Jueves',
                5:'Viernes',
                6:'Sabado'
             }
        return diasDeLaSemana.get(i,"el dia Osvaldo todavia no existe")


print(semana(5))