#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Starting $2 participants in parallel"
for ((i = 1; i <= $2; i++))
do
    python $1 &
done

let break_time=$2*10
sleep $break_time
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
