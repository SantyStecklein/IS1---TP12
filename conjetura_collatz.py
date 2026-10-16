def conjetura_collatz(numero):
    """
    Calcula la secuencia de la Conjetura de Collatz para un número entero positivo
    hasta alcanzar la secuencia de finalización [4, 2, 1].

    Parámetros:
        numero (int): Número entero positivo mayor a cero (> 0).

    Retorna:
        tuple[int, list[int]]: Una tupla con:
            - iteraciones (int): Cantidad total de operaciones realizadas.
            - secuencia (list[int]): Lista con la secuencia completa desde el
              número inicial hasta completar la secuencia 4, 2, 1.

    Lanza:
        ValueError: Si el dato ingresado no es un número entero positivo (> 0).
    """
    # Validación de entrada: debe ser un entero estricto (excluyendo booleanos) y mayor a 0
    if isinstance(numero, bool) or not isinstance(numero, int) or numero <= 0:
        raise ValueError(
            f"Error de validación: '{numero}' no es válido. "
            "Debe ingresar un número entero positivo mayor a cero."
        )

    secuencia = [numero]
    iteraciones = 0
    actual = numero

    # Repetir las operaciones hasta que los últimos tres elementos sean [4, 2, 1]
    while secuencia[-3:] != [4, 2, 1]:
        if actual % 2 == 0:
            actual = actual // 2
        else:
            actual = actual * 3 + 1

        secuencia.append(actual)
        iteraciones += 1

    return iteraciones, secuencia


if __name__ == "__main__":
    # Casos de prueba representativos (incluyendo casos borde 1, 2, 4 y entradas inválidas)
    casos_prueba = [6, 1, 2, 4, 0, -5, 3.5, "texto", True]

    print("=== Pruebas de la Conjetura de Collatz ===\n")
    for caso in casos_prueba:
        try:
            total_iteraciones, recorrido = conjetura_collatz(caso)
            print(f"Entrada: {caso}")
            print(f"  -> Iteraciones totales: {total_iteraciones}")
            print(f"  -> Secuencia completa:  {recorrido}\n")
        except ValueError as error:
            print(f"Entrada: {caso!r} -> {error}\n")