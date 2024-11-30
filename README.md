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


Testausohjeet

Aluksi kloonaa repositorio

    git clone https://github.com/sannitiainen/Ravintolasovellus.git

Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

    DATABASE_URL=<tietokannan-paikallinen-osoite>
    SECRET_KEY=<salainen-avain>

Avaa kohdekansio Ravintolasovellus ja kansio sovellus

    cd Ravintolasovellus
    cd sovellus

Rakenna virtuaaliympäristö

    python3 -m venv venv

Asenna esivaatimukset

    pip install -r requirements.txt

Avaa virtuaaliympäristö

    source venv/bin/activate

Avaa tietokanta uuteen terminaali-ikkunaan

    start-pg.sh

Avaa Postgresql uudessa terminaalissa

    psql

Luo uusi tietokanta

    CREATE DATABASE <tietokannan-nimi>;

Määritä tietokantaskeema

    psql -d <tietokannan-nimi> < schema.sql

Määritä vielä tietokannan osoite projektille siten, että osoite päättyy luomasi tietokannan nimeen. Esimerkiksi, jos omalla sovelluksellasi osoite on muotoa postgresql:///user ja loit vertaisarviontia varten tietokannan nimeltä testi, tulisi uudeksi tietokannan osoitteeksi postgresql:///testi.

Käynnistä uuteen ikkunaan paikallinen sovellus

    flask run
