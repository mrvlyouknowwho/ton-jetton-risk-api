# TON Jetton Risk API

A pay-per-call risk snapshot for TON jettons (tokens). Screen a token **before** you buy — catch rugs, honeypots, and mint traps. Built for sniper bots, trading bots, and traders on TON.

One HTTP call → a deterministic risk score. No SDK, no signup. **First 5 calls free.**

> Beta hosted endpoint: `https://mathematical-alice-occupations-permissions.trycloudflare.com`
> (early access; the stable domain is coming — watch this repo.)

📖 **Guide:** [How to spot a TON jetton rug pull before you buy](./GUIDE.md)

## Quickstart

```bash
# free trial (5 calls, no payment): pick any secret string as your API key
curl -H "X-Api-Key: my-secret-key" \
  "https://mathematical-alice-occupations-permissions.trycloudflare.com/v1/jetton/risk?address=EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs"
```

Response:
```json
{
  "address": "EQCxE6mU...",
  "symbol": "USD₮",
  "mintRevoked": false,
  "holdersCount": 3305827,
  "holders": { "top1Pct": 53.79, "top10Pct": 78.15 },
  "liquidity": { "listed": true, "liquidityTier": "very_high", "taxable": false, "blacklisted": false },
  "honeypot": { "risk": "low" },
  "score": 40,
  "flags": ["mint_not_revoked", "admin_present", "holder_concentration_high"],
  "_billing": { "mode": "trial", "trialRemaining": 4 }
}
```

`score`: 0 (clean) → 100 (dangerous). `flags` explain why.

## What it checks

| Signal | Source | Why it matters |
|---|---|---|
| Mint authority revoked | jetton master contract | if not revoked, the dev can mint unlimited supply and dilute you |
| Holder concentration (top 1% / 10%) | on-chain holders | a few wallets holding most supply = dump risk |
| Holder count | on-chain | very few holders = fresh / thin token |
| DEX liquidity + tier | STON.fi | no pool / thin liquidity = you may not be able to sell |
| Taxable transfer | STON.fi | hidden transfer tax = honeypot-adjacent |
| Blacklisted | STON.fi | flagged by the DEX |
| Honeypot risk (heuristic) | derived | low / high / unknown from the above; precise sell-emulation on the roadmap |

## Pricing

- **Free:** first 5 calls per API key — try before you pay.
- **Paid:** $0.001 USDT per call, prepaid balance. No subscription, no card.

### How to pay (USDT on TON)

Send USDT (TON network) to the address below with **your API key as the transfer comment (memo)**. Balance is credited automatically within ~20s; each call debits $0.001.

```
Network:  TON
Asset:    USDT (USD₮, Tether on TON)
Address:  UQD6z4gLZ7HQXu3YGF6sre0uZaIsffUflKYJKEyLx8AYj1TN
Comment:  <your API key>   ← required: this links the deposit to your key
```

> ⚠️ Send **USDT on the TON network only**. Sending from another chain (e.g. TRC20/ERC20) will be lost.

The `_billing` field in every response shows your remaining trial calls or paid balance.

## Endpoint

`GET /v1/jetton/risk?address=<jetton_master_address>`

- Header: `X-Api-Key: <your key>` (any secret string you choose)
- `address`: jetton master address in friendly `EQ…` / `UQ…` form

Payment is checked before any work: unpaid/exhausted keys get HTTP `402` with funding instructions — no charge, no data on failure.

## Examples

See [`examples/`](./examples) for `curl` and Python clients.

## Status

Live beta. Signals above are active. Roadmap: precise honeypot sell-simulation, TRON-USDT payments, stable custom domain. Issues/requests welcome.
