# How to spot a TON jetton rug pull before you buy (2026)

Most TON memecoin losses are avoidable. A rug or honeypot leaves on-chain fingerprints
*before* the dump. This guide covers the concrete signals to check on any TON jetton (token),
why each matters, and how to check all of them in one API call.

## The signals that actually matter

### 1. Mint authority not revoked
A jetton's master contract stores a `mintable` flag and an `admin` address. If mint is still
enabled, the deployer can print unlimited new supply and dilute holders to zero. **Revoked mint
= one less way to get rugged.** A legit fixed-supply token has `mintable: false` and often a
burned/empty admin.

### 2. Holder concentration
If the top 1–10 wallets hold most of the supply, a single sell dumps the price. Check the
top-1% and top-10% share. High concentration on a *new* token is the classic pre-dump setup.

### 3. Holder count
A token with a handful of holders is either brand new or fake volume. Very low holder counts
mean thin, manipulable markets.

### 4. DEX liquidity and its depth
No pool on STON.fi/DeDust, or a tiny one, means **you may not be able to sell** — the exit is
the trap. Check that real liquidity exists and its tier (e.g. STON.fi tags liquidity as
`very_high` down to none). Thin liquidity + high concentration is a red flag stack.

### 5. Taxable transfers
A hidden transfer tax is honeypot-adjacent: you buy, but selling costs a punitive fee or fails.
Check the token's `taxable` flag.

### 6. Blacklist / verification status
DEXs flag known-bad tokens. If STON.fi has it blacklisted, walk away.

## Check all of it in one call

Instead of opening six explorers, [TON Jetton Risk API](https://github.com/mrvlyouknowwho/ton-jetton-risk-api)
returns every signal above plus a 0–100 risk score and human-readable flags in one request.
First 5 calls are free:

```bash
curl -H "X-Api-Key: my-key" \
  "https://mathematical-alice-occupations-permissions.trycloudflare.com/v1/jetton/risk?address=<JETTON_MASTER>"
```

A clean blue-chip (e.g. USDT on TON) scores low; a token with mint enabled, concentrated
holders, and no liquidity scores high with explicit flags telling you why.

## Rules of thumb

- Never buy a token you can't sell — verify liquidity and taxable status first.
- Fresh token + mint enabled + top wallet > 30% = assume dump risk.
- Automate it: if you run a sniper/trading bot, screen every candidate token programmatically
  before entry.

See the [full API docs and examples](https://github.com/mrvlyouknowwho/ton-jetton-risk-api).
