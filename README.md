# 🛒 Inventario RIWI

## 📌 Descripción
**Inventario RIWI** es un programa en Python que permite registrar productos ingresando su **nombre**, **precio** y **cantidad**.  
El sistema valida los datos y calcula automáticamente el **costo total** del producto (`precio × cantidad`).  
Finalmente, muestra una **factura final** con toda la información ingresada.

---

## ⚙️ ¿Qué hace el programa paso a paso?

1. **Muestra un menú inicial**  
   Al ejecutar el programa, aparece el siguiente texto:
   ```text
   =MENU=
2. **Solicita el nombre del producto**  
   - El usuario debe escribir únicamente **letras** (sin números ni símbolos).  
   - Si se escribe algo incorrecto, el programa volverá a pedir el nombre.  
   - Cuando el texto es válido, muestra:
     ```text
     texto valido
     ```

3. **Solicita el precio del producto**  
   - Debe escribirse un **número mayor que cero** (por ejemplo: `20.5`).  
   - Si se ingresa una letra, símbolo o número menor o igual a cero, el programa pedirá nuevamente el valor.
4. **Solicita la cantidad de productos**  
   - Debe escribirse un **número entero positivo** (por ejemplo: `3`).  
   - Si no es válido, el programa pedirá el valor otra vez.

6. **Muestra una factura final** con la información completa:
   ```text
   ===== FACTURA FINAL =====
   Nombre del producto: ...
   Precio unitario: ...
   Cantidad: ...
   Costo total: ...
   ==========================

## 🚀 Cómo usar este programa

### 🔧 Requisitos previos
Antes de ejecutar el programa, asegúrate de tener instalado:
- **Python 3** en tu computadora  
  📥 Descárgalo desde: [https://python.org/downloads/](https://python.org/downloads/)

---

### 💻 Pasos para ejecutar (paso a paso)

#### Para **Windows**:
1. **Descarga** `inventario.py` a tu escritorio o carpeta Downloads.
2. **Click derecho** sobre el archivo `inventario.py` 👆
3. Selecciona **"Abrir con"** → **"Python"**  
   *(Si no aparece Python, ve al método 2)*
4. ¡Listo! Se ejecutará automáticamente 😎

#### Para **Mac**:
1. **Descarga** `inventario.py`.
2. **Click derecho** → **"Abrir con"** → **"Python 3.x"**.
3. El programa se abrirá y funcionará.

#### Para **Linux**:
1. **Click derecho** → **"Abrir con"** → **"Python 3"**.

---

### 💡 Si Python NO aparece en "Abrir con":

**Opción A - Windows:**
1. **Instala Python** marcando ✅ **"Add Python to PATH"** durante la instalación.
2. **Click derecho** → **"Abrir con"** → **"Elegir otra aplicación"** → busca `python.exe`.

---

## 👨‍💻 Autor
**Desarrollado por:** Luis Cala  
📍 **Barranquilla, Atlántico, Colombia**  
🌐 **riwi**  
🗓 **2026**

