import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your dataset is loaded into a DataFrame named 'data'
# data = pd.read_csv('your_dataset.csv')

# Set the figure style
sns.set(style="whitegrid")

# Create a function to display all the plots
def plot_fifa_data(data):
    plt.figure(figsize=(10, 6))
    # 1. Distribution of Player Ratings (Overall Rating)
    plt.subplot(3, 3, 1)
    sns.histplot(data['OVR'], bins=20, kde=True, color='skyblue')
    plt.title('Distribution of Player Overall Ratings (OVR)')
    plt.xlabel('Overall Rating (OVR)')
    plt.ylabel('Frequency')

    # 2. Top 10 Players by Overall Rating
    plt.subplot(3, 3, 2)
    top_10_players = data[['Name', 'OVR']].sort_values(by='OVR', ascending=False).head(10)
    sns.barplot(x='OVR', y='Name', data=top_10_players, palette='viridis')
    plt.title('Top 10 Players by Overall Rating (OVR)')
    plt.xlabel('Overall Rating (OVR)')
    plt.ylabel('Player')

    # 3. Player Age Distribution
    plt.subplot(3, 3, 3)
    sns.histplot(data['Age'], bins=15, kde=True, color='lightgreen')
    plt.title('Distribution of Player Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    # 4. Height vs. Weight
    plt.subplot(3, 3, 4)
    sns.scatterplot(x=data['Height'], y=data['Weight'], color='coral')
    plt.title('Height vs. Weight of Players')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')

    # 5. Top 10 Players by Strength
    plt.subplot(3, 3, 5)
    top_10_strength = data[['Name', 'Strength']].sort_values(by='Strength', ascending=False).head(10)
    sns.barplot(x='Strength', y='Name', data=top_10_strength, palette='plasma')
    plt.title('Top 10 Players by Strength')
    plt.xlabel('Strength')
    plt.ylabel('Player')

    # 6. Position Distribution
    plt.subplot(3, 3, 6)
    position_counts = data['Position'].value_counts()
    plt.pie(position_counts, labels=position_counts.index, autopct='%1.1f%%', colors=sns.color_palette('Set3', len(position_counts)))
    plt.title('Distribution of Players by Position')

    # 7. Skill Moves vs Weak Foot
    plt.subplot(3, 3, 7)
    sns.scatterplot(x=data['Skill moves'], y=data['Weak foot'], color='mediumslateblue')
    plt.title('Skill Moves vs Weak Foot')
    plt.xlabel('Skill Moves')
    plt.ylabel('Weak Foot')

    # 8. Correlation Matrix (Heatmap)
    plt.subplot(3, 3, 8)
    corr_data = data[['Acceleration', 'Sprint Speed', 'Finishing', 'Shot Power', 'Short Passing', 'Dribbling', 'Balance', 'Strength']]
    sns.heatmap(corr_data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of Player Attributes')

    # 9. Average Player Strength by Position
    plt.subplot(3, 3, 9)
    average_strength_by_position = data.groupby('Position')['Strength'].mean().sort_values(ascending=False)
    sns.barplot(x=average_strength_by_position.index, y=average_strength_by_position.values, palette='muted')
    plt.title('Average Strength by Position')
    plt.xlabel('Position')
    plt.ylabel('Average Strength')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


data = pd.read_csv("male_players.csv")  # Replace with your dataset path

# Run the function to display all plots
plot_fifa_data(data)
