# Project: Graph Theory 2021
**Name:** Emmanuel Osabuehien\
**Student ID:** G00373559\
**Module:** Graph Theory\
**Date:** 30/04/2021

## Description

In regards to my project, my repository should be very simple to follow and easy to follow, I didn't want to make it difficult for an uncommon user to follow but still make it seem quite professional, the contents within my repository.

My project searches text files using regular expressions, it is written in the Python 3 programming language, the concept is to match any string of text matches a regular expression which will be compared using an Non-Definite Automaton also known as an NFA for short which involes operations for regular expressions, e.g. Concatanate, this code is coded from scratch and will not use external libraries such as re package.

## Instructions

My program isn't too complex in the way it is presented or coded, it should be simple to follow how to get this up and running.

Before attempting to test my program make sure git is installed on your selected device.

- First you should navigate to my github repository (https://github.com/Emmanuel-Osabuehien/project-graph-theory)
- You should then clone/download my repository to your local machine
- Open a command line or terminal whichever you prefer
- Enter a location that you wish to perform this test before cloning your repostiory, e.g. mkdir project, cd project
- Clone the repository into your command line or terminal by typing "git clone https://github.com/Emmanuel-Osabuehien/project-graph-theory"
- The contents of the repository should then be imported onto your local machine 
- Assuming everything needed to run this program correctly is installed (Git, Python, Anaconda), you can then run the program by typing "Python regex.py" or "Python3 regex.py" which ever one suits you

You will then be presented with a list of infixes and match function like so:

infix:   a.(b.b)*.a
postfix: abb.*.a.
nfa:  {<__main__.NFA object at 0x7f8b58008eb8>}
The String Passes True Or False: True
The String Passes True Or False: False
The String Passes True Or False: False
The String Passes True Or False: False
The String Passes True Or False: False
The String Passes True Or False: False
The String Passes True Or False: False
The String Passes True Or False: False
The String Passes True Or False: False
The String Passes True Or False: False
infix:   a.b
postfix: ab.

You should also be presented with a sort of main menu where you can interact with the program by:

1. Reading a text file which contains and infix and comparing that infix with strings from another text file.
2. Printing out the results from the above function to a seperate text file

The file and infix should be entered in manually and for exmaple something like this should be printed when passed:

Match: True, Infix: a+b.c, String: abc

3. You can then choose to exit the program if you wish

## Explanation

The Shunting Yard Alogrithm was the whole basis for my program, the Shunting Yard Alogrithm was created by computer scientist Edsger Dijkstra, a fun fact is the algorithm is actually named after a railroad shunting yard due to the operations resemblence.
The algorithm was invented with the use of parsing mathematical expressions in infix notation and in turn can produce a postfix notation, as we see later when using the algorithm for our program, the algorithm is stack-based and the alogrithm can also be used to convert string variables (input and output).

Most people use Infix expressions (this is a single letter or operator which is preceded by an infix string and another infix string) as a form of mathematical notation, an example of this is: (3 + 4)

1. Input: 3 + 4
2. Push 3 to the output queue (whenever a number is read it is pushed to the output)
3. Push + (or its ID) onto the operator stack
4. Push 4 to the output queue
5. After reading the expression, pop the operators off the stack and add them to the output.
In this case there is only one, "+".
6. Output: 3 4 +

Look at [Brilliant.Org,<br> https://brilliant.org/wiki/shunting-yard-algorithm](https://brilliant.org/wiki/shunting-yard-algorithm) and [Wikipedia,<br> https://en.wikipedia.org/wiki/Shunting-yard_algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

Now a closer look in my project specfically, lets take a deep dive into how I implmented this algorithm into my program:

- The program requests the user to enter a condition for the NFA.
- The program then determines whther the condition is infix or postfix based the string constaining brackets/notation
- If the string contains a bracket the program will convert the string to postfix notation.
- We then create and set an Operatror Precedence which itself contains the order of precedence each special character is taken into.
- The Operator Precendence contains the Kleane star (*), the Concatination notation (.) and the OR operator (|).
- Two runes are Created a postfix rune and a rune labeled s, These will be used as stacks to add and remove from.
- We then loop thorugh the infix with just one character at a time.
- If the current charcater is an opening bracket, then the character is added to the stack (s)
- But if the current character is a closing bracket, then it continues popping from s stack until an opening bracket is recieved, it will then append the top of the s stack to the postfix until opening bracket is found and the stack is the same as the previous s stack with just one one less item
- If the current character is equal to one of the characters in the operator precedence then it is then added to the top of the s stack to the postfix stack with all elements which in turn removes the last item and adds the current characters to the s stack
- If the current character does not fit one of the previous conditions, append to the postfix stack
- If the length of the s stack  is larger than, then the last item of the s stack is then added to postifx stack and all characters from s stack except char is added to postfix stack and the loop will continue until s stack is empty
- Postfix is then returned to a string.
- A boolean variable will be returned to tell if the string was a match or not.

After this, I use Thompson's Construction to build an NFA Algorithm which creates an NFA stack and will help convert my regular expression into a NFA object and there I then create my different functions to read files, print outputs, match strings and compare to NFA.

Here is a link to some of the rough work I used to complete this project: [Github, https://github.com/Emmanuel-Osabuehien/graph-theory-project](https://github.com/Emmanuel-Osabuehien/graph-theory-project)

## What is a regular expression?

 Before we get into what is a regular expession in python, the whole concept and development of a regular expression can be dated back to as early as the 1950's and maybe even in the 1940's but in 1951, the concept of regular language was created by a mathematician by the name of Stephen Cole Kleene, where we have a language that can be idenitfied by a finite automaton and represented using regular expression.

As we move on to the 1960's where a Ken Thompson who was a computer science pioneer and is also one of the designers of Unix (a multitasking, multiuser computing operating system) would add the concept of matching patterns in a text editor using Stephen Cole Kleene's code and in the 1970's is when we really see regular expressions takeover the programming world, another note is the whole concept became common use with Unix text-processing.
 
As we move on to modern day computer science, we see how highley influential this was as we now see the use of regular expressions in so many different programming languages such as Python, C#, Javascript and many more but also regular expressions are used in text editor as well as a use for other tools where we can regulate if a special sequence of characters or string match a specific pattern.

This information I obtained reading books, pdf's and websites such as: 

- [Wikipedia,<br> https://en.wikipedia.org/wiki/Regular_expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Teach Yourself Regular Expression in 10 Minutes by Ben Forta,<br> http://mygugazabocu.bloggersdelight.dk/sams-teach-yourself-regular-expressions-in-10-minutes-pdf](http://mygugazabocu.bloggersdelight.dk/sams-teach-yourself-regular-expressions-in-10-minutes-pdf)
- [Mastering Regular Expressions by Jeffrey Friedl,<br> https://www.amazon.co.uk/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124](https://www.amazon.co.uk/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124) (You can purchase this book here but you can also find pdf's online to read through)

Now we move on to the main question what is a regular expression, A regular expression or sometimes referred to as a regex can be defined as a unique set or sequence of characters that are used to to match, locate and manage a set of strings.

Here is an example of using regular expression in python for pattern matching:

s = 'emmanuel70156'

import re

if re.search('123', s):
    print('Found a match.')
else:
    print('No match.')

As you can see in the above code, the regex is '015' and the string is 's' and re.search is used to return the match object instead of null and when it is run in python it should print out the text 'Found a match.'

One of the most common methods of using a regular expression is used in a command line and in text editors to find text inside a file and another use is when search engines use regular expression to search and replace dialogs of word processors and text editors.

Perl is one good example of a prograaming language that uses regular expression as this arose in the 1980's and it was originally fored from regular expression library and this library was later expanded and added many new features.

An example of using regular expression in Perl could be as follows:

$data =~ s/e/E/;

The above example is a piece of code where we search and replace any data variable with a lowercase 'e' with and uppercase 'E', e.g. 'An elephant in the river' gets replaced with 'An ElEphant in the rivEr'.

We can even change this to change a whole world for example:

$data =~ s/happy morning/good night/i;

The above example is a piece of code where any data variable wih 'happy morning' changes to 'good night', e.g. 'Have a happy morning' changes to 'Have a good night'.

You can find a moe examples of this on websites such as [(Google For Education, https://developers.google.com/edu/python/regular-expressions)](https://developers.google.com/edu/python/regular-expressions)

So this all here is all about regular expressions from a brief history of the concept and creation, to it's impact in programming languages, to some examples of it's uses and most important the definition of what is a regular expression.

 ## How do regular expressions differ across implementations?

To understand the many different ways of implementations of regular expression, you have to understand about what are regular expressions (regex) and how they work which we have already discussed in the previous question as well as an understanding of the regex engine, when you have the knowledge of all this you will then know how to craft a great amount of regular expressions with ease and it may also help with the understanding of why a regular expression may not do as expected or intended to savinga lot of time that may have felt wasted.

Much information can be obtained on regular expressions in relation to implentation from [(*Regular Expression Matching Can Be Simple And Fast*, Russ Cox, https://swtch.com/~rsc/regexp/regexp1.html)](https://swtch.com/~rsc/regexp/regexp1.html)

Now as we will discuss later in my next question, we see that many different formal languages can use regular expression which means we can implement regular expressions in a vast variety of different ways as each language is going to have its own form of implementation.

When it comes to implementation in regular expression there are many implementations that differ both just slightly and outstandingly whether in syntax or behaviour but in this case there two types of regular expressions (regex engines) are they are known as regex driven and text driven.

Nowadays, when you come across most modern regular expressions implemented in any language that can encode regular expression, they are more than likely going to be regex driven due to advantage of features associated such as backrefencing (This is when you can identify a previously matched group and look for the exact same text again).

When it comes to regex driven engines (Regexps), regular languages have a lot of structure, a regex driven engine will walk thorugh the regular expression and attempts to match the token in the regex to the next character, if there is match the engine will proceed in the regex and string, if it fails then the engine then backtracks in the regex and string and will continue to try a different path, backtracking is where you try to match as much of the string as you can but if you get stuck you have to go back and try a different way to match it.

But when it comes to text driven engines (regular expressions), the engine will walk through the string instead of the regular expression and attempts to grouping of regular expressions before eventually proceeding to the next character in the string, there is a huge difference compared to regex driven engines as a text driven engine will never backtrackbut at the same time the text driven engine will find the same matches as a regex driven engine would find.

There are three different algorithms that are used to choose whether and how a regex matches a string, one is the tranformation of nondeterministic finite automaton (NFA) to deterministic finite automaton (DFA), the DFA can be constructed and then run on the resulting input string one symbol at a time.

Another algorithm is to duplicate the NFA directly, building each DFA state and getting rid of it after it moves on, the advantages of this is it will keep the DFA indirect and avoids rising construction costs.

The final algortihm is the use of the aforementioned "Backtracking" where you try to match as much of the string as you can but if you get stuck you have to go back and try a different way to match it.

Reading through the "implementation and running times" section on wikipedia is also a good read to gain knowledge on this question, [(Wikipedia, https://en.wikipedia.org/wiki/Regular_expression)](https://en.wikipedia.org/wiki/Regular_expression/)

So this all is how regular expression differs across implementation.

Search through [(Regular Expressions: Regexes in Python*, Real Python, https://realpython.com/regex-python)](https://realpython.com/regex-python) if you wish to understand more about regular expressons and it's different forms of implementations.

 ## Can all formal languages be encoded as regular expressions?

When I was talking in the previous question (What is a regular expression?), I made some references to how there are many different programming languages that use regular expression "we see how highley influential this was as we now see the use of regular expressions in so many different programming languages such as Python, C#, Javascript and many more but also regular expressions" and as I continue you will see me dig a bit deeper with my answer to this question but before that let me give you some details about formal languages in the context of regular expressions.

We know we can use regular expression (regex) in languages such as Python and Javascript but if we step out of those languages and use this same approach then can we expect the same results to be produced.

Now most of us like to copy and paste to save time and comfort but can we use this same method across all different programming languages and can all programming languages accept this.

Every regular expression denotes a formal language, but a formal language is only regular if there is a regular expression denoting it.

While programming languages are composed of a syntax representing program as strings and characters and is the meaning of the program and on the other hand a formal language are syntaxes without any meaning and is used to study the structure of a set of strings defined formally without attaching meaning to those set of strings.

So, as I move on with my answer to this question, can all formal languages be encoded as a regular expression, to break it down easy and simply in layman's terms I will say that most formal languages can be encoded as a regular expression.

This all ties in with the concept of a regular language, a regular language that can be defined by a regular expression.

For information regarding this topic you can look at sites such as:
- [Lecture on Formal Languages,<br> http://www.cs.ucc.ie/~dgb/courses/toc/handout7.pdf](http://www.cs.ucc.ie/~dgb/courses/toc/handout7.pdf)
- [Wikipedia,<br> https://en.wikipedia.org/wiki/Formal_language](https://en.wikipedia.org/wiki/Formal_language)
- [Wikipedia,<br> https://en.wikipedia.org/wiki/Regular_expression](https://en.wikipedia.org/wiki/Regular_expression)

There are many reasons why most formal languages can use regular expressions while some can't, one of the reasons that not all formal languages can be encoded using regular expressions is as simple as not all languages support the same features which means for language such as the aforementioned PERl using this type of code is perfectly fine while in some other languages it may completely unreadable and impossible to debug.

Some languages may use the same syntax for different features and even for the same features, but they can also exhibit different behaviour which makes it hard to reuse the regular expressions across different formal languages.

So long story short, technically no not all formal languages can be encoded as regular expressions for many reasons while there are a lot of languages that use regular expressio there is also many that don't for many reasons.

For this question in general if you have more questions about it, I suggest you read this document which I found very helpful in discussing this question:

[*Why Aren't Regular Expressions a Lingua Franca? *, An Empirical Study on the Re-use and Portability of Regular Expressions,<br> https://people.cs.vt.edu/~davisjam/downloads/publications/DavisMichaelCoghlanServantLee-LinguaFranca-ESECFSE19.pdf](https://people.cs.vt.edu/~davisjam/downloads/publications/DavisMichaelCoghlanServantLee-LinguaFranca-ESECFSE19.pdf)

 ## References

 Here is a list of references that helped me with the research of my project:

 1. [Why Aren't Regular Expressions a Lingua Franca?*, An Empirical Study on the Re-use and Portability of Regular Expressions,<br> https://medium.com/@davisjam/why-arent-regexes-a-lingua-franca-esecfse19-a36348df3a2](https://medium.com/@davisjam/why-arent-regexes-a-lingua-franca-esecfse19-a36348df3a2)
 2. [Mastering Regular Expressions by Jeffrey Friedl,<br> https://www.amazon.co.uk/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124](https://www.amazon.co.uk/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124)
 3. [Regular Expressions: Regexes in Python*, Real Python,<br> https://realpython.com/regex-python](https://realpython.com/regex-python/)
 4. [Teach Yourself Regular Expression in 10 Minutes by Ben Forta,<br> http://mygugazabocu.bloggersdelight.dk/sams-teach-yourself-regular-expressions-in-10-minutes-pdf](http://mygugazabocu.bloggersdelight.dk/sams-teach-yourself-regular-expressions-in-10-minutes-pdf)
 5. [Wikipedia,<br> https://en.wikipedia.org/wiki/Regular_expression/](https://en.wikipedia.org/wiki/Regular_expression)
 6. [Python Regular Expression Tutorial,,<br> https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)
 7. [Google For Education,<br> https://developers.google.com/edu/python/regular-expressions/](https://developers.google.com/edu/python/regular-expressions)
 8. [*Regular Expression Matching Can Be Simple And Fast*,Russ Cox,<br> https://swtch.com/~rsc/regexp/regexp1.html](https://swtch.com/~rsc/regexp/regexp1.html)
 9. [Lecture on Formal Languages,<br> http://www.cs.ucc.ie/~dgb/courses/toc/handout7.pdf](http://www.cs.ucc.ie/~dgb/courses/toc/handout7.pdf)
 10. [Github,<br> https://github.com/Emmanuel-Osabuehien/graph-theory-project](https://github.com/Emmanuel-Osabuehien/graph-theory-project)