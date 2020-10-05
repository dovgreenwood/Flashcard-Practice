# Flashcard Practice
 New Flashcard Practicing App

This program, once complete, will be a new flashcard app, inspired, but no based in, the principle of Spaced Repetition Learning. The idea of it is as follows: when you rate a card on a flashcard app, you are actually rating your own confidence that you know the card at a particular time, not your *real* knowledge of that card. To approximate your "true" knowledge of a card, you need to keep in mind what got you to that point--how many times you've rated your confidence in that card at a maximum, how long you've been practicing it, and what path you took to get there (example: did you know the card from the first time you saw it? Did you learn it slowly, over time? Do you rates cards on a 1 or 5 binary rather than a 1-5 scale, eliminating nuance?).

This *real* knowledge can be tracked by approximating your learning of that card by using a statistical model. Which one to use yet, I'm not sure, but likely a multinomial logistic model. The coefficient vector generated from a model based on your past ~20 confidence ratings of that card will serve as your "true knowledge" vector, and the goal is thus now not to simply maximize confidence, but to maximize "true knowledge." Essentially, you want to get the model to become a horizontal line with a y-intercept at 5.

The idea was born of my frustration with Anki (an extremely populat SR flashcard app), because it's so difficult to understand what's going on under the hood in that app; and Brainscape, an online SR flashcard site, whose software doesn't work very well (e.g. once you rate all cards at 5, each time you enter that deck, it shows you all the cards in order starting from the first one). I am hoping to solve both of these problems by eventually have a more intuitive GUI and a better model of learning, based on statistics rather than personal rating.

The program is currently under development. 
