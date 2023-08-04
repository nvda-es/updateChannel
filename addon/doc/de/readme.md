# Update-Kanal-Auswahl #

* Autor: José Manuel Delicado
* NVDA-Kompatibilität: 2022.4 und neuer
* [Stabile Version herunterladen][1]

Mit dieser NVDA-Erweiterung können Sie die neueste NVDA-Version des
ausgewählten Typs herunterladen und installieren, ohne einen Web-Browser zu
benutzen. Dies ist nützlich, wenn Sie beispielsweise neue Funktionen in
einem NVDA-Snapshot testen und dann zur neuesten stabilen Version
zurückkehren möchten. Wenn Sie regelmäßig NVDA-Snapshots testen und diese in
der Regel auf Ihrem Computer installieren, sparen Sie mit dieser
NVDA-Erweiterung viel Zeit. Wenn Sie es vorziehen, Snapshots als portable
Version zu testen und die installierte NVDA-Version unverändert zu lassen,
ist diese NVDA-Erweiterung ebenfalls für Sie geeignet.

## Verwendung

Sie können den Kanal für die NVDA-Updates ändern, in dem Sie über das
NVDA-Menü, Optionen, Einstellungen, Kategorie "Update-Kanal-Auswahl"
gehen. Nach dem Sie den gewünschten Kanal ausgewählt und auf "OK" geklickt
haben, warten Sie bis zur nächsten automatischen Update-Prüfung oder im
NVDA-Menü, Hilfe und wählen Sie die Option "Nach Updates suchen" aus. Im
Moment sind dies die verfügbaren Kanäle:

* Standard: Dies ist der Standardkanal, der von der aktuellen NVDA-Version
  verwendet wird. Die Auswahl dieser Option bedeutet dasselbe wie das
  Deaktivieren der NVDA-Erweiterung.
* Stabil: Aktualisierungskanal auf stabil erzwingen. Nützlich, wenn Sie von
  einem Snapshot zu einer stabilen Version zurückkehren möchten.
* Stable, RC und Beta: Dies ist der Kanal für Beta-Releases. Sie erhalten
  die erste Beta-Version, sobald sie veröffentlicht wird. Über diesen Kanal
  können Sie über Betas und Release-Kandidaten aktualisieren, bis Sie die
  nächste stabile Version erreichen.
* Alpha (Snapshots): Wählen Sie diese Option aus, um auf die neueste Alpha
  zu aktualisieren. Mit den Alpha-Snapshots können Sie neue Funktionen
  ausprobieren, aber sie können noch ziemlich instabil sein; daher auf
  eigene Gefahr.
* Updates deaktivieren (nicht empfohlen): Diese Option deaktiviert den
  Update-Kanal. Wenn Sie nach Updates suchen, wird eine Fehlermeldung
  angezeigt. Denken Sie daran, dass Sie automatische Updates in den
  Einstellungen in der Kategorie Allgemein deaktivieren können. Verwenden
  Sie diese Option nur zu Testzwecken.

Informationen zu verfügbaren Updates für jeden Kanal werden im Hintergrund
abgerufen, sobald das Einstellungsfenster geöffnet wird. Drücken Sie die
Tabulatortaste, um zu einem schreibgeschützten Bearbeitungsfeld zu
navigieren, in dem Sie diese Informationen sehen können. Sie werden
dynamisch aktualisiert, wenn Sie den Update-Kanal über das Kombinationsfeld
ändern. Ist für den ausgewählten Kanal ein Update verfügbar, werden neben
dem Bearbeitungsfeld ein oder zwei Links dazu angezeigt:

* Download: Betätigen Sie die Leertaste auf diesem Link, um die neueste
  Setup-Datei im Web-Browser zu öffnen und sie herunterzuladen.
* Änderungsprotokoll anzeigen: Betätigen Sie die Leertaste auf diesem Link,
  um das Dokument im Web-Browser zu öffnen. Bei einigen Kanälen wird dieser
  Link nicht angezeigt.

## Änderungsprotokoll

### Version 1.4

* Aktualisierte Übersetzungen.
* Kompatibel mit NVDA 2023.1.
* Aus Sicherheitsgründen ist die Mindestversion von NVDA auf 2022.4
  festgelegt.

### Version 1.3

* Aktualisierte Übersetzungen.
* Es wurde ein Fehler behoben, der die Erstellung portabler Versionen von
  Alpha-Schnappschüssen verhinderte.

### Version 1.2

* Aktualisierte Übersetzungen.
* Kompatibel mit NVDA 2022.1.
* Aus Sicherheitsgründen wurde die Mindestanforderung der NVDA-Version auf
  2021.3 festgelegt.
* Workaround für einen Fehler im Server bei NV Access, der dazu führte, dass
  beim Update von Alpha auf Stable die Version 2019.2.1 angeboten wurde.

### Version 1.1

* Nicht unterstützte Kanäle entfernt.
* Aktualisierte Übersetzungen.
* Informationen zu derzeit verfügbaren Updates zum Einstellungsfeld
  hinzugefügt.

### Version 1.0

* Erste Version.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=updateChannel
