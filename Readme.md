# Wallet Credit Scoring

## Overview

This project analyzes on-chain user wallet transactions to assign a **credit score** (ranging from 0 to 1000) to each wallet. The score is designed to reflect the financial behavior and risk profile of wallet holders using decentralized finance (DeFi) protocols.

---

## Motivation

Traditional credit scoring is not feasible in DeFi due to the pseudonymous nature of wallets. This solution provides a data-driven, transparent, and extensible approach to measure creditworthiness based only on wallet activity, helping lenders and platforms make safer decisions.

---

## Features Engineered

- **Transaction Counts:**
  - Number of deposits, borrows, repayments, redeems, liquidations per wallet.
- **Transaction Amounts:**
  - Total deposited, borrowed, and repaid amounts.
- **Behavioral Ratios:**
  - Responsible Ratio: $(\text{deposits} + \text{repayments}) / \text{total transactions}$
  - Risky Ratio: $(\text{borrows} + \text{liquidations}) / \text{total transactions}$
  - Liquidation Ratio: $\text{liquidations} / \text{total transactions}$
- **Amounts Used for Bonuses/Penalties:**
  - High deposit/repay amounts boost score.
  - High borrow amounts reduce score.

---

## Scoring Logic

- **Responsible actions** (deposits, repayments) increase the score.
- **Risky actions** (borrows, liquidations) decrease the score.
- **Liquidations** penalize the score heavily as they indicate risk of default.
- **Transaction volumes** (deposit/borrow amounts) provide small positive or negative nudges.

### Formula

$$
\text{score} = 500 \\
\text{score} += 200 \times \text{responsible\_ratio} \\
\text{score} -= 300 \times \text{liquidation\_ratio} \\
\text{score} -= 100 \times \text{risky\_ratio} \\
\text{score} += 0.00001 \times \text{deposit\_amt} \\
\text{score} -= 0.00001 \times \text{borrow\_amt} \\
\text{score} = \text{clip}(\text{score}, 0, 1000)
$$

- All ratios are relative to the total number of transactions for the wallet.
- Final score is clipped between 0 and 1000.

---

## Files

- `score_wallets.py` – Python script that processes input and generates scores.
- `user-wallet-transactions.json` – Input file with wallet transaction history.
- `wallet_scores.json` – Output file with computed scores for each wallet.
- `analysis.md` – Detailed analysis of the score distribution and behavioral findings.
- `score_distribution.png` – Visual plot of credit score distribution.
- `plot_scores.py` – Script to generate the distribution plot.

---

## How to Run

1. Place your transaction data in `user-wallet-transactions.json`
2. Run the scoring script:
python score_wallets.py

3. The wallet scores will be saved in `wallet_scores.json`
4. To generate a score distribution graph, run:
python plot_scores.py

This will create `score_distribution.png`.

---



