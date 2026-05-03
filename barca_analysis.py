# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (make sure the path is correct)
df = pd.read_csv(r"C:\Users\USER\Desktop\Work\barca 2009 analytics\barca_2009_10.csv")

# -------------------------------
# BASIC DATA OVERVIEW
# -------------------------------

# Display first few rows (for sanity check)
print("Dataset Preview:")
print(df.head())

# -------------------------------
# TEAM PERFORMANCE STATS
# -------------------------------

# Calculate match results
wins = (df['Result'] == 'W').sum()
draws = (df['Result'] == 'D').sum()
losses = (df['Result'] == 'L').sum()

# Calculate goals
goals_scored = df['Goals_Scored'].sum()
goals_conceded = df['Goals_Conceded'].sum()

# Calculate Win Percentage
total_matches = len(df)
win_rate = (wins / total_matches) * 100

# Print results
print("\n--- Team Performance ---")
print(f"Total Matches: {total_matches}")
print(f"Wins: {wins}")
print(f"Draws: {draws}")
print(f"Losses: {losses}")
print(f"Win Rate: {win_rate:.2f}%")
print(f"Goals Scored: {goals_scored}")
print(f"Goals Conceded: {goals_conceded}")

# -------------------------------
# ADDITIONAL INSIGHTS
# -------------------------------

# Best attacking match (max goals scored)
best_match = df.loc[df['Goals_Scored'].idxmax()]

print("\n--- Best Match (Highest Goals Scored) ---")
print(best_match)

# Clean sheets (no goals conceded)
clean_sheets = (df['Goals_Conceded'] == 0).sum()
print(f"\nClean Sheets: {clean_sheets}")

# -------------------------------
# VISUALIZATION SECTION
# -------------------------------

# 1. Goals Scored per Match
plt.figure()
plt.plot(df['Match'], df['Goals_Scored'], marker='o')
plt.title("Goals Scored per Match (Barcelona 2009-10)")
plt.xlabel("Match Number")
plt.ylabel("Goals Scored")
plt.grid()

# Save BEFORE showing
plt.savefig(r"C:\Users\USER\Desktop\Work\barca 2009 analytics\goals_scored.png")
plt.show()


# 2. Goals Conceded per Match
plt.figure()
plt.plot(df['Match'], df['Goals_Conceded'], marker='o')
plt.title("Goals Conceded per Match (Barcelona 2009-10)")
plt.xlabel("Match Number")
plt.ylabel("Goals Conceded")
plt.grid()

plt.savefig(r"C:\Users\USER\Desktop\Work\barca 2009 analytics\goals_conceded.png")
plt.show()


# 3. Combined Goals (Scored vs Conceded)
plt.figure()
plt.plot(df['Match'], df['Goals_Scored'], marker='o', label="Scored")
plt.plot(df['Match'], df['Goals_Conceded'], marker='o', label="Conceded")

plt.title("Goals Scored vs Conceded")
plt.xlabel("Match Number")
plt.ylabel("Goals")
plt.legend()
plt.grid()

plt.savefig(r"C:\Users\USER\Desktop\Work\barca 2009 analytics\goals_comparison.png")
plt.show()


# 4. Match Results Distribution (Pie Chart)
plt.figure()
results = [wins, draws, losses]
labels = ['Wins', 'Draws', 'Losses']

plt.pie(results, labels=labels, autopct='%1.1f%%')
plt.title("Match Results Distribution")

plt.savefig(r"C:\Users\USER\Desktop\Work\barca 2009 analytics\results_distribution.png")
plt.show()