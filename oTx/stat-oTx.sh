#!/bin/bash
ls | awk -F"." '{print $1}' | sort | uniq -c | sort -n
