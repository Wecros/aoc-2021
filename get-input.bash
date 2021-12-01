#!/usr/bin/env bash

# Author: Wecros <Marek Filip>
# Date: 01/12/2020
# Brief: Get the user's input and print it to the stdout.
# Parameters:
#   1st: Number of day. Day ∈ <1, 25>.
#   stdin or 2nd: User's session ID got from the cookie header.

# use bash "strict" mode
# source: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail

function print_usage() {
	printf "Usage:\n"
	printf "\tget-input.bash <day_number> [session_id]\n"
	printf "\tget-input.bash -h\n"
	printf "\n"
	printf "Parameters:\n"
	printf "\t1st: Number of day. Day ∈ <1, 25>.\n"
	printf "\t2nd|stdin: User's session ID got from the cookie header.\n"
	printf "\n"
	printf "Options:\n"
	printf "\t-h: Print this.\n"
	exit 1
}

# get and handlearguments
set +u
# first arg
day_no="$1"
if [ "$day_no" = "-h" ] || [ -z "$day_no" ]; then
	print_usage
fi
if ((day_no < 1 || day_no > 25)); then
	printf "Day number needs to be between 1 and 25.\n\n"
	print_usage
fi

# second arg
session_id=""
while read -r line
do
	session_id="$line"
done < "${2-/dev/stdin}"  # 2nd arg or stdin

if [[ -z "$session_id" ]]; then
	printf "Session ID must be provided.\n\n"
	print_usage
fi
# got right arguments here
set +u

# set the pwd to the script's location
cd "$(dirname "$0")"

mkdir -p "day$day_no"
# print the request to the standard output
curl -s -X GET "https://adventofcode.com/2021/day/$day_no/input" \
	-H "cookie: session=$session_id" > "day$day_no/input.txt"
