curl "https://adventofcode.com/2022/day/$1/input" \
  -H 'authority: adventofcode.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'cookie: session=53616c7465645f5f47ef35db8f3621045a963e0064a8eda8972b87892642a68c59d5e4a6bafc920e79f6aa7cdef0af49078dc5e6dad56254a0063b018cc2edab' \
  -H 'referer: https://adventofcode.com/2022/day/1' \
  -H 'sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-gpc: 1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: nicholas.estoll@gmail.com' \
  --compressed \
  --insecure \
  -o "./day$1/input.txt"
  if [[ $(cat ./day$1/input.txt) == $(cat bad.txt) ]]
  then
    rm "./day$1/input.txt"
  fi