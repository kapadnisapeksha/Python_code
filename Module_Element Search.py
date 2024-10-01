'''Module: Element Search

In a school, class teacher wants to organize a game for L.K.G students and the game is like there will be a  basket  with numbered balls teacher will give one number and student has to search for that particular  numbered ball if student found that  numbered ball  then he has to say "Got It!" otherwise  "Sorry!".
Help the students to write a program to search the numbered ball.

Input  Format: 

The first line of input corresponds to the number of balls in the basket,n.
The next n  line of input consists of the numbered balls in the basket.
The last line of input consists of a numbered ball to be searched.

Output Format:

The output is a  string consist of 'Got It!' or 'Sorry!' (without quotes).
[All text in bold corresponds to input and the rest corresponds to output.]

Sample Input and Output 1:

5
21
18
90
6
74
6
Got It!

Sample Input and Output 2:

5
21
18
90
6
74
10
Sorry!'''
# Function to search for a ball in the basket
def search_ball(basket, search_number):
    if search_number in basket:
        return "Got It!"
    else:
        return "Sorry!"

# Taking input for the number of balls in the basket
n = int(input())

# Taking input for the numbered balls in the basket
basket = [int(input()) for _ in range(n)]

# Taking input for the numbered ball to be searched
search_number = int(input())

# Search for the ball in the basket
result = search_ball(basket, search_number)

# Output the result
print(result)
   