@ECHO off
del log\*
java -cp lib\jython.jar;lib\json-20080701.jar;lib\grinder.jar net.grinder.Grinder scenario\%1.properties
