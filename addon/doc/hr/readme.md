# Selektor kanala za aktualiziranje NVDA čitača (NVDAUpdate Channel Selector #

* Autor: Jose Manuel Delicado
* NVDA kompatibilnost: 2019.1 do 2021.1
* Preuzmi [stabilnu verziju][1]

Ovaj dodatak omogućuje preuzimanje i instaliranje najnovije verzije NVDA
čitača odabrane vrste bez posjećivanja bilo koje web stranice te bez
korištenja web preglednika. Korisno je za testiranje novih funkcija
međuizdanja NVDA čitača, uz mogućnost vraćanja na najnovije stabilno
izdanje. Ako redovito testiraš NVDA međuizdanja i ako ih obično instaliraš
na računalo, uštedjet ćeš puno vremena s ovim dodatkom. Ako više voliš
testirati međuizdanja u prijenosnom načinu, čuvajući nepromijenjenu
instaliranu kopiju NVDA čitača, ovaj dodatak je i za tebe.

## Upotreba

Kanal za aktualiziranje NVDA čitača možeš promijeniti putem NVDA izbornika,
Postavke, Postavke, Ažuriranje kategorije kanala. Nakon što odabereš željeni
kanal i pritisneš „U redu”, pričekaj do sljedeće automatske provjere
aktualiziranja ili idi na izbornik NVDA pomoći i odaberi opciju „Provjeri
ažuriranja”. Za sada su ovo dostupni kanali:

* Standarno: ovo je standardni kanal koji koristi tvoja NVDA
  verzija. Biranje ove opcije znači isto kao i deaktiviranje dodatka.
* Stabilno: prisili kanal aktuliziranja na stabilnu verziju. Korisno kad se
  iz međuizdanja želiš vratiti na stabilnu verziju.
* Stabilno, kandidat izdanja i beta izdanje: ovo je kanal za beta
  izdanja. Dobit ćeš prvu beta verziju kad se objavi. Ovaj kanal omogućuje
  aktualiziranje putem beta izdanja i kandidata izdanja sve do sljedeće
  stabilne verzije.
* Alfa (međuizdanja): odaberi ovu opciju za aktualiziranje na najnoviju alfa
  verziju. Alfa međuizdanja omogućuju testiranje novih funkcija, ali su
  prilično nestabilne verzije, stoga ih koristi s oprezom.
* Deaktiviraj aktualiziranja (ne preporučuje se): ova opcija deaktivira
  kanal za aktualiziranje. Ako tražiš nove verzije, prikazat će se poruka o
  pogrešci. Automatsko aktualiziranje možeš deaktivirati u postavakama, pod
  kategorijeom „Opće”. Koristi ovu opciju samo u svrhu testiranja.

Information about available updates for each channel will be retrieved in
the background once the settings panel is opened. Press tab to navigate to a
read only edit field, where you can see this information. This information
will be dynamically updated when you change the update channel from the
combo box. If there is an update available for the selected channel, one or
two links will appear next to the edit field:

* Download: press spacebar on this link to open it in your web browser and
  download the latest installer.
* View changelog: press spacebar on this link to open the What's new
  document in your web browser. For some channels, this link won't be
  displayed.

## Zapis promjena

### Version 1.1

* Removed unsupported channels.
* Updated translations.
* Added information of currently available updates to the settings panel.

### Verzija 1.0

* Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=updchannelselect
