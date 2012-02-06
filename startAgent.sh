#!/bin/bash
rm log/*
java -cp lib/json-20080701.jar:lib/grinder.jar net.grinder.Grinder scenarier/$1.properties
