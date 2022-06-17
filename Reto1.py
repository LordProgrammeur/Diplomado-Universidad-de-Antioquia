def solucion():
  print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
  nombre=input("Por favor ingrese su nombre: ").capitalize()
  materia=input("Ingrese el nombre de la materia: ").capitalize()
  acumulado_notas=0
  acumulado_porcentaje=0
  acumulador_resultado=0
  resultado=0
  decision="S"
  
  while decision=="S":
    nota=float(input("Ingrese la nota obtenida: "))
    porcentaje=int(input("Ingrese el porcentaje de la nota: "))
    acumulado_notas=acumulado_notas+nota
    acumulado_porcentaje=acumulado_porcentaje+porcentaje
    resultado=nota*porcentaje
    acumulador_resultado=acumulador_resultado+resultado/100
    if acumulado_porcentaje > 100:
      print("El porcentaje evaluado de una materia no puede ser mayor a 100") 
      acumulado_porcentaje=acumulado_porcentaje-porcentaje
      acumulado_notas=acumulado_notas-nota
      acumulador_resultado=acumulador_resultado-resultado/100                   
      nota=float(input("Ingrese la nota obtenida: "))
      porcentaje=int(input("Ingrese el porcentaje de la nota: "))
      acumulado_notas=acumulado_notas+nota
      acumulado_porcentaje=acumulado_porcentaje+porcentaje
      resultado=nota*porcentaje
      acumulador_resultado=acumulador_resultado+resultado/100
    
    if acumulado_porcentaje < 100:
      decision=input("¿Falta añadir notas? S/N: ").capitalize()
      if decision != "S":
        nota_final=float(acumulador_resultado)
        nota_final=round(nota_final,2)
        if acumulador_resultado >= 3 and acumulador_resultado < 5:
          print(f"El estudiante {nombre} curso la materia {materia} y obtuvo {nota_final} resultando en aprobado")
        else:
          print(f"El estudiante {nombre} curso la materia {materia} y obtuvo {nota_final} resultando en reprobado")
    
    if acumulado_porcentaje==100:
      nota_final=float(acumulador_resultado)
      nota_final=round(nota_final,2)
      if acumulador_resultado >= 3 and acumulador_resultado < 5:
        print(f"El estudiante {nombre} curso la materia {materia} y obtuvo {nota_final} resultando en aprobado")
        decision="n" 
      else:
        print(f"El estudiante {nombre} curso la materia {materia} y obtuvo {nota_final} resultando en reprobado")
        decision="n"
