def configurar(host, port, /, timeout=30, *, debug=False):
    '''
    host y port: solo posicionales, estos no se pueden cambiar
    timeout: posicional o nombrado
    dbug"solo nombrado despues del *
    '''

    print(host, port, timeout, debug)

configurar("localhost",8000)
configurar("localhost",8080, timeout=60, debug=True)
#configurar(host="Fibonacci",port=5000)
#configurar("localhost",8081, 60, True)