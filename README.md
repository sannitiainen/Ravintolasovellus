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

Avaa kohdekansio Ravintolasovellus (cd)
Avaa kansio sovellus

Rakenna virtuaaliympäristö

    python3 -m venv venv

Asenna esivaatimukset

    pip install -r requirements.txt

Avaa virtuaaliympäristö

    source venv/bin/activate

Avaa tietokanta uuteen terminaali-ikkunaan

    Start-pg.sh

Luo tietokanta ajamalla uudessa terminaali-ikkunassa

    schema.sql psql < schema.sql

Käynnistä uuteen ikkunaan paikallinen sovellus

    flask run --debug
