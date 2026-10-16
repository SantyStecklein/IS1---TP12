def conjetura_collatz(numero):
    """
    Calcula la secuencia de la Conjetura de Collatz para un número entero positivo
    hasta alcanzar la secuencia de finalización [4, 2, 1].

    Parámetros:
        numero (int | str): Número entero positivo mayor a cero (> 0).
            También admite cadenas numéricas provenientes de input().

    Retorna:
        tuple[int, list[int]]: Una tupla con:
            - iteraciones (int): Cantidad total de operaciones realizadas.
            - secuencia (list[int]): Lista con la secuencia completa desde el
              número inicial hasta completar la secuencia 4, 2, 1.

    Lanza:
        ValueError: Si el dato ingresado no es un número entero positivo (> 0).
    """
    valor_original = numero

    # Si el dato proviene de input() (tipo str), intentamos convertirlo solo si representa un entero
    if isinstance(numero, str):
        texto = numero.strip()
        if texto and (texto.isdigit() or (texto[0] in "+-" and texto[1:].isdigit())):
            numero = int(texto)

    # Validación de entrada: debe ser un entero estricto (excluyendo booleanos) y mayor a 0
    if isinstance(numero, bool) or not isinstance(numero, int) or numero <= 0:
        raise ValueError(
            f"Error de validación: '{valor_original}' no es válido. "
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
    num = input("Ingrese el número al que desea aplicar la conjetura de Collatz: ")
    try:
        iteraciones, secuencia = conjetura_collatz(num)
        print(f"Número: {num}")
        print(f"Iteraciones: {iteraciones}")
        print(f"Secuencia: {secuencia}")
    except ValueError as error:
        print(error)