---
id: "01c"
tags: [nivel, ia-aplicada, saas]
revisado: 2026-09-07
---

# 01c - Web, HTTP y JavaScript

Consultá horas y prerrequisitos en el [catálogo](../00-MOC/Catalogo%20de%20modulos.md). La carga cubre el ejercicio acotado de este módulo, con lectura, corrección y primer repaso; no un curso entero más el producto completo.

## Resultado

Comprender el recorrido navegador → petición → servidor → respuesta y construir una pantalla administrativa pequeña. Reconocer qué se ejecuta en el navegador y qué en el servidor antes de pedir cambios a un asistente.

## Recurso y lectura seleccionada

Usá [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development): cómo funciona la web, formularios HTML, CSS básico, JavaScript y solicitudes de datos. Elegí las secciones necesarias para el ejercicio; no completes todo el catálogo. El [Handbook de TypeScript](https://www.typescriptlang.org/docs/handbook/intro.html) es una extensión si el SaaS ya utiliza TypeScript, después de poder leer JavaScript.

## Diagnóstico

Explicá dónde se valida un formulario y qué pasa si la API responde con un error. Identificá método, URL, cuerpo, estado y respuesta de una petición observada en las herramientas del navegador. Si no podés, leé las secciones introductorias antes de usar un framework.

## Aprender

- HTML semántico, etiquetas y navegación con teclado; estilos suficientes para una pantalla legible.
- Funciones, objetos, arrays, módulos, promesas y manejo de errores en JavaScript. Comparar con Python sin repetir todo un curso de programación.
- HTTP, JSON, estados, formularios y carga de datos. Diferencia entre fallo de red y rechazo de la aplicación.
- Estado de carga, vacío, éxito y error; evitar que un doble clic cree dos solicitudes involuntarias.
- Contrato entre pantalla y API. La validación del navegador ayuda al usuario; la del servidor decide qué acepta el sistema.

## Práctica guiada

Crear una pantalla de turnos ficticios: profesional, fecha y estado. Durante este módulo, usar datos locales y una respuesta simulada. Mostrar lista vacía, lista con turnos y error; al enviar, deshabilitar temporalmente el botón y mostrar el resultado. Registrar la petición esperada sin conectar datos reales.

La simulación no demuestra persistencia ni seguridad del servidor. Se sustituye por una API real en 02b.

## Práctica independiente

Agregar un filtro por estado y resolver una respuesta lenta o fallida sin copiar la solución. Si el SaaS utiliza TypeScript, tipar el registro y explicar qué errores requieren validación en ejecución aunque los tipos compilen.

## Condiciones de salida

Demostrar estados de carga, vacío y error; uso con teclado; envío inválido rechazado por la interfaz; y una explicación del contrato HTTP. Identificar qué comprobaciones faltan del lado servidor. Conservar una captura y el código, no solo una imagen de la pantalla.

## Si no sale

Volver a una función y un formulario sin framework. Si cuesta seguir promesas o arrays, practicar esos conceptos aisladamente. No cambiar de framework para evitar entender el error.

## Evaluación y retención

Aplicá la [rúbrica de dominio](../04-Recursos/Autoevaluacion%20y%20dominio.md): implementación, comparación válida, explicación propia y transferencia, de 0 a 2 cada una. Para dominio: 7/8 como mínimo y ninguna dimensión en 0. Guardá evidencia y ayuda usada en `Mi-progreso/`; repetir una variante a los 7 días y reconstruir el razonamiento a los 30. Una demo que funciona con ayuda no acredita todavía independencia.
