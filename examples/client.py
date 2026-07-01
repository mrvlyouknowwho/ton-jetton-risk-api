"""TON Jetton Risk API — minimal Python client. First 5 calls are free."""
import os
import sys
import urllib.request
import urllib.parse
import json

HOST = "https://mathematical-alice-occupations-permissions.trycloudflare.com"


def risk(address: str, api_key: str) -> dict:
    q = urllib.parse.urlencode({"address": address})
    req = urllib.request.Request(
        f"{HOST}/v1/jetton/risk?{q}", headers={"X-Api-Key": api_key}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        # 402 = out of trial / balance; body has funding instructions
        return json.load(e)


if __name__ == "__main__":
    addr = sys.argv[1] if len(sys.argv) > 1 else "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs"
    key = os.environ.get("API_KEY", "my-secret-key")
    print(json.dumps(risk(addr, key), indent=2, ensure_ascii=False))
