# Presentación
<i><b>Asignatura:</b></i> Big Data
<br>
<i><b>Estudiante:</b></i> Edna Sofía Orjuela Puentes
<br>
<i><b>Fecha:</b></i>20/04/23
<br>
</p>

# Objetivo
El objetivo es automatizar el proceso de recolección, transformación y carga de datos para mejorar la eficiencia y la precisión en la gestión de información de periódicos, El Tiempo y el Espectador.

# Procedimiento

Desarrollar los ETL y un Workflow en AWS Glue para la descarga de información de periódicos (eltiempo y el espectador):

a) Crear un Job en AWS Glue(con un trigger) que descargue cada dia la página principal de
el Tiempo y El Espectador(o publímetro).
La información debe quedar en S3 con la estructura:
• s3://bucket/headlines/raw/contenido-yyyy-mm-dd.html

b) Una vez llega el archivo a la carpeta raw, se debe activar un segundo job que procese los
datos que llegaron utilizando Beautifulsoup. Este proceso debe extraer la categoría, el
titular y el enlace para cada noticia. Estos datos se deben guardar en un csv en la
siguiente ruta:

• s3://bucket/headlines/final/periodico=xxx/year=xxx/month=xxx/day=xxx

Para usar paquetes externos revisar:
https://aws.amazon.com/es/premiumsupport/knowledge-center/glue-version2-external-python-libraries/

c) Una vez terminados estos jobs, se debe activar un crawler que actualice el catálogo de
AWS Glue y permita visualizar los datos en AWS Athena.

d) Crear un Job que inserte la información en una base de datos MYSQL(usando aws glue connectors y aws job). Para esto se debe crear la BD de MYSQL en RDS con la respectiva tabla. Luego se debe mapear con un crawler al catálogo del glue. Finalmente crear el job con la interfaz que copie de tabla a tabla(la que representa s3 y la que representa RDS en el catálogo).
- Activar la opción “job bookmarks” cuando se cree el job por interfaz. Esto permite que glue lleve una trazabilidad de los datos insertados y evita que se vuelvan a insertar datos ya insertados.

# Resultado
![WORKFLOW](https://user-images.githubusercontent.com/65740725/233823217-3a9dcc26-14cf-468f-9e99-11c7dcce22e5.png)




