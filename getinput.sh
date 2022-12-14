curl "https://adventofcode.com/2022/day/$1/input" \
  -H 'authority: adventofcode.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'cookie: session=53616c7465645f5f5af87c01bcab673434d54bd7bd6b855f58afbd287a1d8de946061ba2ac15f0d00819c4ded3f9920d8ed63095f5b1c4058496e889e9a3e0eb' \
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