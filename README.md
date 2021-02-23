# Project: Graph Theory 2021
**Name:** Emmanuel Osabuehien
**Student ID:** G00373559
**Module:** Graph Theory

Q. What is a regular expression?

A. Before we get into what is a regular expession in python, the whole concept and development of a regular expression can be dated back to as early as the 1950's and maybe even in the 1940's but in 1951, the concept of regular language was created by a mathematician by the name of Stephen Cole Kleene, where we have a language that can be idenitfied by a finite automaton and represented using regular expression.

As we move on to the 1960's where a Ken Thompson who was a computer science pioneer and is also one of the designers of Unix (a multitasking, multiuser computing operating system) would add the concept of matching patterns in a text editor using Stephen Cole Kleene's code and in the 1970's is when we really see regular expressions takeover the programming world, another note is the whole concept became common use with Unix text-processing.
 
As we move on to modern day computer science, we see how highley influential this was as we now see the use of regular expressions in so many different programming languages such as Python, C#, Javascript and many more but also regular expressions are used in text editor as well as a use for other tools where we can regulate if a special sequence of characters or string match a specific pattern.

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

So this all here is all about regular expressions from a brief history of the concept and creation, to it's impact in programming languages, to some examples of it's uses and most important the definition of what is a regular expression.

 Q. How do regular expressions differ across implementations?

 A.

 Q. Can all formal languages be encoded as regular expressions?

 A. 