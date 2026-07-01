#!/usr/bin/env bash
# TON Jetton Risk API — quickstart. First 5 calls are free.
set -euo pipefail

HOST="https://mathematical-alice-occupations-permissions.trycloudflare.com"
API_KEY="${API_KEY:-my-secret-key}"          # pick any secret string
JETTON="${1:-EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs}"  # default: USDT

curl -s -H "X-Api-Key: ${API_KEY}" \
  "${HOST}/v1/jetton/risk?address=${JETTON}" | python3 -m json.tool
