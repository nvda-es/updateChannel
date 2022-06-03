# Selektor kanala za aktualiziranje NVDA čitača (NVDAUpdate Channel Selector #

* Autor: Jose Manuel Delicado
* NVDA kompatibilnost: 2021.3 i novije verzije
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

Informacije o dostupnim novim verzijama za svaki kanal dohvatit će se u
pozadini kad se otvori ploča s postavkama. Pritisni tabulator za kretanje do
polja za uređivanje koje je samo za čitanje, gdje možeš vidjeti ove
informacije. Ove informacije će se dinamički aktualizirati kad promijeniš
kanal aktualiziranja u odabirnom okviru. Ako je za odabrani kanal dostupna
nova verzija, jedna ili dvije poveznice će se pojaviti pored polja za
uređivanje:

* Preuzimanje: pritisni razmaknicu na ovoj poveznici za otvaranje poveznice
  u tvom web pregledniku i za preuzimanje najnovijeg instalacijskog
  programa.
* Pregledaj dnevnik promjena: pritisni razmaknicu na ovoj poveznici za
  otvaranje dokumenta „Što je novo” u web pregledniku. Za neke kanale ova se
  poveznica neće prikazati.

## Dnevnik promjena

### Verzija 1.2

* Aktualizirani prijevodi.
* Kompatibilno s NVDA čitačem 2022.1.
* Iz sigurnosnih razloga, minimalna NVDA verzija postavljena je na 2021.3.
* Zaobilazno rješenje za grešku na NV Access poslužitelju zbog kojeg se
  verzija 2019.2.1 nudi prilikom aktualiziranja s alfa verzije na stabilnu
  verziju.

### Verzija 1.1

* Uklonjeni su nepodržani kanali.
* Aktualizirani prijevodi.
* Dodane su informacije o trenutačno dostupnim novim verzijama u ploču
  postavki.

### Verzija 1.0

* Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=updchannelselect
