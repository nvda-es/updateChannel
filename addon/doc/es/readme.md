# Modificador del canal de actualización de NVDA

## Introducción

Este complemento te permite descargar e instalar la versión más reciente de NVDA del tipo elegido sin visitar ninguna página web ni usar tu navegador web. Es útil cuando, por ejemplo, quieres probar nuevas características que hay en una versión de desarrollo y después regresar a la versión estable más reciente. Si pruebas con regularidad versiones de desarrollo de NVDA y normalmente las instalas en tu ordenador, ahorrarás un montón de tiempo con este complemento. Si prefieres probar las versiones de desarrollo en modo portable y mantener tu copia instalada de NVDA sin cambios, visita la [página de descarga de versiones de desarrollo de NVDA](https://www.nvaccess.org/files/nvda/snapshots/).

## Modo de uso

Puedes cambiar el canal de actualización yendo al menú NVDA, Preferencias, Opciones, categoría Canal de actualización. Una vez elijas el canal deseado y pulses en Aceptar, espera a la próxima búsqueda automática de actualizaciones o ve al menú ayuda de NVDA y elige la opción "Buscar actualizaciones". Por ahora, estos son los canales disponibles:

* Predeterminado: este es el canal por defecto que utiliza tu versión de NVDA. Elegir esta opción es equivalente a deshabilitar el complemento.
* Estable: forzar canal de actualización a estable. Útil cuando quieres volver a una versión estable desde una versión de desarrollo.
* Estable, rc y beta: este es el canal de las versiones beta. Recibirás la primera versión beta una vez esta sea liberada. Este canal te permite actualizar pasando por betas y candidatas a liberación hasta que alcances la próxima versión estable.
* Alfa (versiones de desarrollo): elige esta opción para actualizar a la alfa más reciente. Las versiones de desarrollo alfa te permiten probar nuevas funciones, pero son bastante inestables. Por favor, ten cuidado.
* Beta (versiones de desarrollo): elige esta opción para actualizar a la beta más reciente construida desde la rama beta. El código beta ha sido más probado que el alfa. Sin embargo, hasta que la versión oficial beta no sea liberada, puede no ser suficientemente estable para la mayoría de los usuarios.
* RC (versiones de desarrollo): elige esta opción para actualizar a la candidata a liberación más reciente construida desde la rama rc. El código rc ha sido más probado que el beta. Sin embargo, hasta que la versión oficial candidata a liberación no se publique, puede no ser suficientemente estable para la mayoría de los usuarios.
* Threshold (versiones de desarrollo): elige esta opción si quieres probar los trabajos de transición a Python 3, la refactorización del habla y muchas nuevas características.
* Threshold (trabajos de transición a Python 3) (versiones de desarrollo): elige esta opción si contribuyes con la transición de Python 2 a Python 3 y quieres probar los cambios.
* Deshabilitar actualizaciones (no recomendado): esta opción desactiva el canal de actualizaciones. Si buscas actualizaciones se mostrará un mensaje de error. Recuerda que puedes desactivar las actualizaciones automáticas desde la categoría de opciones generales.

Nota: algunos canales se han creado con propósitos de transición o pruebas específicas y podrían no recibir actualizaciones nunca más.

## Registro de cambios

### Versión 1.0

* Versión inicial.
