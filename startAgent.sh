#!/bin/bash
rm log/*
java -cp lib/json-20080701.jar:lib/grinder.jar net.grinder.Grinder $1
