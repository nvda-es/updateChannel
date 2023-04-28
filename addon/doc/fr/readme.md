# Sélecteur du canal de mise à jour de NVDA #

* Auteur : Jose Manuel Delicado
* Compatibilité NVDA : 2022.4 et au-delà
* Télécharger [version stable][1]

Cette extension vous permet de télécharger et d'installer la dernière
version de NVDA du type choisi sans visiter une page Web ni utiliser votre
navigateur Web. Elle est utile lorsque, par exemple, vous souhaitez essayer
de nouvelles fonctionnalités dans une version de développement, puis
retourner  à la version stable la plus récente. Si vous testez régulièrement
des versions de développement de NVDA en les installant normalement sur
votre ordinateur, vous économiserez beaucoup de temps avec cette
extension. Si vous préférez tester les versions de développement en mode
portable et conserver votre copie installée de NVDA sans modifications,
cette extension est également pour vous.

## Utilisation

Vous pouvez changer le canal de mise à jour en allant au menu NVDA,
Préférences, Paramètres, catégorie Canal de mise à jour. Une fois que vous
avez choisi le canal souhaité et appuyez sur OK, attendez la prochaine
recherche de mise à jour automatique ou accédez au menu Aide de NVDA et
choisissez l'option "Rechercher une mise à jour". Pour l'instant, voici les
canaux disponibles :

* Défaut : Ceci est le canal par défaut utilisé par votre version de
  NVDA. Choisir cette option équivaut à désactiver l'extension.
* Stable : Force le canal de mise à jour à Stable. Utile lorsque vous
  souhaitez revenir à une version stable à partir d'une version de
  développement.
* Stable, rc et bêta : Ceci est le canal des versions bêta. Vous recevrez la
  première version bêta une fois qu'elle sera publiée. Ce canal vous permet
  de mettre à jour en passant  par bêta et release candidate jusqu'à ce que
  vous atteigniez la prochaine version stable.
* Alpha (versions de développement) : Choisissez cette option pour mettre à
  jour à l'alpha plus récente. Les versions de développement alpha vous
  permettent d'essayer de nouvelles fonctionnalités, mais elles sont assez
  instables. S'il vous plaît soyez prudent.
* Désactiver les mises à jour (non recommandé) : Cette option désactive le
  canal de mises à jour. Si vous recherchez des mises à jour, un message
  d'erreur s'affiche. N'oubliez pas que vous pouvez désactiver les mises à
  jour automatiques à partir de la catégorie Général du dialogue
  Paramètres. Utilisez cette option juste pour faire des tests.

Dès que le panneau  Paramètres, est ouvert, des informations sur les mises à
jour disponibles sur chaque canal seront récupérées en arrière-plan. Appuyez
sur Tab pour accéder à une zone d'édition en lecture seule, où vous pouvez
voir ces informations. Ces informations seront mises à jour de manière
dynamique lorsque vous modifiez le canal de mise à jour dans la liste
déroulante. S'il y a une mise à jour disponible sur le canal sélectionné, un
ou deux liens apparaîtront à côté de la zone d'édition:

* Télécharger: Appuyez sur la barre d'espace sur ce lien pour l'ouvrir dans
  votre navigateur Web et téléchargez l'installateur le plus récent.
* Voir journal des changements: Appuyez sur la barre d'espace sur ce lien
  pour ouvrir la documentation Quoi de Neuf dans votre navigateur Web. Dans
  certains canaux, ce lien ne sera pas affiché.

## Journal des changements

### Version 1.4

* Traductions mis à jour.
* Compatible avec NVDA 2023.1.
* Pour des raisons de sécurité, la version minimale de NVDA est définie sur
  2022.4.

### Version 1.3

* Traductions mis à jour.
* Correction d'un bug qui a empêché la création des copies portables à
  partir des versions alpha en développement.

### Version 1.2

* Traductions mis à jour.
* Compatible avec NVDA 2022.1.
* Pour des raisons de sécurité, la version minimale de NVDA est définie sur
  2021.3.
* Solution pour un bogue dans le serveur NV Access  qui a provoqué la
  version 2019.2.2.1 lors de la mise à jour de la version alpha vers la
  stable.

### Version 1.1

* Les canaux non supportés ont été supprimés.
* Traductions mis à jour.
* Les informations ont été ajoutées au panneau Paramètres sur les mises à
  jour actuellement disponibles.

### Version 1.0

* Version initiale.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=updateChannel
