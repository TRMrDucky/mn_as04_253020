def biseccion(f, xi, xf, eaMax):
    xr = (xi + xf)/2
    i = 0
    ea = 0
    while(True):
        pr = (f(xi) * f(xr))

        if(pr<0):
            xf = xr
            xr = (xi + xf)/2
            ea = errorAprox(xr, xf)
            #Eliminar despues
            print(f"iteracion: {i}")
            print(f"raiz aproximada: {pr}")
            print(f"valor final x: {xf}")
            print(f"valor de la nueva aproximacion: {xr}")
            print(f"error aceptable porcentual: {ea}")
            if(ea < eaMax):
                r = f(pr)
                return {"raiz": pr, "valor_f_en_raiz": r, "iteraciones": i}
                

        elif(pr > 0):
            xi = xr
            xr = (xi + xf)/2
            ea = errorAprox(xr, xi)
            #Eliminar despues
            print(f"iteracion: {i}")
            print(f"raiz aproximada: {pr}")
            print(f"valor final x: {xf}")
            print(f"valor de la nueva aproximacion: {xr}")
            print(f"error aceptable porcentual: {ea}")
            if(ea < eaMax):
                r = f(pr)
                return {"raiz": pr, "valor_f_en_raiz": r, "iteraciones": i}

        elif(pr == 0):
            #Eliminar despues
            print(f"iteracion: {i}")
            print(f"raiz aproximada: {pr}")
            print(f"valor final x: {xf}")
            print(f"valor de la nueva aproximacion: {xr}")
            print(f"error aceptable porcentual: {ea}")
            r = f(pr)
            return {"raiz": pr, "valor_f_en_raiz": r, "iteraciones": i}
            

        
        

        xr = (xi + xf)/2

        i +=1
    

def reglaFalsa(f, xi, xf, eaMax):
    pass
def newtonRaphson(f, df, xi, eaMax):
    pass
def secante(f, e1, e2, eaMax):
    pass

def errorAprox(xrn, xra):
    return abs((xrn - xra)/xrn)*100
