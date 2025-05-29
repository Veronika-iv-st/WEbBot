# 🧠 WebChat AI - Chatbot inteligente con LangChain y tu propia web

Este proyecto crea un **chatbot de preguntas y respuestas** basado en el contenido real de una página web, utilizando:

- `LangChain 0.3`
- `FAISS` como motor de búsqueda semántica
- `ChatOpenAI` para generar respuestas naturales
- `Flask` para servir la API como endpoint `/preguntar`

---

## 🚀 ¿Qué hace?

Cuando levantas el servidor, el agente:

1. Carga las URLs que tú definas
2. Extrae el contenido visible (con `WebBaseLoader`)
3. Divide el texto en chunks y genera embeddings
4. Responde preguntas del usuario usando el contenido real de tu web

---

## 🧩 ¿Para qué sirve?

- Para incrustar un chatbot personalizado en tu sitio WordPress o HTML
- Para ayudar a tus visitantes a entender tu contenido sin tener que buscarlo
- Para crear una API de soporte o asesor virtual, conectado a tu negocio

---

## 🔧 Cómo usarlo

1. Clona el proyecto o copia los archivos
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
````

3. Añade tu clave de OpenAI en un archivo `.env`:

   ```
   OPENAI_API_KEY=tu_clave_aqui
   ```
4. Edita la lista de URLs en `api.py` para que apunten a tu sitio web
5. Ejecuta el servidor:

   ```bash
   python api.py
   ```
6. Envía preguntas al endpoint:

   ```
   POST /preguntar
   {
     "pregunta": "¿Qué servicios ofrece esta empresa?"
   }
   ```

---

## 🌐 ¿Cómo integrarlo?

Puedes integrarlo fácilmente en WordPress o cualquier otra web usando JavaScript `fetch()` apuntando a `/preguntar`.

---

## 🛠 Personalización rápida

Solo cambia esta parte del archivo `api.py`:

```python
urls = [
    "https://tuweb.com/",
    "https://tuweb.com/servicios",
    ...
]
```

Y ya estarás entrenando el chatbot con el contenido de tu sitio.

---

## 💡 Ideal para...

* Agencias
* Consultoras
* Sitios educativos
* Freelancers técnicos
* Cualquier negocio con contenido útil que quiera explicarse mejor

---

## ✨ Creado por Veronika Ivanova 
