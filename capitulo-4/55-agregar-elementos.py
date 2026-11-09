expresiones = ["x","2x","x+2","3x+6","5x²+6"]

expresiones.append("4x-9")
print(expresiones)

expresiones.insert(0,"-10+x")
print(expresiones)

expresiones.extend(["5x","9x+8"])
print(expresiones)

expresiones += ["9x+7","9x+5"]
print(expresiones)