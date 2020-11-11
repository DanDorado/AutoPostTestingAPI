#!/bin/bash

# use nullglob in case there are no matching files
shopt -s nullglob

environments=(./PostmanEnvironments/*)
collections=(./TestCollections/*)

for environment in "${environments[@]}"
do
    for collection in "${collections[@]}"
    do
        newman run $collection --global-var TargetTime="200" -e $environment -r cli,junit --reporter-junitfull-export ./junitReport.xml
    done
done