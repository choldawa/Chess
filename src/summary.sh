#!/bin/bash

awk '{sum+=$1}END{print NR, sum}' $1