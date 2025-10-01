# PROYECTO-INTEGRADOR-G1-VeriFactura
Automatización de Facturas Vehiculares con IA: la banca local,  debe registrar y validar información proveniente de facturas emitidas por concesionarias antes de conceder préstamos vehiculares. Nuestro servicio recibe la información de facturas de múltiples formatos, captura siete campos clave, normaliza los formatos, genera un JSON estandarizado. 

**OBJETIVO GENERAL**

Desarrollar “VeriFactura”, una solución híbrida de IA que integra visión por computador y LLM, destinada a automatizar la captura de facturas vehiculares recibidas por la banca, desde diversas fuentes y formatos, asegurando una precisión superior al 95% en datos críticos, utilizando datos reales de Scribd complementados con generación sintética limitada, para ser implementada en 6 semanas.

**OBJETIVOS ESPECÍFICOS**

Durante el desarrollo de “VeriFactura” se pretende:

●	 Alcanzar un F1-Score mínimo de 0.95 en la extracción automática de datos críticos de facturas vehiculares, que asegurar alta precisión y equilibrio en la clasificación de datos.

●	Mantener la tasa de error OCR en campos críticos (como VIN y RUC) por debajo del 10%, minimizando falsos positivos garantizando la exactitud del procesamiento.

●	 Reducir la necesidad de intervención manual a menos del 20%, optimizando el uso de IA híbrida para minimizar errores que requieren corrección humana.

●	 Asegurar que el tiempo de procesamiento por factura se mantenga entre 5 y 30 segundos, garantizando una respuesta en tiempo real para soportar la operación bancaria continua.

**ALCANCE INCLUIDO**
 
Considerando el objetivo general y los objetivos específicos planteados, y de acuerdo al flujo de “VeriFactura” (recepción, filtrado,OCR, Modelo entrenado (LLM), resulatdos), se detallan las siguientes funcionalidades técnicas:

1. Módulo de Recepción y Pre-procesamiento de Documentos:
Ingreso de Facturas Multi-Fuente a la API: Facturas vehiculares en diversos formatos: PDF, JPG, PNG, XML.
Filtrado y Clasificación de Documentos: a través de un algoritmo identifica si el documento es un escaneo, fotografía, documento digital (PDF/Word), o texto plano.
Derivación al motor correspondiente: Dirigir el documento al motor de procesamiento apropiado: LLM para texto plano, OCR para imágenes/escaneos.

2. Módulo de Procesamiento con Lenguaje Natural (LLM) para Texto Plano:
Extracción de Información:

○	Reconocimiento de entidades nombradas (NER): Identificar y extraer entidades relevantes como:

■	Nombre y RUC del emisor (concesionaria).

■	Nombre y RUC del receptor (banco/cliente).

■	Número de factura.

■	Fecha de emisión.

■	Chasis - VIN (Vehicle Identification Number).

■	TOTAL.

■	IVA.

■	Marca

■	Tipo

■	Clase

■	Modelo

■	Color

■	Código de motor

■	RAMV

■	Año

**Validación y Normalización de Datos:**


○	Validación de formatos: Verificar que los datos extraídos cumplan con formatos esperados (ej. formato del RUC, formato de fecha).
○	Normalización de datos: Estandarizar los datos extraídos (ej. convertir todas las fechas al mismo formato).
