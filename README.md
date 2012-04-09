Materiale til workshop om enkel ytelsestesting med [Grinder](http://grinder.sourceforge.net), med fokus på testing av websider/applikasjoner.

[Slides here](http://kvalle.github.com/grinder-workshop/).

TODO: mer info om workshoppen.

# Forberedelser

TODO Espen: translate

For å spare tid vil det være fint om alle kan gjøre noen forberedelser før workshoppen begynner.
Vi kan da begynne rett på arbeidet med oppgavene, uten å måtte installere og sette opp Grinder først.

Det du trenger å gjøre er:

- Hvis nødvendig, installer [git](http://git-scm.com/download).
- Hvis nødvendig, installer [Java](http://java.com/en/download).
- Sjekk ut dette repositoriet.

    git clone git://github.com/kvalle/grinder-workshop.git

Når du er ferdig med å installere kan du sjekke at alt fungerer ved å kjøre eksempel-testen (når du står i mappen `grinder-workshop`):

    ./startAgent.sh example/scenario.properties
  
Når du kjører dette eksempelet vil Grinder skrive ut en del informasjon.
Først kommer det litt informasjon om hva som skjer under oppstarten, og muligens noen linjer med noe slikt som `*sys-package-mgr*: processing new jar`.
Ignorer dette for nå.

Deretter skriver selve eksempel-testene ut litt info mens de kjøres.
Dette bør se ut omtrent som følgende:

    > output #0 from worker thread 1
    > output #0 from worker thread 0
    > output #1 from worker thread 0
    > output #1 from worker thread 1
    > output #2 from worker thread 0
    ...

Når testen har kjørt ferdig kan du i tillegg sjekke at alt har gått riktig for seg ved å titte på resultatet som skal ha blitt lagret i den nyopprettede mappen `grinder-workshop/log`.
Her skal det ligge to filer med navn som `out_xyz-0.log` og `data_xyz-0.log`, der `xyz` er navnet på din datamaskin.
I `out`-filen finner du et sammendrag av testens resultater, og `data`-filen inneholder alle detaljene i et komma-separert format.
Hvis alt har gått bra skal det *ikke* være laget noen filer med navn som `error_xyz-0.log`!

*Hvis du av en eller annen grunn ikke kan installere git går det også an å laste ned [koden som zip-fil](https://github.com/kvalle/grinder-workshop/zipball/master).*

# Resources

TODO Espen: translate

Vi har forsøkt å forklare hva som skal gjøres i oppgavene så godt vi kan, men det dukker naturligvis alltid opp spørsmål.
I tilfelle vi ikke umiddelbart er tilgjengelige for å svare på disse, oppsummerer vi de viktigste stedene å finne informasjon under.

For informasjon om Grinder er [hjemmesiden](http://grinder.sourceforge.net/) et greit sted å starte.
Det nyttigste stedet å starte for å lage test-script er [script-galleriet](http://grinder.sourceforge.net/g3/script-gallery.html) som inneholder en rekke gode eksempler.
Det finnes også et [script API](http://grinder.sourceforge.net/g3/script-javadoc/index.html) med forklaringer på hvordan de forskjellige klassene og metodene fungerer.

Det første stedet å sjekke om du har spørsmål til selve språket er [Pythons offisielle dokumentasjonen](http://docs.python.org/index.html).
Her ligger veldig mye og god informasjon.
En god måte å finne frem til denne er via [søkesiden](http://docs.python.org/search.html).
For eventuelle spørsmål som går på samspillet mellom Python og Java er [hjemmesiden til Jython](http://www.jython.org/docs/index.html) stedet å starte.

# Tasks

The tasks are described below.
While you could perfectly well solve them by yourself, we reccomend that you work in pairs to get the most out of the workshop.
This way, it will also be easier for us to help everybody.

The tasks start easy, by first only measuring the request time for a single URL.
Through increasing difficulty, the tasks will then take us through testing multiple URLs, validating the responses, testing REST APIs, and utilizing Grinder's TCPProxy module to automatically generate test scripts.

Solutions to all tasks can be found in the `solutions/` folder.
Look at these if you wish, but only as a last resort if you are completely stuck and we are unable to help you!


## Task 1 - Testing GET Response Time

In this first task, we will be writing a test to GET a single URL and measure the response time.

We have prepared some of the code, to help you get started.
First, the test configuration is ready made in `tests/1.properties`.
This file points to the test script file, in `tests/scripts/test1.py`.
Here we have only provided the shell, which you must complete to make the test do anything useful.

To run the test, use the `startAgent` scriptet as follows.

    ./startAgent.sh tests/1.properties
   
(If you are doing this on Windows, substitute `.bat` for `.sh` and use `\` instead of `/`.)

In the test script, there are three things you need to do:

1. Create a `Test` with identification number (could be anything) and a description.
1. Wrap an instance of `HTTPRequest` with the test you just created.
1. Do a GET request every every time the test is run (i.e. from the `__call__`-method).
   You can GET any page you wish, just please be sure not to accidentally DOS-attack anybody.
   A rather harmless alternative is to get [http://grinder.espenhh.com/rocksolid.php](http://grinder.espenhh.com/rocksolid.php).

For how to do the actual GET request, have a look around the [script API](http://grinder.sourceforge.net/g3/script-javadoc/index.html).


## Task 2 - Testing multiple URLs

Just like in task 1, we have also here prepared the configuration in `tests/2.properties`, and a shell for you to get started scripting in `tests/scripts/task2.py`.

The file `tests/scripts/urls.txt` contains a number of URLs.
Your task is to write a scripts that reads this file, and then GETs each one in turn.
Make sure you use different `Test` objects for each URL, to make Grinder record their response times individually.

In short, your script should:

- Read the URLs from file.
- Create a `Test` for each URL. (Remember to wrap a `HTTPRequest`, like in the task 1.)
- GET all the URLs every time the test script is run.

A few Python methods/concepts that could prove useful: [enumerate](http://docs.python.org/library/functions.html#enumerate), [strip](http://docs.python.org/library/stdtypes.html#str.strip), [lists](http://docs.python.org/tutorial/datastructures.html), [open](http://docs.python.org/library/functions.html#open).

### Extra credits

If you complete the task quickly, try one or more of the following:

- Add descriptions to each URL in the `urls.txt` file, and use these when creating the `Test` objects.
- Instead of wrapping `HTTPRequest` with the tests like we did in task 1, try wrapping a [lambda](http://docs.python.org/tutorial/controlflow.html#lambda-forms) that does all the work (e.g. create a HTTPRequest and call `GET` with the correct URL).
  This way, you won't need to keep track of *both* test objects and their URLs in the `__call__` method.


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

For å styre hvorvidt Grinder skal gjenkjenne gjennomføringen av en test som velykket eller ikke bruker vi `grinder.statistics`.
Følgede kan være greie å kjenne til:

* `grinder.statistics.delayReports = 1`  
  Skrur av umiddelbar rapportering av resultater.
  Bruk denne i starten av scriptet slik at vi kan melde inn resultatene manuelt.
* `grinder.statistics.forLastTest.success = 0`  
  Merker testen som ble kjørt sist som feilet.
  Settes automatisk til 1 etter hver test.
* `grinder.statistics.report()`  
  Rapporter resultat for sist kjørte test.

### Ekstraoppgave:

Hvis oppgaven blir enkel kan du utvide med å lage respons-sjekker spesielt tilpasset hver enkelt request.
Dette kan for eksempel løses ved å legge mer informasjon sammen med URL-ene i filen som leses, og bruke denne til å avgjøre hva som skal testes for hver URL.


## Task 4 - Testing of a typical JSON-API (REST API)

Up until now, we have tested some pretty static pages. You (might have) parsed the response to do some basic content-check (e.g. to check whether some specific text are present, or if it's not). Now, it's time to do some more fancy parsing.

We'll be testing against an API which returns JSON. This JSON will contain links to further stuff you can test against. These links will change for each request, this means that we'll have to parse the JSON to fetch the links - we can't hard-core all the links in the script beforehand. This task will prepare you for testing real API's out there, either if they have real links or if they just have ID's you have to parse out and include in a predefined URL-template.

The easiest way to start is to do a manual call against the webpage: http://grinder.espenhh.com/json.php

Take a look at the JSON, and figure out what you want to test. It could be smart to run the JSON through a ["beautifier"](http://jsonformatter.curiousconcept.com/) to be better able to see the structure.

### How-to

Then, start writing the test. We'll give you complete freedom here, but to get you started you can do the following:

1. Start by writing a test that fetches http://grinder.espenhh.com/json.php and outputs the result to the console
2. Now, modify the test to parse the JSON.
3. To start simple, print out the fetched-field on the JSON
4. Now loop through all the tweets, and print out the tweets
5. Find the URL for each tweets profile picture, and do a GET against this URL

If you want to continue doing some JSON testing, you can try the real twitter API. And PLEASE: don't load-test this, just run with a single thread and a single run each time! Load-testing other people's servers without permission is BAD BEHAVIOUR ;)

Twitter: http://search.twitter.com/search.json?q=grinder (change "grinder" to whatever you want)


## Task 5 - Using Grinder's TCPProxy to automatically generate tests

Sometimes, you don't want to write all your tests by hand, you just want to simulate a user clicking through some pages in a browser. Grinder has support for this; by using the [Grinder TCPProxy](http://grinder.sourceforge.net/g3/tcpproxy.html) you can record a web-browsing-session and replay it using Grinder afterward. This technique will also generate a script which you can later modify (this is something you almost certainly would want to do!).

### How-to

Do the following tasks to record a simple web page:

1. Start the proxy server by running the script `./startProxy.sh` .. This will start a simple console that lets you input comments, and stop the proxy cleanly
2. Configure your browser to send traffic through the proxy (read more [here](http://grinder.sourceforge.net/g3/tcpproxy.html) )
3. Go to a simple web page (we recommend starting with http://grinder.espenhh.com/simple/ ). If you go to a complex page, the generated script will be crazy long
4. After the page have loaded in the browser, click "stop" in the simple console window
5. Inspect the script generated: it's located at `proxy/proxygeneratedscript.sh`
6. Try running the script: `./startAgent.sh proxy/proxygeneratedscript.sh`
7. Check the log, try modifying the script, experiment. You can start by removing all the sleep statements in the script. Then try it on a more complicated page. Have fun =)
