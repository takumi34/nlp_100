#!/bin/bash
cut -f 1 popular-names.txt | sort | uniq -c | sort -nrk 1 | awk '{print $2}'
