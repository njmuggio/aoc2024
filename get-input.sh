#!/bin/bash

# Number of extra seconds to wait after the problem unlocks. This helps to
# account for differences between the local time and the AOC server time and
# imprecise integer math.
declare -r slop=5

if [[ $# -eq 0 ]]
then
  declare -i day="$(TZ='America/Detroit' date +%d)"
  day+=1
elif [[ $# -gt 1 ]]
then
  echo "Usage: $0 [day]"
else
  declare -i day="$1"
fi

if [[ ! -f session.txt ]]
then
  echo "Missing session.txt! After logging in to adventofcode.com, copy the
  contents of the session cookie and store it in a file named session.txt"
fi

echo "Will download day $day"

dir="$day"
if [[ $day -lt 10 ]]
then
  dir="0$day"
fi

declare -i target_secs=$(date --date="Dec $day, 2024 12:00:00AM EST" +%s)
target_secs+=$slop

while (((target_secs - EPOCHSECONDS) > slop))
do
  declare -i sleep_secs=$(((target_secs - EPOCHSECONDS) / 2))
  echo "Sleeping $sleep_secs seconds..."
  sleep $sleep_secs
done

while ((EPOCHSECONDS < target_secs))
do
  sleep 0.1
done

curl --cookie "session=$(cat session.txt)" https://adventofcode.com/2024/day/"$1"/input > "$dir/input"
