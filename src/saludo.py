"""Modulo con una funcion de saludo."""


def saludar(nombre: str) -> str:
    """Devuelve un saludo para la persona indicada."""
    if not nombre or not nombre.strip():
        raise ValueError("el nombre no puede estar vacio")
    return f"Hola, {nombre}!"
