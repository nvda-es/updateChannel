# NVDAUpdate Channel Selector #

* Autor: Jose Manuel Delicado
* Compatibilidade con NVDA: 2021.3 en diante
* Descargar [versión estable][1]

Este complemento permíteche descargar e instalar a última versión de NVDA do
tipo escollido sen visitar ningunha páxina web nin usar o teu navegador
web. É útil cando, por exemplo, precisas probar novas características nunha
versión de desenvolvemento de NVDA e logo volver á publicación estable máis
recente. Se probas regularmente versións de desenvolvemento de NVDA e
adoitas instalalas no teu ordenador, aforrarás unha chea de tempo con este
complemento. Se prefires probar as versións de desenvolvemento en modo
portable mantendo a túa copia instalada de NVDA sen cambios, este
complemento tamén é para ti.

## Uso

Podes cambiar a canle de actualización de NVDA indo ó menú de NVDA,
Preferencias, Opcións,  categoría Update channel. Unha vez escollas a canle
desexada e premas Aceptar, agarda á próxima verificación automática de
actualizacións ou vai ó menú e escolle a opción "Procurar
actualización...". Polo de agora, estas son as canles dispoñibles:

* Default (predeterminada): ésta é a canle por defecto utilizada pola túa
  versión de NVDA. Elixir esta opción é o mesmo que desactivar o
  complemento.
* Stable (estable): forzar o canle de actualización a estable. Útil cando
  queiras volver a unha versión estable dende unha versión de
  desenvolvemento.
* Stable, rc and beta (estable, rc e beta): ésta é a canle das versións
  beta. Recibirás a primeira versión beta unha vez se publique. Esta canle
  permíteche actualizar ás betas e candidatas a publicación ata chegar á
  próxima versión estable.
* Alpha (alfa, versións de desenvolvemento): escolle esta opción para
  actualizar á última alfa. As versións de desenvolvemento alfa permítenche
  probar novas características, pero son algo inestables. Por favor, sé
  coidadoso.
* Disable updates (desactivar actualizacións, non recomendada): esta opción
  desactiva a canle de actualización. Se buscas actualizacións amosarase
  unha mensaxe de erro. Lembra que podes desactivar as actualizacións
  automáticas dende a categoría xeral das opcións. Utiliza esta opción só
  con fins de proba.

Obterase información sobre as actualizacións dispoñibles para cada canle en
segundo plano cando se abra o panel de opcións. Preme tab para navegar a
unha caixa de edición de só lectura, onde poderás ver esta información. Esta
información actualizarase dinamicamente cando cambies o canle de
actualización na caixa combinada. Se hai unha actualización dispoñible para
a canle seleccionada, aparecerán unha ou dúas ligazóns a continuación da
caixa de edición:

* Download (Descargar): preme a barra espaciadora nesta ligazón para abrilo
  no teu navegador web e descargar o último instalador.
* View changelog (Ver rexistro de trocos): preme a barra espaciadora nesta
  ligazón para o documento de Que hai de novo no teu navegador web. Para
  algúns canais, esta ligazón non se amosará.

## Rexistro de trocos

### Versión 1.2

* Traducións actualizadas.
* Compatible con NVDA 2022.1.
* Por razóns de seguridade, a versión mínima de NVDA establécese na 2021.3.
* Parche para un erro no servidor de NV Access que causaba que se ofrecese a
  versión 2019.2.1 ó actualizar dende alfa a estable.

### Versión 1.1

* Eliminados canais sen soporte.
* Traducións actualizadas.
* Engadida a información de actualizacións actualmente dispoñibles ó panel
  de opcións.

### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=updchannelselect
