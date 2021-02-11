
def nuevaLista()->dict:
    lst = {'ED': 'lista', 'tamano': 0, 'datos':[]}
    return lst

def obt_datos(lst):
    return lst['datos']

def obt_tamaño(lst):
    return lst['tamano']

def ir_a_pos(lst, p):
    return obt_datos(lst)[p-1]

def verificar(lst, est):
    encontrado = False
    i = 1
    while i < obt_tamaño(lst) and not encontrado:
        if ir_a_pos(lst,i) == est:
            encontrado = True
        i += 1
    return (encontrado, i)
    

def agregar_est(lst, est):
    if verificar(lst, est)[0]:
        print('ya existe')
    else:
        obt_datos(lst).append(est)
        lst['tamano'] += 1
    return None

def eliminar_est(lst, est):
    if verificar(lst, est)[0]:
        obt_datos(lst).pop(verificar(lst, est)[1])
        lst['tamano'] -= 1
    else:
        print('no existe')
    return None
    
def actualizar_nombre(lst, est, est_nuevo):
    x = verificar(lst, est)
    if x[0]:
        obt_datos(lst)[x[1]] = est_nuevo
    else:
        print('no existe')
    return None

def orden_lex(est1, est2):
    x = str(est1)
    y = str(est2)
    return (x<y)

def org_pylist(lst:list, cmp_function):
    cambios = 1
    while not cambios == 0:
        cambios = 0
        i = 0
        while i < len(lst)-1:
            if not cmp_function(lst[i], lst[i+1]):
                comodin = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = comodin
                cambios += 1
            i += 1

def org_lista(lst)->dict:
    l = obt_datos(lst)
    org_pylist(l)
    lista_nueva = nuevaLista()
    lista_nueva['datos'] = l
    lista_nueva['tamano'] = obt_tamaño(lst)
    return lista_nueva

'''l = ['c','d','a','1','guau', '3']
org_pylist(l, orden_lex)
print(l)'''