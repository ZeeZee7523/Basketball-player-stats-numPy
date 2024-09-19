In the provided code I first created a numPy array using the data straight from the csv file. 
Then I used this numpy array to create a second array that would only contain the stats we wanted to look at for this assignment. 
I extracted one column from the original array at a time, performed needed arithmatic on it with the np.divide() funtion and then added it to the secondary array with np.hstack()
I then sorted the second array by each stat I added and saved the top 100 in that stat into a new array that would print at the end.
