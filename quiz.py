import json
import random
import textwrap
import shutil
import string
from copy import deepcopy


# -------------------- utilidades -------------------- #
def cargar_preguntas(nombre_archivo: str):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return json.load(f)


def ancho_terminal(default: int = 100) -> int:
    """Devuelve el ancho actual de la terminal (o un ancho fijo)."""
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return default


def barajar_opciones(pregunta: dict):
    """
    Mezcla las opciones y devuelve:
      • nuevo_diccionario_opciones
      • letra_correcta_despues_de_barajar
      • mapa  original → nueva
    """
    pares = list(pregunta["opciones"].items())  # [('a', 'Texto A'), ...]
    random.shuffle(pares)                       # 🔀 mezclamos

    letras = string.ascii_lowercase
    nuevas_opciones = {}
    mapa_letras = {}                            # 'a' ➜ 'c', …

    for idx, (letra_orig, texto) in enumerate(pares):
        letra_nueva = letras[idx]
        nuevas_opciones[letra_nueva] = texto
        mapa_letras[letra_orig.lower()] = letra_nueva

    letra_correcta = mapa_letras[pregunta["respuesta"].lower()]
    return nuevas_opciones, letra_correcta, mapa_letras


def adaptar_explicacion(exp: dict, mapa_letras: dict):
    """
    Clona la explicación y reemplaza las letras de porque_erroneas
    por las nuevas letras barajadas.
    """
    exp_mod = deepcopy(exp)

    nuevas_razones = {}
    for letra_orig, razon in exp.get("porque_erroneas", {}).items():
        letra_nueva = mapa_letras.get(letra_orig.lower(), letra_orig)
        nuevas_razones[letra_nueva] = razon
    exp_mod["porque_erroneas"] = nuevas_razones
    return exp_mod


# -------------------- presentación -------------------- #
def mostrar_explicacion(exp: dict):
    print("\nℹ️  Explicación detallada")
    print(f"   🎯 Concepto clave: {exp.get('concepto', '')}")
    print(f"   ✅ Por qué es correcta: {exp.get('porque_correcta', '')}")

    print("   ❌ Por qué las otras son erróneas:")
    for letra, razon in exp.get("porque_erroneas", {}).items():
        texto = textwrap.fill(f"{letra}) {razon}",
                              width=ancho_terminal(),
                              subsequent_indent=" " * 6)
        print(f"      {texto}")

    print(f"   🔎 Resumen: {exp.get('resumen', '')}\n")


# -------------------- lógica del examen -------------------- #
def hacer_examen(preguntas):
    aciertos = 0
    falladas = []

    for idx, p in enumerate(preguntas, 1):
        print(f"\n📖  Pregunta {idx}: {p['pregunta']}")

        # 🔀 barajamos
        opciones, correcta, mapa = barajar_opciones(p)

        for letra, opcion in opciones.items():
            print(f"   {letra}. {opcion}")

        # entrada de usuario
        try:
            respuesta = input("✏️  Tu respuesta: ").strip().lower()
        except UnicodeDecodeError:
            print("⚠️  Error de codificación. Intenta otra vez.")
            respuesta = input("✏️  Tu respuesta (sin caracteres raros): ").strip().lower()

        # evaluación
        if respuesta == correcta:
            print("🎉  ¡Correcto!")
            aciertos += 1
        else:
            print(f"❌  Incorrecto. La respuesta correcta es «{correcta}»")
            falladas.append(p)

        # explicación (adaptada al nuevo orden)
        if "explicacion" in p:
            exp_adaptada = adaptar_explicacion(p["explicacion"], mapa)
            mostrar_explicacion(exp_adaptada)
        else:
            print("(Sin explicación disponible)\n")

        print(f"📈  Progreso: {aciertos}/{idx} acertadas")

    return aciertos, falladas


# -------------------- programa principal -------------------- #
def main():
    archivo = "preguntas.json"   # <-- cambia aquí si tu JSON se llama distinto
    preguntas = cargar_preguntas(archivo)
    total = len(preguntas)

    try:
        num = int(input(f"¿Cuántas preguntas quieres responder? (máx {total}): "))
        if num < 1 or num > total:
            print("🔢 Número fuera de rango. Se usarán todas las preguntas.")
            num = total
    except ValueError:
        print("🔢 Entrada inválida. Se usarán todas las preguntas.")
        num = total

    random.shuffle(preguntas)
    seleccionadas = preguntas[:num]

    print("\n🚀  Comienza el examen interactivo")
    aciertos, falladas = hacer_examen(seleccionadas)

    # ---- resultado final ----
    print("\n🏁  Resultados finales")
    print(f"   🏆  Aciertos: {aciertos}")
    print(f"   ❌  Fallos: {len(falladas)}")
    porcentaje = (aciertos / num) * 100
    nota10 = round(porcentaje / 10, 2)
    print(f"   📊  Nota: {porcentaje:.1f}%  —  {nota10}/10")

    # ---- recuperación ----
    if falladas:
        repetir = input("🔁  ¿Repetir solo las falladas? (s/n): ").strip().lower()
        if repetir == "s":
            print("\n🔄  Examen de recuperación")
            hacer_examen(falladas)


if __name__ == "__main__":
    main()
