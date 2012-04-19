@ECHO off
del /Q proxy\proxygeneratedscript.py
java -cp lib\grinder.jar net.grinder.TCPProxy -console -http > proxy\proxygeneratedscript.py
