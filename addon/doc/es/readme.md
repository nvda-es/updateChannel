# Selector del canal de actualización de NVDA #

* Autor: José Manuel Delicado
* Compatibilidad con NVDA: de 2022.4 en adelante
* Descargar [versión estable][1]

Este complemento te permite descargar e instalar la versión más reciente de
NVDA del tipo elegido sin visitar ninguna página web ni usar tu navegador
web. Es útil cuando, por ejemplo, quieres probar nuevas características que
hay en una versión de desarrollo y después regresar a la versión estable más
reciente. Si pruebas con regularidad versiones de desarrollo de NVDA y
normalmente las instalas en tu ordenador, ahorrarás un montón de tiempo con
este complemento. Si prefieres probar las versiones de desarrollo en modo
portable y mantener tu copia instalada de NVDA sin cambios, este complemento
también es para ti.

## Modo de uso

Puedes cambiar el canal de actualización yendo al menú NVDA, Preferencias,
Opciones, categoría Canal de actualización. Una vez elijas el canal deseado
y pulses en Aceptar, espera a la próxima búsqueda automática de
actualizaciones o ve al menú ayuda de NVDA y elige la opción "Buscar
actualizaciones". Por ahora, estos son los canales disponibles:

* Predeterminado: este es el canal por defecto que utiliza tu versión de
  NVDA. Elegir esta opción es equivalente a deshabilitar el complemento.
* Estable: forzar canal de actualización a estable. Útil cuando quieres
  volver a una versión estable desde una versión de desarrollo.
* Estable, rc y beta: este es el canal de las versiones beta. Recibirás la
  primera versión beta una vez esta sea liberada. Este canal te permite
  actualizar pasando por betas y candidatas a liberación hasta que alcances
  la próxima versión estable.
* Alfa (versiones de desarrollo): elige esta opción para actualizar a la
  alfa más reciente. Las versiones de desarrollo alfa te permiten probar
  nuevas funciones, pero son bastante inestables. Por favor, ten cuidado.
* Deshabilitar actualizaciones (no recomendado): esta opción desactiva el
  canal de actualizaciones. Si buscas actualizaciones se mostrará un mensaje
  de error. Recuerda que puedes desactivar las actualizaciones automáticas
  desde la categoría de opciones generales. Usa esta opción sólo para hacer
  pruebas.

En cuanto se abra el panel de opciones, se recuperará en segundo plano
información sobre las actualizaciones disponibles en cada canal. Pulsa tab
para navegar a un cuadro de edición de sólo lectura, donde podrás ver esta
información. Esta información se actualizará dinámicamente cuando cambies el
canal de actualización en el cuadro combinado. Si hay una actualización
disponible en el canal seleccionado, aparecerán uno o dos enlaces al lado
del cuadro de edición:

* Descargar: pulsa la barra espaciadora sobre este enlace para abrirlo en tu
  navegador web y descargar el instalador más reciente.
* Ver registro de cambios: pulsa la barra espaciadora sobre este enlace para
  abrir el documento Qué hay de nuevo en tu navegador web. En algunos
  canales, este enlace no se mostrará.

## Registro de cambios

### Versión 1.4

* Traducciones actualizadas.
* Compatible con NVDA 2023.1.
* Por motivos de seguridad, la versión mínima de NVDA se ha establecido en
  2022.4.

### Versión 1.3

* Traducciones actualizadas.
* Corregido un problema que impedía crear copias portables de versiones
  alfa.

### Versión 1.2

* Traducciones actualizadas.
* Compatible con NVDA 2022.1.
* Por motivos de seguridad, la versión mínima de NVDA se ha establecido en
  2021.3.
* Solución para un fallo en el servidor de NV Access que provocaba que se
  ofreciera la versión 2019.2.1 al actualizar de alfa a estable.

### Versión 1.1

* Se han eliminado canales no soportados.
* Traducciones actualizadas.
* Se ha añadido información al panel de opciones sobre las actualizaciones
  disponibles actualmente.

### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=updateChannel
