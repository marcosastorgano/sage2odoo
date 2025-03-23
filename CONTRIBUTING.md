# 🛠️ Guía de Contribución a Sage2Odoo

¡Gracias por tu interés en contribuir! 🙌

---

## 📝 Cómo reportar un problema
1. Ve a la pestaña **Issues** del proyecto.
2. Elige la plantilla adecuada:
   - **Reporte de Bug** para errores.
   - **Solicitud de Funcionalidad** para nuevas ideas o mejoras.
3. Rellena los campos obligatorios con el mayor detalle posible.

---

## 🚀 Cómo proponer cambios (Pull Requests)
1. Ve a tu **Issue asignado** o crea uno nuevo si es necesario.
2. Crea una nueva rama directamente desde el Issue en GitHub o desde terminal:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b nombre-descriptivo-#issue
   ```
   Ejemplo:
   ```
   parser-asientos-mejora-#45
   corregir-ci-en-tests-#33
   ```

3. Sigue estas normas al **commitear**:
   ```
   [Bugfix]: Corrige error en parser #45
   [Feature]: Añade validación de XML #48
   ```

4. Verifica que los tests pasan:
   ```bash
   pytest
   ```

5. Sube tu rama y crea un **Pull Request** contra `develop`.
   Completa la plantilla de PR y añade el número de Issue relacionado.

---

## 🌱 Flujo de trabajo Git simplificado

### Ramas principales
| Rama       | Propósito                                                |
|------------|----------------------------------------------------------|
| `main`     | Rama **estable** para producción y releases oficiales.   |
| `develop`  | Rama de **integración continua** donde se prueban cambios antes de release. |

### Ramas de trabajo
- Se crean **desde `develop`**.
- No tienen prefijos tipo `feature/` o `bugfix/`.
- Se recomienda que incluyan el número de Issue para trazabilidad.

#### Ejemplo de nombres:
```
parser-asientos-mejora-#45
correccion-ci-tests-#33
```

---

### Flujo básico
1. Creas una **rama desde `develop`**.
2. Trabajas en la tarea asignada → Commits claros.
3. Creas un **PR hacia `develop`**, enlazando el Issue.
4. Una vez estable, se hace **merge de `develop` a `main`** para el release.
5. Se crean **tags de versión** si aplica:
   ```bash
   git tag -a v1.0.0 -m "Release 1.0.0"
   git push origin v1.0.0
   ```

---

## 🔖 Versionado semántico
Seguimos la convención **SemVer**:
```
MAJOR.MINOR.PATCH
```
- **MAJOR**: Cambios incompatibles en la API.
- **MINOR**: Nuevas funcionalidades sin romper compatibilidad.
- **PATCH**: Correcciones de bugs o pequeñas mejoras.

---

## ✅ Pull Requests: Requisitos mínimos
- Tests que pasan (`pytest`).
- Nombre descriptivo y claro.
- Referencia al Issue (`#45`).
- Documentación actualizada si es necesario.
- Labels (`bug`, `enhancement`, etc).

---

## 📚 Recursos
- [Discussions del proyecto](https://github.com/marcosastorgano/sage2odoo/discussions)
- [Documentación en la Wiki](https://github.com/marcosastorgano/sage2odoo/wiki)

---

# 🙌 ¡Gracias!
Gracias por contribuir a **Sage2Odoo**.
¡Cada mejora cuenta! 🚀