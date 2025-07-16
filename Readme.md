# Wallet Credit Scoring

This project analyzes user wallet transactions and assigns a credit score (0–1000) to each wallet using a custom Python script.

## Features Used
- Counts of deposit, borrow, repay, redeem, and liquidation actions
- Sums of transaction amounts per action
- Ratios of responsible (deposit, repay) vs. risky (borrow, liquidation) actions

## Scoring Logic
- Higher score for responsible actions (deposit, repay)
- Lower score for risky actions (borrow, liquidation)
- Liquidation events penalize the score heavily
- Formula:  
  - Start from 500  
  - +200 × responsible_ratio  
  - -300 × liquidation_ratio  
  - -100 × risky_ratio  
  - +0.00001 × deposit_amt  
  - -0.00001 × borrow_amt  
  - Result clipped to [0, 1000]

## How to Run
1. Place your transaction data in `user-wallet-transactions.json`
2. Run:  
python score_wallets.py
3. Output: `wallet_scores.json` with credit scores for all wallets

## Files
- `score_wallets.py` – main scoring script
- `user-wallet-transactions.json` – input transaction data
- `wallet_scores.json` – output scores
- `analysis.md` – score analysis and distribution
