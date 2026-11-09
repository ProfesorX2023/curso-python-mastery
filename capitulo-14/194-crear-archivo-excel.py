import openpyxl

wb = openpyxl.Workbook()

hoja = wb.active
hoja.title = "Inventario"

hoja["A1"] = "Producto"
hoja["B1"] = "Precio"
hoja["C1"] = "Stock"

hoja.cell(row = 2, column = 1 , value = "Laptop HP")
hoja.cell(row = 2, column = 2 , value = 8500)
hoja.cell(row = 2, column = 3 , value = 12)

hoja.append(["Mouse Logitech",125.50,45])
hoja.append(["Teclado Mecanico",350.00,28])
hoja.append(["Monitor 24''",2100,15])

wb.save('inventario.xlsx')
print("Archivo guardado!")