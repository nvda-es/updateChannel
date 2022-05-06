# Update-Kanal #

* Autor: José Manuel Delicado
* NVDA compatibility: 2021.3 and beyond
* [Stabile Version herunterladen][1]

Mit dieser Erweiterung können Sie die neueste NVDA-Version des ausgewählten
Typs herunterladen und installieren, ohne eine Webseite besuchen oder Ihren
Webbrowser verwenden zu müssen. Dies ist nützlich, wenn Sie beispielsweise
neue Funktionen in einem NVDA-Snapshot testen und dann zur neuesten stabilen
Version zurückkehren möchten. Wenn Sie regelmäßig NVDA-Snapshots testen und
diese in der Regel auf Ihrem Computer installieren, sparen Sie mit dieser
Erweiterung viel Zeit. Wenn Sie es vorziehen, Snapshots im portablen Modus
zu testen und Ihre installierte Version von NVDA unverändert zu lassen, ist
diese Erweiterung ebenfalls für Sie geeignet.

## Verwendungszweck

Sie können den Kanal für die NVDA-Aktualisierungen ändern, indem Sie im
NVDA-Menü, Optionen, Einstellungen, Kategorie "update-Kanal" gehen. Nachdem
Sie den gewünschten Kanal ausgewählt und auf "OK" geklickt haben, warten Sie
bis zur nächsten automatischen Update-Prüfung oder im NVDA-Menü, Hilfe und
wählen Sie die Option "Nach Updates suchen" aus. Im Moment sind dies die
verfügbaren Kanäle:

* Standard: Dies ist der Standardkanal, der von Ihrer NVDA-Version verwendet
  wird. Die Auswahl dieser Option bedeutet dasselbe wie das Deaktivieren der
  Erweiterung.
* Stabil: Aktualisierungskanal auf stabil erzwingen. Nützlich, wenn Sie von
  einem Snapshot zu einer stabilen Version zurückkehren möchten.
* Stable, RC und Beta: Dies ist der Kanal für Beta-Releases. Sie erhalten
  die erste Beta-Version, sobald sie veröffentlicht wird. Über diesen Kanal
  können Sie über Betas und Release-Kandidaten aktualisieren, bis Sie die
  nächste stabile Version erreichen.
* Alpha (Snapshots): Wählen Sie diese Option aus, um auf die neueste Alpha
  zu aktualisieren. Alpha-Snapshots ermöglichen es Ihnen, neue Funktionen zu
  testen, aber sie sind ziemlich instabil. Seien Sie bitte vorsichtig.
* Updates deaktivieren (nicht empfohlen): Diese Option deaktiviert den
  Update-Kanal. Wenn Sie nach Updates suchen, wird eine Fehlermeldung
  angezeigt. Denken Sie daran, dass Sie automatische Updates in den
  Einstellungen in der Kategorie Allgemein deaktivieren können. Verwenden
  Sie diese Option nur zu Testzwecken.

Informationen zu verfügbaren Updates für jeden Kanal werden im Hintergrund
abgerufen, sobald das Einstellungsfenster geöffnet wird. Drücken Sie die
Tabulatortaste, um zu einem schreibgeschützten Bearbeitungsfeld zu
navigieren, in dem Sie diese Informationen sehen können. Sie werden
dynamisch aktualisiert, wenn Sie den Aktualisierungskanal über das
Kombinationsfeld ändern. Wenn für den ausgewählten Kanal ein Update
verfügbar ist, werden neben dem Bearbeitungsfeld ein oder zwei Links dazu
angezeigt:

* Download: Drücken Sie die Leertaste auf diesem Link, um ihn im Web-Browser
  zu öffnen und das neueste Setup herunterzuladen.
* Änderungsprotokoll anzeigen: Drücken Sie die Leertaste auf diesem Link, um
  das Dokument "Neuigkeiten" im Web-Browser zu öffnen. Bei einigen Kanälen
  wird dieser Link nicht angezeigt.

## Änderungsprotokoll

### Version 1.2

* Aktualisierte Übersetzungen.
* Compatible with NVDA 2022.1.
* For security reasons, minimum NVDA version is set to 2021.3.
* Workaround for a bug in the NV Access server which caused version 2019.2.1
  to be offered when updating from alpha to stable.

### Version 1.1

* Nicht unterstützte Kanäle entfernt.
* Aktualisierte Übersetzungen.
* Informationen zu derzeit verfügbaren Updates zum Einstellungsfeld
  hinzugefügt.

### Version 1.0

* Erste Version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=updchannelselect
