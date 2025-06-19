#ISE_UGR_examen_practicas
Examen interactivo (tipo test) de **Ingenieria de Servidores** para la parte de prácticas.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## ¿Qué hace este proyecto?  
`quiz.py` lanza un cuestionario en terminal para repasar la asignatura:  
1. `preguntas.json` (157 preguntas máx).  
2. Te pide cuántas preguntas quieres contestar.  
3. Muestra las preguntas aleatoriamente ,cada enunciado con opciones **a-d**(tambien en orden aleatorio); registras tu respuesta.  
4. Corrige al momento, da explicación detallada y va contando aciertos.  
5. Al final puedes repetir las falladas.  

> **Ejemplo rápido**
> ```bash
> $ python3 quiz.py
> ¿Cuántas preguntas quieres responder? (máx 157): 25
> 🚀  Comienza el examen interactivo
> ...
> 🏁  Resultados finales
>    🏆  Aciertos: 22
>    ❌  Fallos: 3
> 🔁  ¿Repetir solo las falladas? (s/n):
> ```

## Instalación  
```bash
git clone https://github.com/franciscojramos/ISE_UGR_examen_praticas)
python3 quiz.py
```
## Autor
**Francisco José Ramos Moya** – código y organización de preguntas.

## Créditos
Algunas preguntas se basan en apuntes de **Sr_Aprobados** subidos a *Wuolah*.

## Descargo de responsabilidad
Este repositorio es **solo orientativo** para estudiar; puede contener preguntas o explicaciones incorrectas.  
El autor **no se hace responsable** de errores ni de los resultados obtenidos en exámenes.  
¡Úsalo bajo tu propio criterio y contrástalo siempre con la bibliografía oficial!

## Contribuir
- Haz un *fork*.  
- Añade o corrige preguntas en el mismo formato **JSON**.  
- Abre un *pull request*.
