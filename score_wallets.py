import pandas as pd
import numpy as np
import json

# Load JSON data
with open('user-wallet-transactions.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract flat columns for processing
df['amount'] = df['actionData'].apply(lambda x: float(x.get('amount', 0)))
df['userWallet'] = df['userWallet']
df['action'] = df['action']

features = []
for wallet, group in df.groupby('userWallet'):
    total_tx = len(group)
    deposit = (group['action'] == 'deposit').sum()
    borrow = (group['action'] == 'borrow').sum()
    repay = (group['action'] == 'repay').sum()
    redeem = (group['action'] == 'redeemunderlying').sum()
    liquidation = (group['action'] == 'liquidationcall').sum()
    deposit_amt = group[(group['action'] == 'deposit')]['amount'].sum()
    borrow_amt = group[(group['action'] == 'borrow')]['amount'].sum()
    repay_amt = group[(group['action'] == 'repay')]['amount'].sum()
    liquidation_ratio = liquidation / total_tx if total_tx else 0
    responsible_ratio = (repay + deposit) / total_tx if total_tx else 0
    risky_ratio = (borrow + liquidation) / total_tx if total_tx else 0

    features.append({
        'userWallet': wallet,
        'total_tx': total_tx,
        'deposit': deposit,
        'borrow': borrow,
        'repay': repay,
        'redeem': redeem,
        'liquidation': liquidation,
        'deposit_amt': deposit_amt,
        'borrow_amt': borrow_amt,
        'repay_amt': repay_amt,
        'liquidation_ratio': liquidation_ratio,
        'responsible_ratio': responsible_ratio,
        'risky_ratio': risky_ratio
    })

feat_df = pd.DataFrame(features)

def score(row):
    score = 500
    score += 200 * row['responsible_ratio']
    score -= 300 * row['liquidation_ratio']
    score -= 100 * row['risky_ratio']
    score += 0.00001 * row['deposit_amt']
    score -= 0.00001 * row['borrow_amt']
    return np.clip(score, 0, 1000)

feat_df['credit_score'] = feat_df.apply(score, axis=1)

result = feat_df[['userWallet', 'credit_score']].to_dict(orient='records')
with open('wallet_scores.json', 'w') as f:
    json.dump(result, f, indent=2)
