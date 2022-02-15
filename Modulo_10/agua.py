def water_left(astronautas, aguaRestante, diasRestantes):
    for valor in [astronautas, aguaRestante, diasRestantes]:
        try:
            valor / 10
        except TypeError:
            raise TypeError(f"Todos los valores deben de ser números pero se recibió un valor: '{valor}'")
    usoDia = astronautas * 11
    usoTotal = usoDia * diasRestantes
    aguaTotal = aguaRestante - usoTotal
    if aguaTotal < 0:
        raise RuntimeError(f"No hay agua suficiente para {astronautas} astronautas después de {diasRestantes} dias.")
    return f"El agua que resta después de {diasRestantes} dias es: {aguaTotal} litros."

print(water_left("5", 100, 2))
