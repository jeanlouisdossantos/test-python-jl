def calculer_pourcentage_vma(vma, distance, temps):
    # Convertir le temps en secondes
    heures, minutes, secondes = map(int, temps.split(':'))
    temps_total_secondes = heures * 3600 + minutes * 60 + secondes
    
    # Calculer la vitesse moyenne en m/s
    vitesse_moyenne = distance*1000 / temps_total_secondes
    
    # Convertir la VMA en m/s (si elle est en km/h)
    vma_m_s = vma / 3.6
    
    # Calculer le pourcentage de la VMA
    print(vitesse_moyenne, 'vitesse moyenne')
    pourcentage_vma = round((vitesse_moyenne / vma_m_s) * 100, 2)
    
    return pourcentage_vma

vma = int(input("vma "))
distance = int(input("distance "))
temps = input("temps (format hh:mm:ss)")
print(calculer_pourcentage_vma(vma, distance, temps))