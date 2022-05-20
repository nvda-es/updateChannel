# NVDA-päivityskanavan valitsin #

* Tekijä: Jose Manuel Delicado
* Yhteensopivuus: NVDA 2021.3 ja uudemmat
* Lataa [vakaa versio][1]

Tämän lisäosan avulla voit ladata ja asentaa valitsemaasi tyyppiä olevan
viimeisimmän NVDA-version ilman vierailua millään verkkosivulla tai
käyttämättä verkkoselainta. Tästä on hyötyä esim. kun haluat kokeilla NVDA:n
kehitysversion uusia ominaisuuksia ja palata sitten takaisin uusimpaan
vakaaseen versioon. Jos kokeilet säännöllisesti kehitysversioita asentamalla
ne tietokoneellesi, säästät tällä lisäosalla paljon aikaa. Mikäli kokeilet
kehitysversioita mieluummin massamuistitilassa säilyttäen asennetun
NVDA-versiosi muuttumattomana, tämä lisäosa on myös sinua varten.

## Käyttö

Voit vaihtaa NVDA:n päivityskanavaa menemällä NVDA-valikkoon, Valitsemalla
Asetukset / Asetukset / Päivityskanava-kategoria. Kun olet valinnut
haluamasi kanavan, paina OK, odota seuraavaa automaattista
päivitystarkistusta tai mene NVDA:n Ohje-valikkoon ja valitse "Tarkista
päivitykset" -vaihtoehto. Tällä hetkellä ovat käytettävissä seuraavat
kanavat:

* Oletus: tämä on NVDA-versiosi käyttämä oletuskanava. Tämän vaihtoehdon
  valitseminen  tarkoittaa samaa kuin tämän lisäosan käytöstä poistaminen.
* Vakaa: pakota päivityskanavaksi vakaa. Hyödyllistä, kun haluat palata
  kehitysversiosta vakaaseen versioon.
* Vakaa, rc ja beeta: tämä on beetaversioiden kanava. Saat ensimmäisen
  beetaversion heti, kun se julkaistaan. Tämän kanavan avulla voit päivittää
  beetaversioista RC-versioihinn ja aina seuraavaan vakaaseen versioon asti.
* Alfa (kehitysversiot): päivitä viimeisimpään alfaversioon valitsemalla
  tämä vaihtoehto. Alfa-kehitysversiot mahdollistavat uusien ominaisuuksien
  testaamisen, mutta ne saattavat olla melko epävakaita. Ole varovainen.
* Poista päivitykset käytöstä (ei suositella): tämä vaihtoehto poistaa
  päivityskanavan käytöstä. Jos yrität tarkistaa päivityksiä, sen
  epäonnistumisesta näytetään virheilmoitus. Muista, että voit poistaa
  automaattiset päivitykset käytöstä asetusten Yleiset-kategoriasta. Käytä
  tätä vaihtoehtoa vain testaustarkoituksiin.

Tiedot jokaisen kanavan saatavilla olevista päivityksistä haetaan taustalla,
kun asetuspaneeli on avattu. Paina Sarkainta siirtyäksesi vain luku
-tyyppiseen muokkauskenttään, jossa tiedot näytetään. Tiedot päivitetään
dynaamisesti vaihtaessasi päivityskanavaa yhdistelmäruudusta. Mikäli
valitulle kanavalle on saatavilla päivitys, muokkauskentän viereen ilmestyy
yksi tai kaksi linkkiä:

* Lataa: avaa tämä linkki verkkoselaimessa ja lataa viimeisin asennusohjelma
  painamalla sen kohdalla Väli-näppäintä.
* Näytä muutosloki: avaa Mitä uutta -dokumentti verkkoselaimessa painamalla
  tämän linkin kohdalla Väli-näppäintä. Tätä ei näytetä joissakin kanavissa.

## Muutosloki

### Versio 1.2

* Käännöksiä päivitetty.
* Yhteensopiva NVDA 2022.1:n kanssa.
* Turvallisuussyistä NVDA:n vähimmäisversioksi on asetettu 2021.3.
* Ratkaisu NV Accessin palvelimen virheeseen, joka aiheutti version 2019.2.1
  tarjoamisen päivitettäessä alfasta vakaaseen.

### Versio 1.1

* Ei-tuetut kanavat poistettu
* Käännöksiä päivitetty.
* Asetuspaneeliin lisätty tieto saatavilla olevista päivityksistä.

### Versio 1.0

* Initial version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=updchannelselect
