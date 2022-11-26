#!/bin/bash
for i in {100..110}
do
	python webscraper.py "$i"
done
cat house* > data.csv