Materiale til workshop om enkel ytelsestesting med [Grinder](http://grinder.sourceforge.net), med fokus på testing av websider/applikasjoner.

TODO: mer info om workshoppen.

# Oppgaver

Oppgavene er beskrevet under.
Vi starter svært enkelt med å måle responstid for GET over HTTP med én enkelt URL.
Oppgavene blir gradvis vanskeligere, og vi vil komme innom blant annet sjekking av responser, generering av script ved hjelp av HTTPProxy, og testing av REST-API.

Siden dette er en workshop om Grinder og ikke Python, gir vi for hver oppgave tips om funksjoner det kan være greit å vite om.

Løsningsforslag til alle oppgavene ligger under `solutions/`.


## Oppgave 1 - Enkel testing av responstid

I den første oppgaven skal du skrive en Grinder-test som måler responstiden mot en enkelt URL over HTTP.

For å hjelpe deg i gang har vi laget litt kode du kan ta utgangspunkt i.
Vi har laget en ferdig properties-fil `tests/1.properties` som inneholder testkonfigurasjonen.
Denne peker på testscriptet `tests/scripts/test1.py` som du må gjøre ferdig selv.

For å kjøre testen kan du bruke `startAgent` scriptet på følgende måte:

    ./startAgent.sh tests/1
   
Det er tre ting som må gjøres:

1. Opprett et `Test` med nummer og beskrivelse.
2. Wrap en `HTTPRequest` med testen.
3. Gjør en GET hver gang `__call__`-metoden blir kalt.


## Oppgave 2 - Testing av mange URLer om gangen

Akkurat som i oppgave 1 har vi gjort klart properties-fila `tests/1.properties` og et skall for scriptet i `tests/scripts/task2.py`.

Filen `tests/scripts/urls.txt` inneholder en rekke URL-er.
Oppgaven er ikke mye vanskeligere enn den forige, og går rett og slett ut på å lage et script som leser denne filen, og tester samtlige URL-er.

Testscriptet skal altså:

- Lese URL-ene fra filen.
- Lage tester for hver URL.
- GETe hver enkelt URL hver gang scriptet kjøres (altså, hver gang `__call__`-metoden i `TestRunner` blir kalt).

### Ekstraoppgave:

Blir du raskt ferdig må du gjerne prøve deg på følgende:

- Legg beskrivelser av hver test/URL sammen med URL-ene i `urls.txt`, og bruk disse når du oppretter `Test`-ene.
- I stedet for å wrappe `HTTPRequest` med testene slik vi gjorde i oppgave 1, opprett i stedet lambda-funksjoner for å kalle GET med hver enkelt URL.
  Disse kan i stedet wrappes av testene, slik du slipper å holde styr på listen av URL-er i `__call__` metoden.


## Oppgave 3 - Validering av responser

TODO: beskrive oppgave.


## Oppgave 4 - Bruk av HTTPProxy for å lage tester

Noen ganger ønsker man å teste en typisk brukerøkt.
Man kan da bruke Grinders `HTTPProxy` til å følge med på hva man gjør i nettleseren, og automatisk generere utkast til et script på bakgrunn av dette.

I denne oppgaven skal du generere et testscript med `HTTPProxy`.

TODO: mer om oppgaven.


## Oppgave 5 (++) - Testing av REST-API
