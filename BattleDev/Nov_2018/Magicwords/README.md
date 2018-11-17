# Goal

A friend of yours plays on a Rugby team. He throws the ball when there
is touch. During a touch, the thrower must communicate to other players how
high he will send the ball with a code that the opponents must not be able to
decode.  For  each  height,  there  are  several  codes.  The launcher
shouts several words, only one of which corresponds to a code, and the whole team
can thus determine the chosen height.

Your friend presents you with a list of words that the players have proposed (a
word may appear several times in his list) and asks you to find a method to
extract "magic" words that will be used as code. He will associate them with
heights afterwards.  You  have  decided  that  a  magic  word  would  have  the
following characteristics:
  - It must contain between 5 and 7 letters.
  - It must begin with two letters of the alphabet that follow in alphabetical
order.
  - It must end with a vowel (a, e, i, o,u, or y(y is a vowel in French))

You need to determine how many different magic words are in his list.

## Data

### Input

Row 1: an integer N between 10 and 1000 corresponding to the number of words in the list.

Rows 2 to N + 1: a string containing between 2 and 20 lower case characters corresponding to a word.

### Output

An integer corresponding to the number of different magic words contained in the list.
