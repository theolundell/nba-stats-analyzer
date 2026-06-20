import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("nba_teams_2025_26_dataset.csv")

top_5 = df.sort_values("Wins", ascending=False).head(5)
eastern = df[df["Conference"] == "Eastern"]
western = df[df["Conference"] == "Western"]
eastern_average = eastern["Points_Per_Game"].mean()
western_average = western["Points_Per_Game"].mean()

while True:
    print("\nNBA STATISTICS ANALYZER")
    print("1. View top five teams")
    print("2. Compare conferences")
    print("3. Search for a team")
    print("4. View chart")
    print("5. Top Scoring Teams")
    print("6. Top Shooting Teams")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Enter a number from 1 to 7.")
        continue

    choice = int(choice)

    if choice == 1:
        print(top_5[["Team", "Wins"]].to_string(index=False))
    elif choice == 2:
        print(f"Eastern Total Point Averages: {eastern_average:.1f}")
        print(f"Western Total Point Averages: {western_average:.1f}")
    elif choice == 3:
        selected_team = input("Enter a team name: ").strip().lower()
        team = df[df["Team"].str.lower() == selected_team]

        if team.empty:
            print("Team not found.")
        else:
            team = team.iloc[0]
            print(f"Team: {team['Team']}")
            print(f"Wins: {team['Wins']}")
            print(f"Losses: {team['Losses']}")
            print(f"Conference: {team['Conference']}")
            print(f"Points per game: {team['Points_Per_Game']:.1f}")
    elif choice == 4:
        top_5.plot(
            x="Team",
            y="Wins",
            kind="bar",
            legend=False
        )

        plt.title("Top 5 NBA Teams by Wins")
        plt.xlabel("Team")
        plt.ylabel("Wins")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
    elif choice == 5:
        top_scoring = df.sort_values("Points_Per_Game", ascending=False).head(5)
        print(top_scoring[["Team", "Points_Per_Game"]].to_string(index=False))
    elif choice == 6:
        best_shooting = df.sort_values("Field_Goal_Percentage", ascending=False).head(5)
        print(best_shooting[["Team", "Field_Goal_Percentage"]].to_string(index=False))
    elif choice == 7:
        print("Bye!")
        break
    else:
        print("Enter a valid choice.")
