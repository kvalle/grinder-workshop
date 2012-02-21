Materiale til workshop om enkel ytelsestesting med [Grinder](http://grinder.sourceforge.net), med fokus på testing av websider/applikasjoner.

TODO: mer info om workshoppen.

# Forberedelser

For å spare tid vil det være fint om alle kan gjøre noen forberedelser før workshoppen begynner.
Vi kan da begynne rett på arbeidet med oppgavene, uten å måtte installere og sette opp Grinder først.

Det du trenger å gjøre er:

- Installer [git](http://git-scm.com/download)
- Sjekk ut dette repositoriet:
  `git clone git://github.com/kvalle/grinder-workshop.git`
- Sjekke at alt fungerer ved å kjøre eksempel-testen (når du står i mappen `grinder-workshop`):
  `./startAgent.sh demo/demo`
  
(Hvis du ikke ønsker å installere `git` går det også an å laste ned [koden som zip-fil](https://github.com/kvalle/grinder-workshop/zipball/master).)
  
Når du kjører eksempelet vil Grinder skrive ut en del informasjon.
Denne er ikke så nøye enda, det viktigste er å se at omtrent det følgende blir skrevet ut til sist:

        TODO: lag egnet script og lim inn forventet output her

# Oppgaver

Oppgavene er beskrevet under.
Det går fint an å løse oppgavene på egenhånd, men vi anbefaler å sitte to og to sammen.

Vi starter svært enkelt med å måle responstid for GET over HTTP med én enkelt URL.
Oppgavene blir gradvis vanskeligere, og vi vil komme innom blant annet sjekking av responser, generering av script ved hjelp av HTTPProxy, og testing av REST-API.

Siden dette er en workshop om Grinder og ikke Python, gir vi for hver oppgave tips om funksjoner det kan være greit å vite om.
Vi er også tilgjengelige under hele workshoppen, så ikke nøl med å spørre om hjelp.

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
Pass på å få laget en `Test` for hver URL slik at responstidene måles individuelt.

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

I oppgave 3 er det ikke laget noen kode å ta utgangspunkt i -- i stedet bygger vi videre på løsningen fra oppgave 2.
Dersom du ikke ferdig med forrige oppgave, men likevel har lyst til å begynne med denne, kan du sjekke løsningsforslaget i `solutions/2.properties` og `solutions/scripts/task2.py`.

Oppgaven går ut på å få testene til å se nærmere på responsene vi får tilbake.
Så langt har vi gjort GET requests mot de forskjellige URL-ene, og registrert alle forepørsler som har gitt svar som suksesser.
Du skal nå legge på noen respons-sjekker som feiler tester dersom vi ikke får tilbake det vi forventer.

Du velger selv hva du ønsker å teste.
(Her er det bare fantasien som setter begrensninger!)
Noen forslag til ting som kan testes på en enkel måte er

- at HTTP statuskode er 200
- at responsen har en viss minimum størrelse (i linjer eller byte)
- at responsen (ikke) inneholder en gitt tekst

### Ekstraoppgave:

Hvis oppgaven blir enkel kan du utvide med å lage respons-sjekker spesielt tilpasset hver enkelt request.
Dette kan for eksempel løses ved å legge mer informasjon sammen med URL-ene i filen som leses, og bruke denne til å avgjøre hva som skal testes for hver URL.


## Oppgave 4 - Bruk av HTTPProxy for å lage tester

Noen ganger ønsker man å teste en typisk brukerøkt.
Man kan da bruke Grinders `HTTPProxy` til å følge med på hva man gjør i nettleseren, og automatisk generere utkast til et script på bakgrunn av dette.

I denne oppgaven skal du generere et testscript med `HTTPProxy`.

TODO: mer om oppgaven.


## Oppgave 5 (++) - Testing av REST-API

TODO: Espen
