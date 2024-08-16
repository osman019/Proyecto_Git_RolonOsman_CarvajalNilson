import funciones.globales as  fg

def mainmenu(op):
    title = """
    ***************************
    *                         *
    *       SUCURSALES        *
    *                         *    
    ***************************
    
    ELIGA UNA OPCION DISPLONIBLE
    """
    
    mainmenuop = "1.Ver sucursales\n2.Registrar sucursales\n3.Editar\n4.salir"
    fg.borar_pantalla
    if (op !=3):
     print(title)
     print(mainmenuop)
     try:
        opcion = int(input(':)'))
     except ValueError:
        print('error en la opcion ingresada ')
        fg.pausar_pantalla()
        mainmenu(0)
     else:
        match(opcion):
           case 1:
              uie.menusucursales(0)
           case 2:
               up.area-registro(0)
           case 3:
               uict.editar(0)
           case 4:  
              print("hasta luego") 
           case _:
              print('opcion ingresada no esta en el menu de opciones')
              fg.pausar_pantalla
              mainmenu(0)