from django.shortcuts import render
from .models import Alumno, Nota
from datetime import date

def inicio(request):
    return render(request, 'base/index.html')

def vista_nota_necesaria(request):
    alumnos = Alumno.objects.all()
    resultados = []

    # Fechas límite exactas que definimos para los progresos
    p1_inicio, p1_fin = date(2023, 3, 1), date(2023, 4, 15)
    p2_inicio, p2_fin = date(2023, 11, 1), date(2023, 12, 15)

    for alumno in alumnos:
        # 1. Filtrar las notas por rango de fechas
        notas_p1 = Nota.objects.filter(alumno=alumno, fecha__range=[p1_inicio, p1_fin])
        notas_p2 = Nota.objects.filter(alumno=alumno, fecha__range=[p2_inicio, p2_fin])

        # 2. Calcular los promedios (si no hay notas, el promedio es 0)
        promedio_p1 = sum([n.valor for n in notas_p1]) / len(notas_p1) if notas_p1 else 0
        promedio_p2 = sum([n.valor for n in notas_p2]) / len(notas_p2) if notas_p2 else 0

        # 3. Calcular la nota necesaria para el Progreso 3 (para llegar a 6.0)
        # NUEVOS PESOS: P1 vale 25%, P2 vale 35%, P3 vale 40%
        nota_acumulada = float(promedio_p1) * 0.25 + float(promedio_p2) * 0.35
        nota_necesaria_p3 = (6.0 - nota_acumulada) / 0.40

        # 4. Limpiar los resultados para que tengan sentido lógico
        if nota_necesaria_p3 <= 0:
            estado = "Aprobado"
            nota_necesaria_p3 = 0
        elif nota_necesaria_p3 > 10:
            estado = "Reprobado"
        else:
            estado = "En curso"

        # 5. Guardar la información de este alumno en la lista de resultados
        resultados.append({
            'alumno': alumno,
            'p1': round(promedio_p1, 2),
            'p2': round(promedio_p2, 2),
            'necesita_p3': round(nota_necesaria_p3, 2),
            'estado': estado
        })

    # Finalmente, enviamos todos estos cálculos a una página HTML (Template)
    return render(request, 'base/vista_nota_necesaria.html', {'resultados': resultados})