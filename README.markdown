Materiale til workshop om enkel ytelsestesting med [Grinder](http://grinder.sourceforge.net), med fokus på testing av websider/applikasjoner.

TODO: mer info om workshoppen.

# Oppgaver

## Oppgave 1 - Enkel testing over HTTP

I den første oppgaven skal du skrive en Grinder-test som måler responstiden mot en enkelt URL over HTTP.

For å hjelpe deg i gang har vi laget litt kode du kan ta utgangspunkt i.
Vi har laget en ferdig properties-fil `tests/1.properties` som inneholder testkonfigurasjonen.
Denne peker på testscriptet `tests/scripts/test1.py` som du må gjøre ferdig selv.

For å kjøre testen kan du bruke `startAgent` scriptet som følger

    ./startAgent.sh tests/1
   
TODO: mer om hva som må gjøres her.

## Oppgave 2 - Testing av mange URLer

Akkurat som i oppgave 1 har vi gjort klart properties-fila `tests/1.properties` og et skall for scriptet `tests/scripts/task2.py`.
Det er i tillegg en fil `tests/scripts/urls.txt` som inneholder en rekke URLer.
Det er disse oppgaven går ut på å teste.

Oppgaven går ut på å lage en test som leser inn URL-ene fra fil og deretter tester hver enkelt hver gang scriptet kjøres.

TODO: mer om oppgaven.

Ekstrapoeng: Spesifiser filstien til URL-fila fra properties-fila slik at denne enkelt kan konfigureres utenfor koden.

## Oppgave 3 - Sjekking av responsene

TODO: beskrive oppgave.

