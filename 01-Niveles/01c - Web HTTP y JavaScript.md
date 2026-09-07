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

Usá [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development): cómo funciona la web, formularios HTML, CSS básico, JavaScript y solicitudes de datos. Elegí las secciones necesarias para el ejercicio; no completes todo el catálogo. Retomá los tipos del 01 con el [Handbook de TypeScript](https://www.typescriptlang.org/docs/handbook/intro.html). Para el panel existente, seleccioná componentes, props, estado y eventos de [React Learn](https://react.dev/learn); no hace falta completar otro curso entero.

## Diagnóstico

Explicá dónde se valida un formulario y qué pasa si la API responde con un error. Identificá método, URL, cuerpo, estado y respuesta de una petición observada en las herramientas del navegador. Si no podés, leé las secciones introductorias antes de usar un framework.

## Aprender

- HTML semántico, etiquetas y navegación con teclado; estilos suficientes para una pantalla legible.
- Funciones, objetos, arrays, módulos, promesas y manejo de errores en JavaScript. Retomar lo practicado en el 01, sin repetir otro curso de programación.
- HTTP, JSON, estados, formularios y carga de datos. Diferencia entre fallo de red y rechazo de la aplicación.
- Estado de carga, vacío, éxito y error; evitar que un doble clic cree dos solicitudes involuntarias.
- Contrato entre pantalla y API. La validación del navegador ayuda al usuario; la del servidor decide qué acepta el sistema.

## Práctica guiada

En una rama de aprendizaje, usar un componente pequeño del panel React existente para mostrar turnos ficticios: profesional, fecha y estado. Durante este módulo, usar datos locales y una respuesta simulada. Mostrar lista vacía, lista con turnos y error; al enviar, deshabilitar temporalmente el botón y mostrar el resultado. Registrar la petición esperada sin conectar datos reales.

Leer `web/src/admin/api/client.ts` y seguir una llamada hasta Fastify, usando el [mapa del SaaS real](../03-Proyectos/Estudiar%20con%20el%20SaaS%20real.md). Reutilizar el panel; no construir otra aplicación. La simulación no demuestra persistencia ni seguridad del servidor. En 02b se verifica el recorrido con la API existente en un entorno de prueba.

## Práctica independiente

Agregar un filtro por estado y resolver una respuesta lenta o fallida sin copiar la solución. Tipar el registro en TypeScript y explicar qué errores requieren validación en ejecución aunque los tipos compilen.

## Condiciones de salida

Demostrar estados de carga, vacío y error; uso con teclado; envío inválido rechazado por la interfaz; y una explicación del contrato HTTP. Identificar qué comprobaciones faltan del lado servidor. Conservar una captura y el código, no solo una imagen de la pantalla.

## Si no sale

Volver a una función y un formulario sin framework. Si cuesta seguir promesas o arrays, practicar esos conceptos aisladamente. No cambiar de framework para evitar entender el error.

## Cómo comprobar que aprendí

Usá la [comprobación breve](../04-Recursos/Autoevaluacion%20y%20dominio.md): resolver, explicar y probar una variante sin copiar, cumpliendo las condiciones de salida del módulo. Cerrá con tres líneas en [Mi seguimiento](../00-MOC/Estado%20actual.md). No hacen falta puntajes ni otra ficha; una demo hecha con ayuda no demuestra todavía independencia.
