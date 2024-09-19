""" Data collection and analysis have revolutionized modern sports, especially basketball. Analysts, teams, coaches, and players all participate with the hope that the insights it provides will give them a competitive edge. Common analyses include player performance analysis, opponent scouting, game strategy optimization, injury prevention, fan engagement, and player recruitment. Use the data provided, a subset of the data contained in a Kaggle Repository

Links to an external site., to answer the following questions.

    Determine the field goal accuracy, three point accuracy, and free throw accuracy for each player in each season.
    Determine the averrage points scored per minute for each player in each season.
    Determine the overall shooting accuracy of each player in each season.
    Determine the average number of blocks per game and the average number of steals per game for each player in each season.

Create a list of the top 100 players and corresponding season for each of your calculated metrics: field goal accuracy, three point accuracy, free throw accuracy, average points scored per game, overall shooting accuracy, average blocks per game, and average steals per game.
 """
import numpy as np

# Load the CSV file into a NumPy ndarray
players_stats =np.genfromtxt("players_stats_by_season_full_details(1).csv", delimiter=",",skip_header=1,ndmin=2, dtype=str,missing_values="",filling_values="N/A",usecols=range(0, 32),loose=True)  

# Display the first few rows of the ndarray to verify
#print(players_stats[0:2])

#Determine the field goal accuracy, three point accuracy, and free throw accuracy for each player in each season.

#asked github for this "how do I make a new ndarray where the first column is the 4th colomn of the selected array without duplicates"
# Extract the 4th column (index 3) from the players_stats array
fourth_column = players_stats[:, 1:4]



# Create a new ndarray with the values
players_season = fourth_column.reshape(-1, 3)
players = np.delete(players_season,1,axis=1)


#asked github for help dividing the FGM and FGA to get the shooting accuracy

column_8 = players_stats[:, 7].astype(float)
column_9 = players_stats[:, 8].astype(float)

# Perform the division
division_result = np.divide(column_8, column_9, out=np.zeros_like(column_8), where=column_9!=0)

# Reshape the division result to be a column vector
division_result = division_result.reshape(-1, 1)
players = np.hstack((players, division_result))


#I then did the 3point and free throw accuracy the same way on my own

column_10 = players_stats[:, 9].astype(float)
column_11 = players_stats[:, 10].astype(float)


division_result = np.divide(column_10, column_11, out=np.zeros_like(column_10), where=column_11!=0)
division_result = division_result.reshape(-1, 1)

players = np.hstack((players, division_result))

#free throw accuracy
column_12 = players_stats[:, 11].astype(float)
column_13 = players_stats[:, 12].astype(float)

division_result = np.divide(column_12, column_13, out=np.zeros_like(column_12), where=column_13!=0)
division_result = division_result.reshape(-1, 1)

players = np.hstack((players, division_result))


#    Determine the averrage points scored per minute for each player in each season.
# thats just points/minutes so its column 22/column 7
column_22 = players_stats[:, 21].astype(float)
column_7 = players_stats[:, 6].astype(float)

division_result = np.divide(column_22, column_7, out=np.zeros_like(column_22), where=column_7!=0)
division_result = division_result.reshape(-1, 1)

players = np.hstack((players, division_result))

#    Determine the overall shooting accuracy of each player in each season.
# overall shooting accuracy is FGM(col 8) + 3PM(col 10) + FTM(col 12) / FGA(col 9) + 3PA(col 11) + FTA(col 13) so we already have all those columns
shots_made = column_8 + column_10 + column_12
shots_attempted = column_9 + column_11 + column_13

division_result = np.divide(shots_made, shots_attempted, out=np.zeros_like(shots_made), where=shots_attempted!=0)
division_result = division_result.reshape(-1, 1)

players = np.hstack((players, division_result))


#    Determine the average number of blocks per game and the average number of steals per game for each player in each season.
# steal is col 20 and block is col 21 and games played is col 6
steals = players_stats[:, 19].astype(float)
blocks = players_stats[:, 20].astype(float)
games_played = players_stats[:, 5].astype(float)

average_steals = np.divide(steals, games_played, out=np.zeros_like(steals), where=games_played!=0)
average_blocks = np.divide(blocks, games_played, out=np.zeros_like(blocks), where=games_played!=0)

average_steals = average_steals.reshape(-1, 1)
average_blocks = average_blocks.reshape(-1, 1)

players = np.hstack((players, average_blocks, average_steals)) 



#print(players)
#Create a list of the top 100 players and corresponding season for each of your calculated metrics: field goal accuracy, three point accuracy, free throw accuracy, average points scored per game, overall shooting accuracy, average blocks per game, and average steals per game.
#I will sort the players array by each column and then store the top 100 players in a new array
#I had to ask github for help on how to sort the array by a specific column and it gave me the argsort function as shown below


#field goal accuracy
sorted_players = players[players[:, 2].argsort()]
top_100_field_goal = sorted_players[-100:,:]

#three point accuracy
sorted_players = players[players[:, 3].argsort()]
top_100_three_point = sorted_players[-100:,:]

#free throw accuracy
sorted_players = players[players[:, 4].argsort()]
top_100_free_throw = sorted_players[-100:,:]

#average points scored per game
sorted_players = players[players[:, 5].argsort()]
top_100_points = sorted_players[-100:,:]

#overall shooting accuracy
sorted_players = players[players[:, 6].argsort()]
top_100_shooting = sorted_players[-100:,:]

#average blocks per game
sorted_players = players[players[:, 7].argsort()]
top_100_blocks = sorted_players[-100:,:]

#average steals per game
sorted_players = players[players[:, 8].argsort()]
top_100_steals = sorted_players[-100:,:]




print("\ntop 2 players for field goal accuracy")
print(top_100_field_goal[-2:,:])
print("\ntop 2 players for three point accuracy")
print(top_100_three_point[-2:,:])
print("\ntop 2 players for free throw accuracy")
print(top_100_free_throw[-2:,:])
print("\ntop 2 players for average points scored per minute")
print(top_100_points[-2:,:])
print("\ntop 2 players for overall shooting accuracy")
print(top_100_shooting[-2:,:])
print("\ntop 2 players for average blocks per game")
print(top_100_blocks[-2:,:])
print("\ntop 2 players for average steals per game")
print(top_100_steals[-2:,:])
