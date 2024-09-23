# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:24:18 2024

@author: diego
"""

# Base de datos de conocimiento
conocimiento = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "¿Cómo estás?": "Estoy bien, gracias. ¿Y tú?",
    "¿De qué te gustaría hablar?": "Estoy aquí para ayudarte. ¿De qué tema quieres hablar?"
}

# Función para encontrar coincidencias
def buscar_respuesta(pregunta):
    if pregunta in conocimiento:
        return conocimiento[pregunta]
    else:
        return None

# Función para agregar nuevo conocimiento
def agregar_conocimiento(pregunta, respuesta):
    conocimiento[pregunta] = respuesta
    print(f"Nuevo conocimiento agregado: '{pregunta}' -> '{respuesta}'")

# Chat principal
def iniciar_chat():
    while True:
        # Recibir entrada del usuario
        pregunta = input("Usuario: ")
# Iniciar el chat
iniciar_chat()
