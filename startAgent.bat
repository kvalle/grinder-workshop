@ECHO off
del log\*
java -cp lib\jython-2.5.2.jar;lib\json-20080701.jar;lib\grinder.jar net.grinder.Grinder %1
