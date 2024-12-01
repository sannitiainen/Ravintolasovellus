**Ravintolasovellus**

Sovelluksessa näkyy tietyn alueen ravintolat, joista voi etsiä tietoa ja lukea arvioita. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi antaa arvion (tähdet ja kommentti) ravintolasta ja lukea muiden antamia arvioita.
- Ylläpitäjä voi lisätä ja poistaa ravintoloita sekä määrittää ravintolasta näytettävät tiedot.
- Käyttäjä voi etsiä kaikki ravintolat, joiden kuvauksessa on annettu sana.
- Käyttäjä näkee myös listan, jossa ravintolat on järjestetty parhaimmasta huonoimpaan arvioiden mukaisesti.
- Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion.
- Ylläpitäjä voi luoda ryhmiä, joihin ravintoloita voi luokitella. Ravintola voi kuulua yhteen tai useampaan ryhmään.

Tilanne 1.12.
- Joitain toimintoja puutuu vielä esim. kommentin poisto ja ylläpitäjän mahdollisuus määrittää mitkä tiedot ravintolasta näytetään
- Tietokantoja on kuusi, joista yhtä ei vielä käytetä, mutta sitä tullaan käyttmään lopullisessa versiossa
- Pääosin toiminnot ovat kunnossa ja toimivat, vaativat ehkä pientä hiontaa
- Ulkoasu on melko alkeellinen, sitä pitää vielä hioa


Testausohjeet

Aluksi kloonaa repositorio

    git clone https://github.com/sannitiainen/Ravintolasovellus.git

Avaa kohdekansio Ravintolasovellus ja kansio sovellus

    cd Ravintolasovellus
    cd sovellus

Rakenna virtuaaliympäristö

    python3 -m venv venv

Asenna esivaatimukset

    pip install -r requirements.txt

Avaa virtuaaliympäristö

    source venv/bin/activate

Avaa uusi terminaali-ikkuna ja käynnistä tietokanta

    start-pg.sh

Avaa uusi terminaali-ikkuna ja käynnistä Postgresql siellä

    psql

Luo uusi tietokanta

    CREATE DATABASE <tietokannan-nimi>;

Voit sulkea psql-terminaalin

Määritä tietokantaskeema virtuaaliympäristössä sovellus-kansiossa

    psql -d <tietokannan-nimi> < schema.sql

Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

    DATABASE_URL=<tietokannan-paikallinen-osoite>
    SECRET_KEY=<salainen-avain>

<tietokannan-paikallinen-osoite>: Määritä tietokannan osoite projektille siten, että osoite päättyy luomasi tietokannan nimeen. Esimerkiksi, jos omalla sovelluksellasi osoite on muotoa postgresql:///user ja loit vertaisarviontia varten tietokannan nimeltä testi, tulisi uudeksi tietokannan osoitteeksi postgresql:///testi.
<salainen-avain> Määritä itse jokin numerosarja

Käynnistä uuteen ikkunaan paikallinen sovellus

    flask run
