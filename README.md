# Overthinking Wordle Notes
### Created: 2022-February-27

We want to find 5 words that have no letters in common and are prefereable ranked by the most frequently occuring characters.

So basically this whole project could be replaced with google search for some statistics of the english language, but that would
be boring so lets build our owns from the full text of "War and Peace" instead.

So stats are pretty much for fun, cool to look, but the problem is simpler than that.

If we brute all 5 letter words with single chars than we have 26*25*24*23*22 = 7893600 combinations
of letters to check. Which is manageble I suppose.

We could also cut this by using bigrams as the start of the word.

There are only 2 such collections of 5 letter words that share no letters in common.
So the most you can eliminate is 10 letters. Sad.

What is the ideal condition of a sequence of mutually exclusive words?

That they represent the most frequently occuring characters in english in grouping
by words.

We if we rank the words by char frequency, then sort them, then weight them by index so
that the largest gets the highest, than the lowest gets the lowest weight.

Then we hope to promote the sum with the desired distribution of frequent characters.
