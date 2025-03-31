def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    if altura <= 0:
        return "Error: La altura debe ser mayor a 0."
    imc = peso / (altura ** 2)
    return round(imc, 2)

def calcular_igc(imc, edad, sexo):
    """Calcula el Índice de Grasa Corporal (IGC)."""
    if sexo.lower() == "m":
        igc = (1.20 * imc) + (0.23 * edad) - 16.2
    else:
        igc = (1.20 * imc) + (0.23 * edad) - 5.4
    return round(igc, 2)

def calcular_tmb(peso, altura, edad, sexo):
    """Calcula la Tasa Metabólica Basal (TMB)."""
    if sexo.lower() == "m":
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * edad)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura * 100) - (4.3 * edad)
    return round(tmb, 2)
