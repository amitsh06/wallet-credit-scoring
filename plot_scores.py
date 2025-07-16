import pandas as pd
import matplotlib.pyplot as plt

# Load scores from your output JSON
df = pd.read_json('wallet_scores.json')

# Create bins for score ranges
bins = list(range(0, 1100, 100))
df['score_bin'] = pd.cut(df['credit_score'], bins=bins)

# Plot distribution
df['score_bin'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Score Range')
plt.ylabel('Number of Wallets')
plt.title('Wallet Score Distribution')
plt.tight_layout()
plt.savefig('score_distribution.png')  # This will save the PNG in your current folder
plt.close()
